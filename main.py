#!/usr/bin/env python3
from flask import Flask, render_template, request, url_for


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html', title='Домашняя страница')
    
@app.route('/login')
def login():
    return render_template('login.html', title='Авторизация')
    

if __name__ == '__main__':
    app.run(debug=True)
