from flask import render_template, Flask
app = Flask(__name__)


@app.route('/')
def register():
    return render_template('index.html')
