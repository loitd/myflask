from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email, EqualTo, InputRequired, IPAddress, MacAddress, Optional, Regexp, URL, UUID, AnyOf, NoneOf

class LoginForm(FlaskForm):
    inputEmail = EmailField('inputEmail', validators=[Email(), InputRequired()])
    inputPassword = PasswordField('inputPassword', validators=[DataRequired()])
    # remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    
class RegisterForm(FlaskForm):
    inputName = StringField('inputName', validators=[DataRequired(), Regexp('[a-zA-Z0-9._-]{6,20}')])
    inputEmail = EmailField('inputEmail', validators=[Email(), InputRequired()])
    inputPassword = PasswordField('inputPassword', validators=[DataRequired()])
    submit = SubmitField('Register')
    