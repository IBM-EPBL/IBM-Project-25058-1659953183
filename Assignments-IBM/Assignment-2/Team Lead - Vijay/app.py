import numbers
from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)


@app.route('/')
def home():
    return (render_template('index.html'))

@app.route('/success/<name>/<email>/<number>')
def success(name, email, number):
    return (render_template('Welcome.html', name=name, email=email, number=number))

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        user = request.form['username']
        mail = request.form['email']
        number = request.form['mobile']
        return (redirect(url_for('success', name=user, email=mail, number=number)))
    else:
        user = request.args.get('username')
        mail = request.args.get('email')
        number = request.args.get('mobile')
        return (redirect(url_for('success', name=user, email=mail, number=number)))


if __name__ == '__main__':
    app.run(debug=True)
