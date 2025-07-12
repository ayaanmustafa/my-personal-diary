#SETUP YOUR PASSWORD AND THEN YOU CAN REMOVE IT FROM THIS FILE


import sqlite3
import hashlib, random, string

conn = sqlite3.connect("pwd.db")
curr = conn.cursor()

curr.execute('''
CREATE TABLE IF NOT EXISTS pwd(
             password VARCHAR(256) NOT NULL
             )
'''
)

def gen_pwd(len,special_char=True):
    special_chars = "/&*$@#"
    chars = string.ascii_lowercase + string.digits + string.ascii_uppercase
    if special_char:
        chars+= special_chars
    pass_ = "".join(random.choice(chars) for i in range (len))
    return pass_


#Enter your password here
password = "---"
#password = gen_pwd(8,special_char=True)

pwd = hashlib.sha256(password.encode()).hexdigest()

curr.execute("INSERT INTO pwd (password) VALUES (?)", (pwd,))
conn.commit()
conn.close()
