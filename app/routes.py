from flask import render_template
from app import app
from app.forms import LoginForm
from app.forms import PostForm
from guess_language import guess_language
from flask import jsonify


@app.route('/',methods = ['GET','POST'])
@app.route('/index',methods = ['GET','POST'])
def index():
    form = LoginForm()
    #if form.validate_on_submit():

    user = {'username': 'Jay'}
    posts = [
         {
             'author': {'username': 'John'},
             'body': 'Beautiful day in Portland!'
         },
         {
             'author': {'username': 'Susan'},
             'body': 'The Avengers movie was so cool!'
         }
     ]
    return render_template('index.html', title='Sign In', form=form,user = user)
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)


@app.route('/translate',methods=['POST'])
def translate_text():
    return jsonify({'text': translate(request.form['text'],
                                      request.form['source_language'],
                                      request.form['dest_language'])})

@app.route('/welcome')
def welcome():
    return render_template('welcome.html',title = 'Welcome-Capital Group')
