import wtforms
from wtforms.validators import Email, Length, ValidationError
from .models import *

class LoginForm(wtforms.Form):
    signInUsernameField = wtforms.StringField('Username')
    signInPasswordField = wtforms.StringField('Password', validators=[Length(min=6, max=14, message="please input the right length")])

    def validate_signInUsernameField(self, field):
        username = field.data
        user = User.query.filter_by(username=username).first()
        if not user:
            raise wtforms.ValidationError(message="the username has not been existed, please register")

class RegisterForm(wtforms.Form):
    signUpEmailField = wtforms.StringField('Email')
    signUpUsernameField = wtforms.StringField('User', validators=[Length(min=1, max=50, message="please input the right length")])
    signUpPasswordField = wtforms.StringField('Password', validators=[Length(min=6, max=14, message="please input the right length")])

    def validate_signUpUsernameField(self, field):
        email = field.data
        user = User.query.filter_by(email=email).first()
        if user:
            raise wtforms.ValidationError(message="the email has been existed")
