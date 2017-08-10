from flask import Flask, render_template

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
    return render_template("template.html", data={'Chris':1234, 'Nick':5678}, col1='Name', col2='Phone Numbers' )


if __name__ == '__main__':
    for i in range(1,10):
        print (i)
    app.run(debug=True)
