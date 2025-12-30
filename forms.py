from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Regexp

class StudentForm(FlaskForm):
    firstname = StringField('First Name', validators=[
        DataRequired(), Length(min=2, max=50),
        Regexp(r'^[A-Za-z]+$', message="Only letters are allowed")
    ])
    lastname = StringField('Last Name', validators=[
        DataRequired(), Length(min=2, max=50),
        Regexp(r'^[A-Za-z]+$', message="Only letters are allowed")
    ])
    email = StringField('Email', validators=[
        DataRequired(), Email(message='Invalid email format')
    ])
    phone = StringField('Phone', validators=[
        DataRequired(), Regexp(r'^\+?[0-9\-]{7,15}$', message="Invalid phone number")
    ])
    submit = SubmitField('Submit')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(), EqualTo('password', message='Passwords must match')
    ])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
