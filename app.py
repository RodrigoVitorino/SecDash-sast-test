import sys
import sqlite3
import subprocess

# SQL Injection
conn = sqlite3.connect("users.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM users WHERE username = '" + sys.argv[1] + "'")

# Command Injection
subprocess.run("ls " + sys.argv[2], shell=True)

# Code Injection
eval(sys.argv[3])
