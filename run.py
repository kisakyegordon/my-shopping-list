from flask import *
from functools import wraps
from app.user import User

app = Flask(__name__)

app.secret_key = 'kisakyegordon123456789'
users = {'a': 'a', 'a1': 'a1'}
user = User()


@app.route('/index')
def index():
    """ Route to the index page - that displays all shopping lists """
    lists = user.shopping_lists
    return render_template('index.html', lists=lists)


@app.route('/signup', methods=['GET', 'POST'])
def register():
    """ Route to the signup page - that displays the registration page """
    error = None
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        if name and password:
            users[name] = password
            return redirect(url_for('login'))
    return render_template('signup.html', error=error)


@app.route('/add_list', methods=['GET', 'POST'])
def add_list():
    """ Route to the add_list page - that displays a page where lists can be added """
    error = None
    if request.method == 'POST':
        list_name = request.form['list_name']
        items = request.form['items']

        if list_name and items:
            user.create_shopping_list(list_name, items)
            return redirect(url_for('index'))
    return render_template('add_list.html', error=error)


@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    """ Route to the add_item page - that displays a page where items can be added to a list """
    error = None
    if request.method == 'POST':
        list_name = request.form['list_name']
        items = request.form['items']

        if list_name and items:
            user.add_shopping_list_item(list_name, items)
            return redirect(url_for('item', list_name=list_name))
    return render_template('add_list.html', error=error)


def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        """ Login page Session Innitializer """
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash("You need to login first.")
            return redirect(url_for('log'))
    return wrap


@app.route('/logout')
def logout():
    """ Logout kills current running session """
    session.pop('logged_in', None)
    flash('You Were Logged Out !')
    return redirect(url_for('login'))


@app.route('/item/<list_name>')
@login_required
def item(list_name):
    """ Route to the item page - that displays items belonging to a particular shopping list """
    items = user.read_list(list_name)
    return render_template('item.html', items=items, list_name=list_name)


@app.route('/delete/<list_name>/<item_name>')
def delete(list_name, item_name):
    """ Route to the delete functionality - erases content held by the dictionary """
    user.delete_shopping_list_item(list_name, item_name)
    return redirect(url_for('item', list_name=list_name))
    return render_template('item.html')


@app.route('/delete_list/<list_name>')
def delete_list(list_name):
    """ Route to the delete functionality - erases shopping list from a dictionary """
    user.delete_shopping_list(list_name)
    return redirect(url_for('index'))
    return render_template('index.html')

@app.route('/updatelist', methods=['GET', 'POST'])
def updatelist():
    """ Route to the update list page - that enables editing of lists """
    error = None
    if request.method == 'POST':
        list_name = request.form['list_name']
        new_name = request.form['new_name']
        flash("You have succesfully added registered {} {}".format(list_name, new_name))

        if list_name and new_name:
            user.update_shopping_list(list_name, new_name)
            return redirect(url_for('index'))
    return render_template('updatelist.html')


@app.route('/updatelistitem', methods=['GET', 'POST'])
def updatelistitem():
    """ Route to the update list item page - that enables editing of list items """
    error = None
    if request.method == 'POST':
        list_name = request.form['list_name']
        item_name = request.form['item_name']
        new_name = request.form['new_item_name']
        flash("You have succesfully added registered {} {} {}".format(list_name, item_name, new_name))

        if list_name and item_name:
            user.update_shopping_list_item(list_name, item_name, new_name)
            return redirect(url_for('item', list_name=list_name))
    return render_template('updatelistitem.html', error=error)

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    """ Route to the login / default page """
    error = None
    if request.method == 'POST':
        if request.form['email'] not in users.keys() or request.form['password'] not in users.values():
            error = 'Invalid Credentials'
        else:
            session['logged_in'] = True
            return redirect(url_for('index'))
    return render_template('login.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)
