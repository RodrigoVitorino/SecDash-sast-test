import sqlite3
import subprocess
import os

# SQL Injection - padrão que o CodeQL deteta garantidamente
def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = '" + username + "'")
    return cursor.fetchall()

# Command Injection - padrão detetado pelo CodeQL
def list_files(directory):
    result = subprocess.run(
        "ls " + directory,
        shell=True,
        capture_output=True,
        text=True
    )
    return result.stdout

# Code Injection
def evaluate_input(user_input):
    return eval(user_input)

if __name__ == "__main__":
    import sys
    get_user(sys.argv[1])
    list_files(sys.argv[2])
    evaluate_input(sys.argv[3])
