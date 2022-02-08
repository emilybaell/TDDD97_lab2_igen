import sqlite3
from flask import g

DaDATABASE='database.db'

def connect_db():
    return sqlite3.connect(DaDATABASE)

def get_db():
    db=getattr(g, 'db', None)
    if db is None:
        db = g.db=connect_db()
    return db

def disconnect_db():
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
        g.db = None

def create_profile(email, password, firstname, familyname, gender, city, country):
    try:
        get_db().execute("insert into profile values(?, ?, ?, ?, ?, ?, ?)", [email, password, firstname, familyname, gender, city, country])
        get_db().commit()
        return True
    except Exception as e:
        print(e)
        return False

def find_user(email):
    cursor = get_db().execute("select * from profile where email like ?", [email])
    rows = cursor.fetchall()
    cursor.close()
    return rows