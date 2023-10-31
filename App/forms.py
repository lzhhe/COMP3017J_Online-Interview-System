import wtforms
from wtforms.validators import Email, Length, ValidationError
from .models import *


class RegisterForm(wtforms.Form):
    signUpEmailField = wtforms.StringField(validators=[Email(message="please input the right style")])
    signUpUsernameField = wtforms.StringField(
        validators=[Length(min=1, max=50, message="please input the right length")])
    signUpPasswordField = wtforms.StringField(
        validators=[Length(min=6, max=14, message="please input the right length")])


    def validate_signUpUsernameField(self, field):
        username = field.data
        user = User.query.filter_by(username=username).first()
        if user:
            raise wtforms.ValidationError(message="the username has been existed")


class LoginForm(wtforms.Form):
    signInUsernameField = wtforms.StringField()
    signInPasswordField = wtforms.StringField()

    def validate_signInUsernameField(self, field):
        username = field.data
        user = User.query.filter_by(username=username).first()
        if not user:
            raise wtforms.ValidationError(message="the username has not been existed, please register")