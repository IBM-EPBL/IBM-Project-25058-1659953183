from flask import render_template, Flask
app = Flask(__name__)


@app.route('/')
@app.route('/register')
def register():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')
