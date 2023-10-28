from .extents import db


class User(db.Model):
    __tablename__ = 'user'
    UID = db.Column(db.Integer, primary_key=True, autoincrement=True)  # id唯一
    username = db.Column(db.String(30), unique=True, nullable=False)  # 用户名
    password = db.Column(db.String(256), nullable=False)  # 密码
    email = db.Column(db.String(30), nullable=False)  # 邮箱
    status = db.Column(db.Integer, nullable=False, default=2)  # 0是管理员，1是面试官，2是应试者



