from random import randint
from flask import Blueprint, request, render_template, redirect, url_for, flash
from model.model_usuario import get_all_users
from model.model_usuario import get_user_by_id
from model.model_usuario import update_user_name
from model.model_usuario import update_user_email
from model.model_usuario import delete_user
from model.model_usuario import add_user

user = Blueprint('user', __name__, url_prefix='/user')

@user.route('/')
def main_view_user_controller():
    return render_template('usuario.html', usuarios = get_all_users())

@user.route('/registrar', methods=('GET', 'POST'))
def registrar_usuario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        password = request.form['passwd']
        correo = request.form['correo']
        status = add_user(nombre, correo, password)
        # Si hubo un error al agregar al usuario
        if not status:
            flash('El correo que quieres registrar ya existe', 'error')

    return redirect(url_for('user.main_view_user_controller'))

@user.route('/actualizar/<string:id>', methods=('GET', 'POST'))
def actualizar_usuario(id):
    if request.method == 'POST':
        id_user = request.form['id'];
        nombre = request.form['nombre']
        correo = request.form['correo']
        status1 = update_user_name(id_user, nombre)
        status2 = update_user_email(id_user, correo)
        return redirect(url_for('user.main_view_user_controller'))
    else:
        usuario = get_user_by_id(int(id))
        return render_template('usuario.html', usuarios = get_all_users(), usuario=usuario)
    
@user.route('/eliminar/<string:id>', methods = ('GET', 'POST'))
def eliminar_usuario(id):
    status = delete_user(id)
    return redirect(url_for('user.main_view_user_controller'))
