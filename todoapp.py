from flask import *
import os, re

app = Flask(__name__)
todo_list = []


@app.route('/submit')
def submit():
    return render_template('submit.html')

@app.route('/store_task', methods = ['GET', 'POST'])
def store_task():
    global todo_list
    def email_checker(email):
        pattern = re.compile(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[\.]\w{2,3}$')
        return re.match(pattern, email) is not None

    task = request.form['task']
    email = request.form['email']
    priority = request.form['priority']

    if(email_checker(email) == False):
        print('Invalid Email')
        return redirect(url_for('display'))
    else:
        todo_list.append((task,email,priority))
        return redirect(url_for('display'))


@app.route('/display', methods = ['GET'])
def display():
    global todo_list
    return render_template('submit.html', todo_list=todo_list)

@app.route('/clear')
def clear_list():
    global todo_list
    todo_list.clear()
    return redirect(url_for('display'))


if __name__=="__main__":
    app.run(debug=True)

