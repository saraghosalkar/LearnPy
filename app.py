from flask import Flask, flash, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
import random,copy,json


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///quizques.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.secret_key = 'xyz'
app.config['SESSION_TYPE'] = 'filesystem'


class quizQues(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(100),nullable=False)
    question = db.Column(db.String(200), nullable=False)
    option1 = db.Column(db.String(50), nullable=False)
    option2 = db.Column(db.String(50), nullable=False)
    option3 = db.Column(db.String(50), nullable=False)
    option4 = db.Column(db.String(50), nullable=False)

    def __repr__(self) -> str:  
        return f"{self.question},{self.option1},{self.option2},{self.option3},{self.option4}"
def dbToDict(questionsdb):
    original_questions={}
    for i in questionsdb:
     original_questions.update({i.question:[i.option1,i.option2,i.option3,i.option4]})
    print(original_questions)
    return original_questions

def get_title(questions_db):
    for i in questions_db:
        return i.title
    
def shuffle(q):
 """
 This function is for shuffling 
 the dictionary elements.
 """
 selected_keys = []
 i = 0
 while i < len(q):
  a=list(q.keys())
  current_selection = random.choice(a)
  if current_selection not in selected_keys:
   selected_keys.append(current_selection)
   i = i+1
 return selected_keys


@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
     return redirect('quiz.html')
    return render_template("learnpy.html")

@app.route('/quiz/<content>')  
def quiz(content):
    global questionsdb 
    global cont
    global questions_shuffled
    cont=content
    # if request.method=='POST':
    #     if content in request.form:
    print("Hello")
    questionsdb=quizQues.query.filter_by(title=content).all()
    # questionsdb=quizQues.query.filter_by(title=content).all()
    original_questions=dbToDict(questionsdb)
    questions = copy.deepcopy(original_questions)
    questions_shuffled = shuffle(questions)
    for i in questions.keys():
     random.shuffle(questions[i])  
    return render_template("quiz.html",question=questions_shuffled,o=questions)

@app.route('/quiz/evaluation',methods=['GET','POST'])       
def evaluate():
    if (request.method=='POST'):    
            topic = get_title(questionsdb)
             # questionsdb=quizQues.query.filter_by(title=content).all()
            original_questions=dbToDict(questionsdb)
            questions = copy.deepcopy(original_questions)
            # questions_shuffled = shuffle(questions)
            # for i in questions.keys():
            #  random.shuffle(questions[i])
            # if request.form['SubmitQuiz']=='Submit':
            correct = 0 
            count=0
            if(len(request.form)==6):
                print(len(request.form))
                for i in questions.keys():
                    count=count+1
                    answered = request.form[i]
                    if original_questions[i][0] == answered:
                        correct = correct+1  
                return render_template('results.html',correctans=str(correct),title=topic)        
            else:
                return render_template('quiz.html',question=questions_shuffled,o=questions) 
    else:
        return f"The URL /evaluation is accessed directly. Try going to '/quiz' to apply for quiz"             
#   return render_template(cont+".html",questions=questions_shuffled,o=questions)
@app.route('/comments')
def comments():
    return render_template('TableOfContent/comments.html')

@app.route('/Dictionary')
def Dictionary():
     return render_template('TableOfContent/Dictionary.html')

@app.route('/functions')
def functions():
    return render_template('TableOfContent/function.html')

@app.route('/lambda')
def lambda1():
    return render_template('TableOfContent/lambda.html')

@app.route('/lists')
def lists():
    return render_template('TableOfContent/lists.html')

@app.route('/loops')
def loops():
    return render_template('TableOfContent/loops.html')

@app.route('/numbers')
def numbers():
    return render_template('TableOfContent/numbers.html')

@app.route('/set')
def sets():
    return render_template('TableOfContent/set.html')

@app.route('/arrays')
def arrays():
     return render_template('TableOfContent/arrays.html')

@app.route('/tuples')
def tuples():
    return render_template('TableOfContent/tuples.html')

# @app.route('/userinput')
# def userinput():
#     return render_template('TableOfContent/userinput.html')
if __name__=='__main__':
    app.run(debug=False)
