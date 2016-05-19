from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Regexp, ValidationError, Email, Length, EqualTo
from models import User


def check_if_name_exists(form, field):
    if User.select().where(User.username == field.data).exists():
        raise ValidationError('User with that name already exists.')


def check_if_email_exists(form, field):
    if User.select().where(User.email == field.data).exists():
        raise ValidationError('A user account has already been created with that email.')


class RegisterForm(Form):
    username = StringField('Username', validators=[DataRequired(message='Username is required'),
                                                                check_if_name_exists])
    email = StringField('Email', validators=[Email(), DataRequired(message='A valid email address is required'),
                                             check_if_email_exists])
    password = PasswordField('Email', validators=[DataRequired(message='A valid password is required'),
                                                  Length(min=6), EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm Password', validators=[DataRequired()])


class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
