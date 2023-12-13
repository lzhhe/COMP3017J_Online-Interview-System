import os
import subprocess
import time
import uuid

from agora_token_builder import RtcTokenBuilder
from agora_token_builder.RtcTokenBuilder import Role_Publisher
from flask import Blueprint, request, render_template, jsonify
from flask_socketio import emit

from .socket_config import socketio
from App.models import *

vac = Blueprint('vac', __name__)


@vac.route('/videoAndCode.html', methods=['GET', 'POST'])
def video_and_code():
    return render_template('videoAndCode.html')


@vac.route('/candidate.html', methods=['GET', 'POST'])
def receive():
    return render_template('candidate.html')


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
                output = "通过所有测试用例"
            else:
                # output = result.stderr
                output = "未通过所有测试用例，请修改代码后再次尝试"
            return jsonify({'output': output})



        elif language == 'java':
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
                    'import java.util.Arrays;\n'
                )

                class_name = "Main" + uuid.uuid4().hex
                file_name = class_name + ".java"

                modified_test_code = test_code.replace("public class Main", "public class " + class_name)

                # 合并代码
                full_code = common_imports + modified_test_code + "\n" + user_code
                with open(file_name, 'w') as file:
                    file.write(full_code)
                print(full_code)
                # 编译和运行 Java 程序
                compile_result = subprocess.run(['javac', file_name], capture_output=True, text=True)
                if compile_result.returncode != 0:
                    return jsonify({'error': compile_result.stderr})
                run_result = subprocess.run(['java', '-ea', class_name], capture_output=True, text=True)
                if run_result.returncode == 0:
                    output = "通过所有测试用例"
                else:
                    output = "未通过所有测试用例，请修改代码后再次尝试"
                return jsonify({'output': output})
            finally:
                # 清理生成的文件
                if os.path.exists(file_name):
                    os.remove(file_name)
                if os.path.exists(file_name.replace('.java', '.class')):
                    os.remove(file_name.replace('.java', '.class'))
                if os.path.exists("Solution.class"):
                    os.remove("Solution.class")
                    # print("Solution.class" + "已被成功删除。")

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


@vac.route('/get_problem_description', methods=['POST'])
def get_problem_description():
    data = request.get_json()
    language = data.get('language')
    proID = data.get('proID')

    problem = Problem.query.filter_by(ProID=proID).first()
    if problem:
        description = problem.pythonDescription if language == 'python' else problem.javaDescription
        return jsonify({'description': description})
    else:
        return jsonify({'description': None})





@vac.route('/get_token')
def get_token():
    app_id = "b5a04df0256a451ebec8ee8774ef85ff"
    app_certificate = "612b6116aa5c42a6b0900b77aba1086b"
    channel_name = request.args.get('channelName')  # 从请求中获取频道名称
    print(channel_name)
    uid = request.args.get('uid', 0)  # 从请求中获取用户ID，如果没有则默认为 0
    print(uid)

    expiration_time_in_seconds = 7200  # Token 有效时间，例如1小时
    current_time = int(time.time())
    privilege_expired_ts = current_time + expiration_time_in_seconds

    token = RtcTokenBuilder.buildTokenWithUid(app_id, app_certificate, channel_name, int(uid), Role_Publisher, privilege_expired_ts)
    print(token)
    return jsonify({'token': token})


@socketio.on('update_editor_content')
def handle_editor_update(data):
    # print("USING the update_editor_content function")
    emit('editor_content_updated', data, broadcast=True, include_self=False)



# @vac.route('/getFastboardRoom', methods=['GET'])
# def get_fastboard_room():
#     app_identifier = "3MKPgJlsEe6oBM-FcV-UgA/6hO0-eLyLEoFpA"
#     sdk_token = "NETLESSSDK_YWs9UXRvS01odUtmOXBSa29YQyZub25jZT1lOTRmMzMyMC05OTcxLTExZWUtOGYyMS04ZDg1NDBiMjY4MjQmcm9sZT0wJnNpZz1mMGM2YTI3ZWE5NTNkZmFmMTk1MmViYTliZTI2NGU3YmY2MjQ2NWIwOTVlNWJiYzA5MDRhMjIwNzhiYTg4Nzk1"
#
#     # 创建房间
#     room_response = requests.post(
#         "https://api.netless.link/v5/rooms",
#         headers={"token": sdk_token, "Content-Type": "application/json", "region": "cn-hz"}
#     )
#     room_uuid = room_response.json()["uuid"]
#
#     # 生成 Room Token
#     token_response = requests.post(
#         f"https://api.netless.link/v5/tokens/rooms/{room_uuid}",
#         headers={"token": sdk_token, "Content-Type": "application/json", "region": "cn-hz"},
#         json={"lifespan": 3600000, "role": "admin"}
#     )
#     room_token = token_response.text
#
#     return jsonify({"uuid": room_uuid, "token": room_token})