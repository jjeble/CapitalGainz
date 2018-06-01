from flask_wtf import FlaskForm
from wtforms import Form, validators,TextField,StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange, InputRequired
class LoginForm(FlaskForm):
    username = StringField('Username', validators= [DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
class PostForm(FlaskForm):
    ina = StringField('Username', validators= [DataRequired()])

class ReusableForm(Form):
    age = IntegerField('Age:', validators=[InputRequired(), NumberRange(min=0,max=100)]) #best practice to use InputRequired instead of DataRequired due to some details under the hood
