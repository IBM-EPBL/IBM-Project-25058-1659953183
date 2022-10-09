from flask import Flask,render_template,request,url_for,redirect
app = Flask(__name__)

@app.route('/success/<un>/<mail>')
def success(un,mail):
    return (render_template('Welcome.html', name = un, email = mail))

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == "POST":
        user = request.form['username']
        mail = request.form['email']
        return (redirect(url_for('success', un = user,mail = mail)))
    else:
        user = request.args.get('username')
        mail = request.args.get('email')
        return (redirect(url_for('success', un = user,mail = mail)))


if __name__ == '__main__':
    app.run(debug = True)