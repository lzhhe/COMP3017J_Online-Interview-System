from datetime import datetime

from flask import Blueprint, request, redirect, flash, url_for, render_template, session, jsonify

from App.forms import RegisterForm, LoginForm
from App.models import *
from werkzeug.security import generate_password_hash, check_password_hash

admin = Blueprint('admin', __name__)


@admin.route('/get-all-applications')
def get_all_applications():
    try:
        applications = db.session.query(
            User.username,
            MeetingRoom.startTime,
            MeetingRoom.endTime,
            Application.salary,
            Application.introduction,
            Application.AID
        ).join(User, User.UID == Application.UID) \
            .join(MeetingRoom, MeetingRoom.MID == Application.MID).all()

        applications_data = [{
            'username': app.username,
            'timePeriod': f"{app.startTime.strftime('%Y-%m-%d %H:%M')} - {app.endTime.strftime('%Y-%m-%d %H:%M')}",
            'salary': app.salary,
            'introduction': app.introduction,
            'applicationID': app.AID
        } for app in applications]

        return jsonify(applications_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@admin.route('/update-application-status', methods=['POST'])
def update_application_status():
    try:
        data = request.json
        application_id = data['applicationID']
        new_status = data['status']


        application = Application.query.get(application_id)
        if application:
            application.status = new_status
            db.session.commit()
            meeting_room_id = application.MID
            meetingRoom = MeetingRoom.query.get(meeting_room_id)
            if new_status==1: # accept
                meetingRoom.status = 1; # unavailable or occupy
            else:
                meetingRoom.status = 0;  # unavailable or occupy
            db.session.commit()
            return jsonify({'message': 'Application status updated'}), 200
        else:
            return jsonify({'error': 'Application not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@admin.route('/add-position', methods=['GET', 'POST'])
def add_position():
    if request.method == 'POST':
        try:
            data = request.get_json()
            position_name = data['positionName']
            position_description = data.get('positionDescription', '')
            position_requirement = data.get('positionRequirement', '')
            salary = data['salary']

            new_position = Position(
                positionName=position_name,
                positionDescription=position_description,
                positionRequirement=position_requirement,
                salary=salary
            )

            db.session.add(new_position)
            db.session.commit()

            return jsonify({'message': 'New position added successfully', 'success': True}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500




@admin.route('/add-meeting-room', methods=['POST'])
def add_meeting_room():
    if request.method == 'POST':
        try:
            data = request.get_json()
            print("Received data:", data)  # 打印接收到的数据

            # 检查必要字段
            if 'date' not in data or 'startTime' not in data or 'endTime' not in data:
                return jsonify({'error': 'Invalid JSON data. Missing required fields.'}), 400

            # 解析日期和时间
            date_str = data['date']
            start_time_str = data['startTime']
            end_time_str = data['endTime']

            try:
                start_datetime = datetime.strptime(f"{date_str} {start_time_str}", '%Y-%m-%d %H:%M')
                end_datetime = datetime.strptime(f"{date_str} {end_time_str}", '%Y-%m-%d %H:%M')
            except ValueError as ve:
                error_message = f'Invalid date or time format: {ve}'
                return jsonify({'error': error_message}), 400

            # 创建MeetingRoom实例，设置status为0（可用）
            new_meeting_room = MeetingRoom(startTime=start_datetime, endTime=end_datetime, status=0)
            db.session.add(new_meeting_room)
            db.session.commit()

            return jsonify({'message': 'Meeting room added successfully', 'success': True}), 200
        except Exception as e:
            error_message = str(e)
            return jsonify({'error': error_message}), 500

