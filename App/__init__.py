from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO

from . import admin_view, interviewer_view, videoAndCode
from .views import blue

from .extents import init_exts

from .socket_config import socketio

from flask_sslify import SSLify

import socket

# 动态获取ip
def get_host_ip():
    try:
        # 创建一个socket来连接一个不存在的地址
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    print(ip)
    return ip



HOSTNAME = get_host_ip()
PORT = 3306
USERNAME = "root"
# PASSWORD = "2003721gavin?"
PASSWORD = "131a2abLZH"
FLASK_DB = "online_interview_system"



def create_app():
    app = Flask(__name__)
    sslify = SSLify(app)
    CORS(app)
    app.register_blueprint(blueprint=blue)
    app.register_blueprint(admin_view.admin, url_prefix='/admin')
    app.register_blueprint(interviewer_view.interviewer, url_prefix='/interviewer')
    app.register_blueprint(videoAndCode.vac, url_prefix='/vac')

    app.config['SECRET_KEY'] = 'COMP3017J'

    db_uri = f'mysql+pymysql://{USERNAME}:{PASSWORD}@localhost:{PORT}/{FLASK_DB}?charset=utf8mb4'
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    socketio.init_app(app, cors_allowed_origins="*") # 正确绑定 socketio 实例

    init_exts(app)

    # 绑定 Flask 应用到 SocketIO
    socketio.init_app(app)

    return app

