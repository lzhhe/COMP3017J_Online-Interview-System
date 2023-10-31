from .extents import db


class User(db.Model):
    __tablename__ = 'user'
    UID = db.Column(db.Integer, primary_key=True, autoincrement=True)  # id唯一
    username = db.Column(db.String(30), unique=True, nullable=False)  # 用户名
    password = db.Column(db.String(256), nullable=False)  # 密码
    email = db.Column(db.String(30), nullable=False)  # 邮箱
    status = db.Column(db.Integer, nullable=False, default=2)  # 0是管理员，1是面试官，2是应试者


# class position(db.Model):
#     __table__ = 'position'
#     PID = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     positionName = db.Column(db.String(255), nullable=False)  # like java developer, architect
#     positionDescription = db.Column(db.String(1000), nullable=False)  # description
#     positionRequirement = db.Column(db.String(1000), nullable=False)  # job content
#     salary = db.Column(db.Integer, nullable=False)
#
#
# class interviewResult(db.Model): # to record the result of a interview
#     __table__name = 'interviewResult'
#     UID = db.Column(db.Integer, primary_key=True, autoincrement=True) # the user ID who is interviewed
#     answer = db.Column(db.Text)
#     grade = db.Column(db.Integer, nullable=False) # it is given by the examiner
#     evaluation = db.db.Column(db.Text, nullable=False)
#     status = db.db.Column(db.Integer, nullable=False)  # 1 pass, 2 reject, 3 alternate
#
#
# class applicaiton(db.Model):
#     __table__name = 'application'
#     UID = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     PID = db.Column(db.Integer, primary_key=True, autoincrement=True) # apply job ID
#     salary = db.Column(db.Integer)
