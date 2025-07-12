#SETUP YOUR PASSWORD AND THEN YOU CAN REMOVE IT FROM THIS FILE


import sqlite3
import hashlib

conn = sqlite3.connect("pwd.db")
curr = conn.cursor()

curr.execute('''
CREATE TABLE IF NOT EXISTS pwd(
             password VARCHAR(256) NOT NULL
             )
'''
)


#Enter your password here
password = "ayaan@---"

pwd = hashlib.sha256(password.encode()).hexdigest()

curr.execute("INSERT INTO pwd (password) VALUES (?)", (pwd,))

conn.commit()