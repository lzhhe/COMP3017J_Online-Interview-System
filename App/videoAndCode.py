import os
import subprocess
import time
import uuid

from agora_token_builder import RtcTokenBuilder
from agora_token_builder.RtcTokenBuilder import Role_Publisher
from flask import Blueprint, request, render_template, jsonify, session, redirect, url_for
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

    token = RtcTokenBuilder.buildTokenWithUid(app_id, app_certificate, channel_name, int(uid), Role_Publisher,
                                              privilege_expired_ts)
    print(token)
    return jsonify({'token': token})


@socketio.on('update_editor_content')
def handle_editor_update(data):
    # print("USING the update_editor_content function")
    emit('editor_content_updated', data, broadcast=True, include_self=False)


@socketio.on('problem_description')
def handle_problem_description(data):
    emit('problem_description_updated', data, broadcast=True)


@socketio.on('output_update')
def handle_output_update(data):
    emit('output_updated', data, broadcast=True)


@socketio.on('send_uid')
def handle_send_uid(data):
    uid = data['UID']
    # 这里可以进行必要的处理，例如验证UID
    emit('uid_received', {'UID': uid}, broadcast=True)  # 广播给所有客户端


@socketio.on('draw')
def handle_draw(data):
    emit('draw', data, broadcast=True, include_self=False)


@vac.route('/get-earliest-application', methods=['POST'])
def get_earliest_application():
    data = request.json
    uid = data.get('UID')
    print(uid)

    earliest_application = db.session.query(
        Application,
        User.username,
        User.email,
        Position.positionName,
        MeetingRoom.startTime,
        MeetingRoom.endTime
    ).join(User, User.UID == Application.UID
           ).join(Position, Position.PID == Application.PID
                  ).join(MeetingRoom, MeetingRoom.MID == Application.MID
                         ).filter(Application.UID == uid
                                  ).order_by(Application.AID
                                             ).first()

    if earliest_application:

        application, username, email, positionName, startTime, endTime = earliest_application
        print("Application Data:", {
            'AID': application.AID,
            'UID': application.UID,
            'PID': application.PID,
            'MID': application.MID,
            'salary': application.salary,
            'introduction': application.introduction,
            'username': username,
            'email': email,
            'positionName': positionName,
            'startTime': startTime,
            'endTime': endTime
        })
        application_data = {
            'AID': application.AID,
            'UID': application.UID,
            'PID': application.PID,
            'MID': application.MID,
            'salary': application.salary,
            'introduction': application.introduction,
            'username': username,
            'email': email,
            'positionName': positionName,
            'interviewStartTime': startTime.isoformat().replace('T', ' '),
            'interviewEndTime': endTime.isoformat().replace('T', ' ')
        }
        return jsonify(application_data)
    else:
        return jsonify({'error': 'No applications found for the user'}), 404


@vac.route('/submit-interview-result', methods=['POST'])
def submit_interview_result():
    aid = request.form.get('AID')
    answer = request.form.get('editorContent')
    grade = request.form.get('grade')
    evaluation = request.form.get('evaluation')
    status = request.form.get('status')
    print(aid, answer, grade, evaluation, status)

    # 创建一个新的 InterviewResult 实例
    new_interview_result = InterviewResult(
        AID=aid,
        answer=answer,
        grade=grade,
        evaluation=evaluation,
        status=status
    )

    # 添加到数据库并提交
    db.session.add(new_interview_result)
    db.session.commit()

    # 重定向或返回成功消息
    return render_template('interviewer_home.html')


@vac.route('/get-accepted-applications')
def get_accepted_applications():
    # 查询所有状态为接受（例如，status = 1）的申请
    accepted_applications = db.session.query(
        Application,
        User.username,
        User.email,
        Position.positionName,
        MeetingRoom.startTime,
        MeetingRoom.endTime,
        Application.salary,
        Application.introduction
    ).join(User, User.UID == Application.UID
    ).join(Position, Position.PID == Application.PID
    ).join(MeetingRoom, MeetingRoom.MID == Application.MID
    ).filter(Application.status == 1  # 假设 status = 1 表示接受
    ).all()

    applications_data = []
    for application, username, email, positionName, startTime, endTime, salary, introduction in accepted_applications:
        application_info = {
            'username': username,
            'email': email,
            'positionName': positionName,
            'interviewStartTime': startTime.isoformat(),
            'interviewEndTime': endTime.isoformat(),
            'salary': salary,
            'introduction': introduction
        }
        applications_data.append(application_info)

    # 返回 JSON 数据
    return jsonify(applications_data)

@vac.route('/get-interview-results')
def get_interview_results():
    # 查询所有面试结果
    interview_results = db.session.query(
        InterviewResult,
        User.username,
        User.email,
        Position.positionName,
        InterviewResult.grade,
        InterviewResult.evaluation,
        InterviewResult.status
    ).join(Application, Application.AID == InterviewResult.AID
    ).join(User, User.UID == Application.UID
    ).join(Position, Position.PID == Application.PID
    ).all()

    results_data = []
    for result, username, email, positionName, grade, evaluation, status in interview_results:
        # 构造视频文件名


        result_info = {
            'username': username,
            'email': email,
            'positionName': positionName,
            'grade': grade,
            'evaluation': evaluation,
            'status': 'Accepted' if status == 1 else 'Rejected' if status == 0 else 'Pending',
            # 'videoFilename': video_filename  # 添加视频文件名
        }
        results_data.append(result_info)

    return jsonify(results_data)

@vac.route('/save_video', methods=['POST'])
def save_video():
    print("执行储存代码")
    video_file = request.data
    username = request.headers.get('Username')
    period = request.headers.get('Period')
    print(username)
    print(period)

    # 确保video目录存在
    os.makedirs('video', exist_ok=True)

    # 构造文件名

    filename = f"{username}_{period}.webm".replace(':', '_')

    # 保存文件
    filepath = os.path.join('video', filename)
    with open(filepath, 'wb') as f:
        f.write(video_file)
    print("储存完成")
    return jsonify({'message': 'Video saved successfully!'})