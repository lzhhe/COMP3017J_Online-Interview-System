from flask import Blueprint, render_template
from App.models import *


blue = Blueprint('user',__name__)

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