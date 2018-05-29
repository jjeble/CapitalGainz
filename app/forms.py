from flask_wtf import FlaskForm
from wtforms import Form, validators,TextField,StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange
class LoginForm(FlaskForm):
    username = StringField('Username', validators= [DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
class PostForm(FlaskForm):
    ina = StringField('Username', validators= [DataRequired()])

class ReusableForm(Form):
    age = IntegerField('Age:', validators=[validators.required(), NumberRange(min=0,max=20)])

class QuestionsForm(Form):
    age = TextField('Age:', validators=[validators.required()])
