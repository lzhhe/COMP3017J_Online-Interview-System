from flask import render_template

from App import create_app

app = create_app()


# Define a route for testing purposes
@app.route('/home')
def home():
    return render_template('home.html')

# Define a route for testing purposes
@app.route('/')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
