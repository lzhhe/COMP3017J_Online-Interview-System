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
    code = data['code']
    language = data['language']

    try:
        if language == 'python':
            # Python execution logic
            result = subprocess.run(['python', '-c', code], capture_output=True, text=True)
            output = result.stdout if result.returncode == 0 else result.stderr

        elif language == 'java':
            # Extract class name from the Java code
            match = re.search(r'public\s+class\s+(\w+)', code)
            if not match:
                return jsonify({'error': 'Invalid Java code. No public class found.'})

            original_class_name = match.group(1)
            unique_suffix = uuid.uuid4().hex
            class_name = f"{original_class_name}_{unique_suffix}"
            code = code.replace(original_class_name, class_name, 1)
            file_name = f"{class_name}.java"

            with open(file_name, 'w') as file:
                file.write(code)

            # Compile the Java code
            compile_result = subprocess.run(['javac', file_name], capture_output=True, text=True)
            if compile_result.returncode != 0:
                os.remove(file_name)
                return jsonify({'error': compile_result.stderr})

            # Run the compiled Java code
            run_result = subprocess.run(['java', class_name], capture_output=True, text=True)
            os.remove(file_name)
            os.remove(class_name + '.class')
            output = run_result.stdout if run_result.returncode == 0 else run_result.stderr

        else:
            return jsonify({'error': 'Unsupported language'})

        return jsonify({'output': output})

    except Exception as e:
        return jsonify({'error': str(e)})

# @vac.route('/get_problem_title', methods=['POST'])
# def get_problem_title():
#     data = request.get_json()
#     problem_id = data['problem_id']
#     language = data['language']
#
#     problem = Problem.query.filter_by(ProID=problem_id).first()
#     if not problem:
#         return jsonify({'error': 'Problem not found'})
#
#     if language == 'python':
#         title = problem.pythonTitle
#     elif language == 'java':
#         title = problem.javaTitle
#     else:
#         return jsonify({'error': 'Unsupported language'})
#
#     return jsonify({'title': title})
