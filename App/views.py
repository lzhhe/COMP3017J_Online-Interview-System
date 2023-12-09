from flask import Blueprint, request, redirect, flash, url_for, render_template, session, jsonify

from App.forms import RegisterForm, LoginForm
from App.models import *
from werkzeug.security import generate_password_hash, check_password_hash




blue = Blueprint('user', __name__)


@blue.route('/')
@blue.route('/loginAndRegister')
def loginAndRegister():
    return render_template('login.html')


@blue.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    elif request.method == 'POST':
        form = LoginForm(request.form)
        if form.validate():
            username = form.signInUsernameField.data
            password = form.signInPasswordField.data
            user = User.query.filter_by(username=username).first()

            if user and check_password_hash(user.password, password):
                session['UID'] = user.UID
                session['status'] = user.status  # Store user status in session

                # Redirect based on user status
                if user.status == 0:  # Admin
                    return redirect(url_for('user.admin_home'))
                elif user.status == 1:  # Interviewer/HR
                    return redirect(url_for('user.interviewer_home'))
                else:  # Regular User
                    return redirect(url_for('user.home'))
            else:
                return render_template('login.html', errors="The password is wrong or user does not exist.")
        else:
            return render_template('login.html', errors=form.errors)



@blue.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        form = RegisterForm(request.form)
        if form.validate():
            email = form.signUpEmailField.data
            username = form.signUpUsernameField.data
            password = form.signUpPasswordField.data
            status = form.signUpStatusField.data
            # print(status)
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
            user = User(username=username, password=hashed_password, email=email, status=status)
            db.session.add(user)
            db.session.commit()
            response = redirect('/home')
            session['UID'] = user.UID
            return response
        else:
            return render_template('login.html', errors=form.errors)

@blue.route('/home')
def home():  # put application's code here
    return render_template('home.html')

@blue.route('/admin_home')
def admin_home():  # put application's code here
    return render_template('admin_home.html')

@blue.route('/interviewer_home')
def interviewer_home():  # put application's code here
    return render_template('interviewer_home.html')


# Define a route for testing purposes

@blue.route('/video')
def video():  # put application's code here
    return render_template('video.html')

@blue.route('/get-positions')
def get_positions():
    positions = Position.query.all()
    positions_data = [{'PID': position.PID, 'positionName': position.positionName} for position in positions]
    return jsonify(positions_data)

@blue.route('/get-available-times')
def get_available_times():
    available_times = MeetingRoom.query.filter(MeetingRoom.status == 0).all()
    times_data = [{'MID': time.MID, 'startTime': time.startTime.strftime("%Y-%m-%d %H:%M"), 'endTime': time.endTime.strftime("%Y-%m-%d %H:%M")} for time in available_times]
    return jsonify(times_data)

@blue.route('/submit-application', methods=['GET','POST'])
def submit_application():

    try:
        if request.method == 'POST':
            data = request.json
            uid = session.get('UID')
            if not uid:
                return jsonify({'error': 'User not logged in'}), 401

            new_application = Application(
                UID=uid,
                PID=data['position'],
                MID=data['time'],
                salary=data['salary'],
                introduction=data['introduction']
            )
            db.session.add(new_application)
            db.session.commit()

            return jsonify({'message': 'Application submitted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@blue.route('/view-applications')
def view_applications():
    if 'UID' not in session:
        return jsonify({'error': 'User not logged in'}), 401

    uid = session['UID']
    user_applications = Application.query.filter_by(UID=uid).all()

    applications_data = []
    for app in user_applications:
        position = Position.query.get(app.PID)
        meeting_room = MeetingRoom.query.get(app.MID)

        applications_data.append({

            'position': position.positionName if position else 'N/A',
            'meeting_room': {
                'start_time': meeting_room.startTime.strftime("%Y-%m-%d %H:%M"),
                'end_time': meeting_room.endTime.strftime("%Y-%m-%d %H:%M")
            } if meeting_room else {'start_time': 'N/A', 'end_time': 'N/A'},

            'status': app.status
        })

    return jsonify(applications_data)

@blue.route('/view-interview-results', methods=['GET'])
def view_interview_results():
    current_user_id = session.get('UID')  # Assuming the user's ID is stored in the session

    if current_user_id is None:
        return jsonify({'error': 'User not logged in'}), 401

    try:
        # Fetching interview results for the current user
        interview_results = db.session.query(
            InterviewResult,
            Position.positionName,
            MeetingRoom.startTime,
            MeetingRoom.endTime
        ).join(Application, InterviewResult.AID == Application.AID)\
         .join(Position, Position.PID == Application.PID)\
         .join(MeetingRoom, MeetingRoom.MID == Application.MID)\
         .filter(Application.UID == current_user_id).all()

        # Preparing the final results
        formatted_results = [{
            'positionName': result.positionName,
            'timePeriod': f"{result.startTime.strftime('%Y-%m-%d %H:%M')} - {result.endTime.strftime('%Y-%m-%d %H:%M')}",
            'status': 'Reject' if result.InterviewResult.status == 0 else 'Accept' if result.InterviewResult.status == 1 else 'Pending'
        } for result in interview_results]

        return jsonify(formatted_results)
    except Exception as e:
        return jsonify({'error': str(e)}), 500




