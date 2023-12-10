from datetime import datetime

from flask import Blueprint, request, redirect, flash, url_for, render_template, session, jsonify

from App.forms import RegisterForm, LoginForm
from App.models import *
from werkzeug.security import generate_password_hash, check_password_hash

interviewer = Blueprint('interviewer', __name__)


@interviewer.route('/get-all-meetingRooms', methods=['GET', 'POST'])
def get_meeting_rooms():
    # 假设你要获取当前月份的会议室数据
    now = datetime.now()
    meeting_rooms = MeetingRoom.query.filter(db.extract('month', MeetingRoom.startTime) == now.month).all()
    meeting_rooms_data = [{
        'MID': room.MID,
        'startTime': room.startTime.isoformat(),
        'endTime': room.endTime.isoformat(),
        'status': room.status
    } for room in meeting_rooms]

    return jsonify(meeting_rooms_data)


