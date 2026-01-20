#!/usr/bin/env python3
from flask import Flask, render_template, request, url_for


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
