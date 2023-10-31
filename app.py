from flask import Flask, request, jsonify,render_template
import subprocess
import sys
from App import create_app

app = create_app()


# @app.route('/execute', methods=['POST'])
# def execute():
#     data = request.json
#     code = data['code']
#
#     # CAUTION: This method of executing code can be unsafe. You may want to use a sandbox or other security mechanism.
#     try:
#         output = subprocess.check_output([sys.executable, "-c", code], stderr=subprocess.STDOUT, text=True)
#     except subprocess.CalledProcessError as e:
#         output = e.output
#
#     return jsonify({"output": output})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
