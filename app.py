from flask import Flask, request
import mysql.connector
import os

app = Flask(__name__)

DB_HOST = os.environ.get('DB_HOST', 'mysql')
DB_USER = os.environ.get('DB_USER', 'root')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'password')
DB_NAME = os.environ.get('DB_NAME', 'testdb')

@app.route('/')
def index():
    conn = mysql.connector.connect(
        host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME
    )
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS visits (count INT)")
    cursor.execute("SELECT count(*) FROM visits")
    row = cursor.fetchone()
    if row[0] == 0:
        cursor.execute("INSERT INTO visits (count) VALUES (1)")
    else:
        cursor.execute("UPDATE visits SET count = count + 1")
    conn.commit()
    cursor.execute("SELECT count FROM visits")
    count = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return f'Hello! This page has been visited {count} times.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)