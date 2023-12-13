from flask import Flask
from flask_cors import CORS

from . import admin_view, interviewer_view, videoAndCode
from .views import blue

from .extents import init_exts

HOSTNAME = "127.0.0.1"
PORT = 3306
USERNAME = "root"
# PASSWORD = "2003721gavin?"
PASSWORD = "131a2abLZH"
FLASK_DB = "online_interview_system"


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(blueprint=blue)
    app.register_blueprint(admin_view.admin, url_prefix='/admin')
    app.register_blueprint(interviewer_view.interviewer, url_prefix='/interviewer')
    app.register_blueprint(videoAndCode.vac, url_prefix='/vac')

    app.config['SECRET_KEY'] = 'COMP3017J'

    db_uri = f'mysql+pymysql://{USERNAME}:{PASSWORD}@localhost:{PORT}/{FLASK_DB}?charset=utf8mb4'
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    init_exts(app)

    return app

