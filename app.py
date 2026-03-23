# vulnerabilidades intencionais para teste
import sqlite3
import os
import subprocess

# SQL Injection
def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchall()

# Path Traversal
def read_file(path):
    with open(path, "r") as f:
        return f.read()

# Command Injection
def ping_host(host):
    os.system("ping -c 1 " + host)

# Hard-coded credentials
DB_PASSWORD = "supersecret123"
API_KEY = "ghp_fakekey1234567890abcdef"

if __name__ == "__main__":
    print(get_user("admin"))
    print(read_file("/etc/passwd"))
    ping_host("localhost")
