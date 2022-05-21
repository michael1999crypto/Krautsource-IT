import json
import random
import sqlite3

query_check_user = "SELECT * FROM users WHERE userid = ?"
query_insert = "INSERT INTO users (userid) VALUES (?)"

data_path = './data/main.db'

def get_new_question():
    con = sqlite3.connect(data_path)
    cur = con.cursor()
    cur.execute("SELECT * FROM questions WHERE answered = 0")
    res = cur.fetchone()    
    if(res):
        cur.execute("UPDATE questions SET answered = 1 WHERE id = ?", (res[0],))
        con.commit()
    return res

def add_user(user_id):
    con = sqlite3.connect(data_path)
    cur = con.cursor()
    cur.execute(query_insert, (int(user_id),))
    con.commit()

def check_user(user_id):
    con = sqlite3.connect(data_path)
    cur = con.cursor()
    cur.execute(query_check_user, (int(user_id),))
    if cur.fetchone() is None:
        add_user(user_id)        

def add_points_user(userid, points):
    con = sqlite3.connect(data_path)
    cur = con.cursor()
    cur.execute("UPDATE users SET points = points + ? WHERE userid = ?", (points, userid))    
    con.commit()
    cur.execute("SELECT points FROM users WHERE userid = ?", (userid,))
    res = cur.fetchone()
    return res 

def get_all_users():
    con = sqlite3.connect(data_path)
    cur = con.cursor()
    cur.execute("SELECT * FROM users")
    """return [(171141279,), (777722458,)]"""
    return cur.fetchall()

def get_ranking():
    con = sqlite3.connect(data_path)
    cur = con.cursor()
    cur.execute("SELECT * FROM users ORDER BY points DESC")    
    res = cur.fetchall()
    print(res)
    return res