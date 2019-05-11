from flask import Flask,render_template,request

home = Flask(__name__)

@home.route('/')
def homepage():
    return render_template('home.html')

@home.route('/login',methods=['GET','POST'])
def login():
    return render_template('login.html')

@home.route('/articles')
def articles():
    return render_template('article.html')

if __name__ == '__main__':
    home.run(debug=True,host='0.0.0.0')

