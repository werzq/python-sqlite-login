from pick import pick
import sqlite3
import os

if os.path.exists("data.db"):
	conn = sqlite3.connect("data.db")
	c = conn.cursor()
else:
    print("database missing...\nmake a file called 'data.db'")

title = "What do you want to do?"
options = ["log in","add account"]
option = pick(options, title, indicator=">>")
accOrLog = str({option})

if accOrLog == "{('add account', 1)}":
	uname = input("Enter account username to add: ")
	pwd = input("Enter account password to add: ")

	c.execute("INSERT INTO accounts VALUES (?, ?)", [uname, pwd])

	conn.commit()
	conn.close()

	print("Account added")

elif accOrLog == "{('log in', 0)}":
	uname = input("Enter username: ")
	pwd = input("Enter password: ")

	c.execute("SELECT * FROM accounts WHERE uname=? and pwd=?", [uname, pwd])
	
	if c.fetchone() == None:
		print("Incorrect credentials")
	else:
		print("Logged in!")
else:
	print("error")