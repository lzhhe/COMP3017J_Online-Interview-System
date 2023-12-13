from flask import Flask, request, jsonify, render_template
import subprocess
import sys
from App import create_app, socketio

app = create_app()

if __name__ == '__main__':
    socketio.run(app, host = '0.0.0.0', debug=True,allow_unsafe_werkzeug=True)
