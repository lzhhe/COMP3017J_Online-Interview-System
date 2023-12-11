import os
import re
import subprocess
import json
import uuid
from datetime import datetime

from flask import Blueprint, request, redirect, flash, url_for, render_template, session, jsonify

from App.forms import RegisterForm, LoginForm
from App.models import *
from werkzeug.security import generate_password_hash, check_password_hash

vac = Blueprint('vac', __name__)


@vac.route('/videoAndCode.html', methods=['GET', 'POST'])
def video_and_code():
    return render_template('videoAndCode.html')


@vac.route('/execute_code', methods=['POST'])
def execute_code():
    data = request.get_json()
    user_code = data.get('code')
    language = data.get('language')
    problem_id = data.get('proID')  # 获取题目ID

    if not all([user_code, language, problem_id]):
        return jsonify({'error': 'Missing data (code, language, or problem ID)'})

    try:
        problem = Problem.query.filter_by(ProID=problem_id).first()
        if not problem:
            return jsonify({'error': 'Problem not found'})

        # 根据选择的语言获取测试代码
        test_code = problem.pythonTestCode if language == 'python' else problem.javaTestCode

        # 组合用户代码和测试代码
        full_code = user_code + "\n" + test_code

        if language == 'python':
            result = subprocess.run(['python', '-c', full_code], capture_output=True, text=True)
            if result.returncode == 0:
                # 执行成功，表示通过所有测试用例
                output = "通过所有测试用例"
            else:
                # 执行失败，返回错误信息
                # output = result.stderr
                output = "未通过所有测试用例，请修改代码后再次尝试"
            return jsonify({'output': output})

        if language == 'java':
            try:
                common_imports = (
                    'import java.util.*;\n'
                    'import java.io.*;\n'
                    'import java.math.*;\n'
                    'import java.net.*;\n'
                    'import java.text.*;\n'
                    'import java.time.*;\n'
                    'import java.sql.*;\n'
                    'import java.util.stream.*;\n'
                    # 移除了对 java.awt.* 和 java.swing.* 的引用
                )

                # 生成一个唯一的文件名
                class_name = "Solution_" + uuid.uuid4().hex
                file_name = class_name + ".java"
                test_file_name = "Main.java"

                # 将用户代码和测试代码写入文件
                modified_user_code = common_imports + user_code.replace("public class Solution",
                                                                        "public class " + class_name)
                with open(file_name, 'w') as file:
                    file.write(modified_user_code)

                modified_test_code = common_imports + test_code.replace("Solution()", class_name + "()").replace(
                    "Solution ", class_name + " ")
                with open(test_file_name, 'w') as file:
                    file.write(modified_test_code)
                # 编译 Java 程序
                compile_result = subprocess.run(['javac', file_name, test_file_name], capture_output=True, text=True)

                if compile_result.returncode != 0:
                    return jsonify({'error': compile_result.stderr})

                # 运行 Java 程序

                run_result = subprocess.run(['java', 'Main'], capture_output=True, text=True)

                if run_result.returncode == 0:
                    output = "未通过所有测试用例，请修改代码后再次尝试"
                else:
                    output = run_result.stderr
                return jsonify({'output': output})

            finally:
                # 清理生成的文件
                if os.path.exists(file_name):
                    os.remove(file_name)
                if os.path.exists(class_name + ".class"):
                    os.remove(class_name + ".class")
                if os.path.exists(test_file_name):
                    os.remove(test_file_name)
                if os.path.exists("Main.class"):
                    os.remove("Main.class")

        else:
            return jsonify({'error': 'Unsupported language'})

    except Exception as e:
        return jsonify({'error': str(e)})

    # 默认返回，以防万一
    return jsonify({'error': 'Unexpected error occurred'})


@vac.route('/get_problems')
def get_problems():
    problems = Problem.query.all()
    problems_list = [{'ProID': p.ProID, 'Description': p.problemDescription} for p in problems]
    return jsonify(problems_list)


@vac.route('/get_problem_title', methods=['POST'])
def get_problem_title():
    data = request.get_json()
    language = data.get('language')
    proID = data.get('proID')

    problem = Problem.query.filter_by(ProID=proID).first()
    if problem:
        title = problem.pythonTitle if language == 'python' else problem.javaTitle
        return jsonify({'title': title})
    else:
        return jsonify({'title': None})
