from flask_wtf import FlaskForm
from wtforms import Form, validators,TextField,StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
class LoginForm(FlaskForm):
    username = StringField('Username', validators= [DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
class PostForm(FlaskForm):
    ina = StringField('Username', validators= [DataRequired()])

class ReusableForm(Form):
    age = TextField('Age:', validators=[validators.required()])
