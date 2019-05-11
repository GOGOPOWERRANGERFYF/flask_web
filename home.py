from flask import Flask,render_template

home = Flask(__name__)

@home.route('/')
def homepage():
    return render_template('home.html')

if __name__ == '__main__':
    home.run(debug=True,host='0.0.0.0')

