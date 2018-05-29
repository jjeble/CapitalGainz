from flask import render_template
from app import app
from app.forms import LoginForm
from app.forms import PostForm, ReusableForm, QuestionsForm
from guess_language import guess_language
from flask import jsonify
from flask import request
from flask import flash
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


@app.route("/hello", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)

    print(form.errors)
    if request.method == 'POST':

        age=request.form['age']



        if form.validate():
            # Save the comment here.
            flash('ok ' + age)
            years_for_college = 18 - int(age)
            info = "That means your child has "+ str(years_for_college) + " years left for college!"
            flash
        else:
            flash("Fill out your child's age )

    return render_template('hello.html', form=form)

@app.route('/questionnaire',methods=['GET','POST'])
def questions():
    form = QuestionsForm(request.form)
    if request.method == 'POST':  #this block is only entered when the form is submitted
        language = request.form.get('age')
        return '''<h1>The language value is: bal</h1>
                  <h1>The framework value is: bah</h1>'''
    return render_template('questions.html',form = form, title='Questions')


@app.route('/translate',methods=['POST'])
def translate_text():
    return jsonify({'text': translate(request.form['text'],
                                      request.form['source_language'],
                                      request.form['dest_language'])})

@app.route('/welcome')
def welcome():
    return render_template('welcome.html',title = 'Welcome')

@app.route('/options')
def options():
    print('hi')
    return render_template('options.html',title = 'Options')
