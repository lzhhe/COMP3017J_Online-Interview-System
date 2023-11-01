from flask import Flask, request, jsonify,render_template
import subprocess
import sys
from App import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
