from flask import render_template
from app import app
from app.forms import LoginForm
from app.forms import PostForm, ReusableForm
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


@app.route('/questionnaire', methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)

    print(form.errors)
    if request.method == 'POST':
        if('age' in request.form):
            age=request.form['age']
            if form.validate():
                # Save the comment here.
                flash('ok ' + age)
                years_for_college = 18 - int(age)
                age_info = "That means your child has "+ str(years_for_college) + " years left for college!"


                return render_template('questions.html',form = form,age_info = age_info, progress = 40)
            else:
                flash("Fill out your child's age" )
        elif('ctype' in request.form):
            ctype = request.form['ctype']
            ctype_info = ctype + " is a good choice!"
            ctype_subinfo = ""
            if(ctype ==  'Public College'):
                ctype_subinfo = "Did you know? Public universities collect a large portion of their operating funds from Federal and local State governments. This allows them to make tuition costs more affordable to the average student."
            elif(ctype == 'Private College'):
                ctype_subinfo = "Did you know? Many students who attend private colleges have more opportunities for scholarships because of the strong relationships private institutions have with their alumni."
            elif(ctype == 'Community College'):
                ctype_subinfo = "Did you know? The most obvious reason that students attend community college is for the financial advantage. Many junior colleges cost less than two thousand dollars each semester to attend full time."
            return render_template('questions.html',form = form,ctype_info = ctype_info, progress = 60,ctype_subinfo = ctype_subinfo)
        elif ('state' in request.form):
            state = request.form['state']
            state_info = str(state) + " is a great choice!"
            state_subinfo = ""
            if(state == 'In State'):
                state_subinfo = "Depending on endowments for schools in your state, students may be eligible for more merit-based scholarships and grants by staying in their home state."
            elif(state=="Out of State"):
                state_subinfo = "Going to college out of state is an exciting and new experience. Not only do you experience culture shock, but you also learn to become more independent and have the opportunity to meet new people from a new region of the country."
            return render_template('questions.html',form = form,state_info = state_info, progress = 80,state_subinfo = state_subinfo)

    return render_template('questions.html', form=form, progress = 20)

#@app.route('/questionnare',methods=['GET','POST'])
#def questions():
#    form = QuestionsForm(request.form)
#    if request.method == 'POST':  #this block is only entered when the form is submitted
#        language = request.form.get('age')
#        return '''<h1>The language value is: bal</h1>
#                  <h1>The framework value is: bah</h1>'''
#    return render_template('questions.html',form = form, title='Questions')


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
    return render_template('options.html',title = 'Options')
