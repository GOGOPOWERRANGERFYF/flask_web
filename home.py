from flask import Flask,render_template,request
from flask_bootstrap import Bootstrap

home = Flask(__name__)
bootstrap = Bootstrap(home)

@home.route('/',methods=['GET','POST'])
def homepage():
    return render_template('cssselector.html')

@home.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        passwd = request.form['password']
        #return '%s %s' % (name,passwd)
        return render_template('login.html',name=name,passwd=passwd)
    return render_template('login.html')

@home.route('/articles')
def articles():
    return render_template('article.html')

if __name__ == '__main__':
    home.run(debug=True,host='0.0.0.0')

