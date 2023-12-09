from .extents import db

class User(db.Model):
    __tablename__ = 'user'
    UID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True) # Increased length for email
    status = db.Column(db.Integer, nullable=False, default=2)  # 0 admin 1 HR 2 user

class Position(db.Model):
    __tablename__ = 'position'
    PID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    positionName = db.Column(db.String(255), nullable=False)
    positionDescription = db.Column(db.String(1000))
    positionRequirement = db.Column(db.String(1000))
    salary = db.Column(db.Integer, nullable=False)

class MeetingRoom(db.Model):
    __tablename__ = 'meetingRoom'
    MID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    startTime = db.Column(db.DateTime, nullable=False)
    endTime = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Integer, nullable=False)  # 0 available 1 not available

class InterviewResult(db.Model):
    __tablename__ = 'interviewResult'
    IRID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    AID = db.Column(db.Integer, db.ForeignKey('application.AID'))
    answer = db.Column(db.Text)
    grade = db.Column(db.Integer, nullable=False) # pass examples
    evaluation = db.Column(db.Text, nullable=False)
    status = db.Column(db.Integer, nullable=False)  # 0 reject 1 accept 2 pending

class Application(db.Model):
    __tablename__ = 'application'
    AID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    UID = db.Column(db.Integer, db.ForeignKey('user.UID'))
    PID = db.Column(db.Integer, db.ForeignKey('position.PID'))
    MID = db.Column(db.Integer, db.ForeignKey('meetingRoom.MID'))
    salary = db.Column(db.Integer, nullable=False)
    introduction = db.Column(db.Text, nullable=False)
    status = db.Column(db.Integer, nullable=False, default=0)  # 0 reject 1 accept


