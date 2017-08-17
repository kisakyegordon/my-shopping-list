from flask import *
from functools import wraps

app = Flask(__name__)

app.secret_key = 'elgordo123456789'

users = {'admin':'admin','art':'art'}
new_users = {}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        username = request.form['rname']
        password = request.form['pword']
        flash("You have succesfully registered {} {}".format(username, password))


        if username and password:
            new_users[username] = password
            return redirect(url_for('log'))
    return render_template('register.html', error=error)

def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash("You need to login first.")
            return redirect(url_for('log'))
    return wrap

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You Were Logged Out !')
    return redirect (url_for('log'))

@app.route('/hello')
@login_required
def hello():
    return render_template('hello.html')


@app.route('/log', methods=['GET', 'POST'])
def log():
    users = {'admin': 'admin', 'art': 'art'}
    error = None
    if request.method == 'POST':
        if request.form['username'] not in users.keys() or request.form['password'] not in users.values():
            error = 'Invalid Credentials'
        else:
            session['logged_in'] = True
            return redirect(url_for('hello'))
    return render_template('log.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)



