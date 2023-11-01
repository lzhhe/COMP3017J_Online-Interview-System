from flask import Blueprint, request, redirect, flash, url_for, render_template, session
from werkzeug.security import check_password_hash

from .forms import RegisterForm, LoginForm
from .models import *
from werkzeug.security import generate_password_hash, check_password_hash


blue = Blueprint('user',__name__)
@blue.route('/')
@blue.route('/loginAndRegister')
def loginAndRegister():
    return render_template('login.html')


@blue.route('/login', methods=['GET', 'POST'])
def login():
    # print("checked")

    if request.method == 'GET':
        # print("GET")
        return render_template('login.html')


    elif request.method == 'POST':
        # print("POST")
        form = LoginForm(request.form)
        print(form.data)
        if form.validate():
            # print("get form") # here need to consider why
            username = form.signInUsernameField.data
            password = form.signInPasswordField.data
            user = User.query.filter_by(username=username).first()
            if user and check_password_hash(user.password, password):
                # print("password correct and find it ")
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
        # print("get form")
        # print (form.data)
        if form.validate():
            email = form.signUpEmailField.data
            username = form.signUpUsernameField.data
            password = form.signUpPasswordField.data
            status = form.signUpStuatusField.data
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
            user = User(username=username, password=hashed_password, email=email, status=status)
            db.session.add(user)
            db.session.commit()
            response = redirect('/home')
            session['UID'] = user.UID
            return response
        else:
            return render_template('login.html', errors=form.errors)


@blue.route('/home')
def home():
    return render_template('home.html')

# Define a route for testing purposes

@blue.route('/whiteboard')
def whiteboard():# put application's code here
    return render_template('whiteboard.html')
