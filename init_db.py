import sqlite3
from flask import Flask

app = Flask(__name__)

DATABASE = 'mydb.db'

def init_db():
    db=sqlite3.connect(DATABASE)

    with app.open_resource('db.sql', mode='r') as f:
        sql =f.read()

    print(sql)
    db.cursor().execute(sql)
    db.commit()
    db.close()

if __name__=='__main__':
    init_db()
