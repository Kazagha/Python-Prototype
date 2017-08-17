from flask import Flask, render_template, request
from collections import defaultdict

# persistence
#
# could go with serialization
# import shelve
# or:
# import pickle
#
# could go with stdlib DB
# import sqlite3
# 
# could go with ORM
# $ pip install flask_sqlalchemy
# add:
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("template.html", data=get_lib(), col1='Select activity', col2='',
                           activities=get_activities())

@app.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')

@app.route('/sign_in')
def sign_in():
    return render_template("sign_up.html")

@app.route('/submit', methods=['POST'])
def submit():
    if request.method=='GET':
        print('GET-Method')
        return render_template("sign_up.html")
    else:
        print('Posting')
        print(f"Get Name: {request.form.get('name')}")
    #print(f'Submitting data')

    #_name = request.form['inputName']
    return render_template("sign_up.html")

def get_lib():
    """Return a basic library
    
    In the HTML template use the following syntax
    {% for k, v in data.items() %}
    """

    return {'Chris':1234, 'Nick':5678}

def get_activities():
     return ['Buying','Carousing','Crafting','Crime','Gambling','Relaxation']

def get_selected():
    pass

def get_history():
    pass

if __name__ == '__main__':
    for item in get_activities():
        print(item)
    app.run(debug=True)
