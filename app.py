from flask import Flask, request
import sqlite3
import subprocess

app = Flask(__name__)

# SQL Injection
@app.route('/user')
def get_user():
    username = request.args.get('username')
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = '" + username + "'")
    return str(cursor.fetchall())

# Command Injection
@app.route('/ping')
def ping():
    host = request.args.get('host')
    result = subprocess.run("ping -c 1 " + host, shell=True, capture_output=True, text=True)
    return result.stdout

# Code Injection
@app.route('/eval')
def run_eval():
    code = request.args.get('code')
    return str(eval(code))
