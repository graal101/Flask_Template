#!/usr/bin/env python3
from flask import Flask, render_template, request, url_for
from forms import LoginForm



app = Flask(__name__)
app.config.update(
    SECRET_KEY='Замени_потом'
)

@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html', title='Домашняя страница')


@app.route('/login', methods=['GET', 'POST'])
def login():
    
    form = LoginForm()
    
    return render_template('login.html', title='Авторизация', form=form)


@app.errorhandler(404)
def pageNotFound(error):
    return render_template('404.html', title='404 - Страница не найдена')


if __name__ == '__main__':
    app.run(debug=True)
