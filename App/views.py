from flask import Blueprint, request, redirect, flash, url_for, render_template

from .forms import RegisterForm, LoginForm
from .models import *

blue = Blueprint('user',__name__)

@blue.route('/', methods=['GET', 'POST'])  # 直接将根URL指向login函数
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.signInUsernameField.data
        password = form.signInPasswordField.data

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            flash('Logged in successfully!', 'success')
            return redirect(url_for('user.hello_world'))  # Redirect to a protected page or dashboard
        else:
            flash('Login failed. Check your username and password.', 'danger')

    return render_template('login.html', form=form)

@blue.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        email = form.signUpEmailField.data
        username = form.signUpUsernameField.data
        password = form.signUpPasswordField.data

        new_user = User(email=email, username=username,
                        password=password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('user.login'))

    return render_template('register.html', form=form)


@blue.route('/home')
def home():# put application's code here
    return render_template('home.html')

# Define a route for testing purposes
@blue.route('/')
def login():# put application's code here
    return render_template('login.html')

@blue.route('/whiteboard')
def whiteboard():# put application's code here
    return render_template('whiteboard.html')
