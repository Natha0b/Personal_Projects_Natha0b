#!/usr/bin/python3
"""
script that starts a Flask web application.
"""
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('mydatabase.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS contactos
             (name TEXT, email TEXT, city TEXT)''')


@app.route("/", strict_slashes=False)
def web():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    city = request.form['city']

    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    c.execute("INSERT INTO contactos VALUES (?, ?, ?)", (name, email, city))
    conn.commit()
    conn.close()

    return render_template('submit.html', name=name, email=email, city=city)


if __name__ == '__main__':
    conn.commit()
    app.run(host='0.0.0.0', port=5000)
