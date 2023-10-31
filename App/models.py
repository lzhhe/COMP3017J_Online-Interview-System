from .extents import db
class User(db.Model):
    __tablename__ = 'user'
    UID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    status = db.Column(db.Integer, nullable=False, default=2) # admin 0 interviewer 1 user 2

class Position(db.Model):
    __tablename__ = 'position'
    PID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    positionName = db.Column(db.String(255), nullable=False)
    positionDescription = db.Column(db.String(1000), nullable=False)
    positionRequirement = db.Column(db.String(1000), nullable=False)
    salary = db.Column(db.Integer, nullable=False)

class InterviewResult(db.Model):
    __tablename__ = 'interviewResult'
    UID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    answer = db.Column(db.Text)
    grade = db.Column(db.Integer, nullable=False)
    evaluation = db.Column(db.Text, nullable=False)
    status = db.Column(db.Integer, nullable=False)

class Application(db.Model):
    __tablename__ = 'application'
    UID = db.Column(db.Integer, db.ForeignKey('user.UID'), primary_key=True)
    PID = db.Column(db.Integer, db.ForeignKey('position.PID'), primary_key=True)
    salary = db.Column(db.Integer)
