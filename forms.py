#!/usr/bin/env python3
#
# Форма авторизации

from wtforms import SubmitField, StringField, PasswordField, validators
from flask_wtf import FlaskForm
"""
import re
from wtforms.validators import DataRequired, ValidationError
def validate_complex_password(form, field):
    '''Валидатор, который проверяет на наличие символов, цифр и разного регистра.'''
    if not re.search(r'[A-Za-z]', field.data):
        raise ValidationError('Должен содержать хотя бы одну букву.')
    if not re.search(r'\d', field.data):
        raise ValidationError('Должен содержать хотя бы одну цифру.')
    if field.data.islower() or field.data.isupper():
        raise ValidationError('Должен содержать буквы как верхнего, так и нижнего регистра.')
"""


class LoginForm(FlaskForm):
    username = StringField('Логин', [validators.Length(min=6, max=25)])
    password = PasswordField('Пароль', [
        validators.DataRequired(),
        validators.Length(min=6, max=25)]
        # validators.EqualTo('confirm', message='Passwords must match')
    )
    submit = SubmitField('Войти')
