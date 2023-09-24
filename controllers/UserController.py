from random import randint

from flask import Blueprint, request, render_template, redirect, url_for, flash

from model.model_usuario import get_all_users

user = Blueprint('user', __name__, url_prefix='/user')

@user.route('/')
def main_view():
    s = ''
    for usuario in get_all_users():
        s += str(usuario)
    return s

@user.route('/registrar', methods=('GET', 'POST'))
def registrar():
    if request.method == 'POST':
        nombre = request.form['nombre']
        passwd = request.form['passwd']
        correo = request.form['correo']
        return f'{nombre}\n{correo}\n{passwd}'
    return render_template('user-registration.html')

@user.route('/error-message')
def example_flash():
    mensaje = 'Hola soy un mensaje'
    r = randint(0,2)
    if r == 0:
        flash(mensaje)
    return render_template('error.html')