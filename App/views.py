from flask import Blueprint, request, redirect, flash, url_for, render_template, session
from werkzeug.security import check_password_hash

from .forms import RegisterForm, LoginForm
from .models import *

blue = Blueprint('user',__name__)

@blue.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        form = LoginForm(request.form)
        if form.validate():
            username = form.signInUsernameField.data  # 修改这里
            password = form.signInPasswordField.data  # 修改这里
            user = User.query.filter_by(username=username).first()
            if check_password_hash(user.password, password):
                response = redirect('/home')
                session['UID'] = user.UID
                return response
            else:
                return render_template('login.html', errors="the password is wrong")
        else:
            return render_template('login.html', errors=form.errors)
@blue.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        form = RegisterForm(request.form)
        if form.validate():
            email = form.signUpEmailField.data  # 修改这里
            username = form.signUpUsernameField.data  # 修改这里
            password = form.signUpPasswordField.data  # 修改这里
            user = User(username=username,password=password,email=email)
            db.session.add(user)
            db.session.commit()
            response = redirect('/home')
            session['UID'] = user.UID
            return response
        else:
            return render_template('login.html', errors=form.errors)


@blue.route('/home')
def home():# put application's code here
    return render_template('home.html')

# Define a route for testing purposes

@blue.route('/whiteboard')
def whiteboard():# put application's code here
    return render_template('whiteboard.html')
