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
    return render_template('usuario.html')

@user.route('/registrar', methods=('GET', 'POST'))
def registrar_usuario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        password = request.form['passwd']
        correo = request.form['correo']
        status = add_user(nombre, correo, password)
        if status:
            return 'OK'
        else:
            return 'ERROR'
    return render_template('user-registration.html')

@user.route('/leer')
def leer_usuario():
    usuarios = get_all_users()
    tabla = "<table>\n"
    for usuario in usuarios:
        tabla += "<tr>\n"
        tabla += "<td>{}</td><td>{}</td><td>{}</td>\n".format(usuario.idUsuario, usuario.nombre, usuario.email)
        tabla += "</tr>\n"
    tabla += "</table>"
    return tabla

@user.route('/actualizar', methods=('GET', 'POST'))
def actualizar_usuario():
    if request.method == 'POST':
        id_user = request.form['id']
        nuevo_nombre = request.form['nombre']
        nuevo_email = request.form['correo']
        update_user_name(id_user,nuevo_nombre)
        update_user_email(id_user, nuevo_email)
        return f"id={id_user}<br/>nuevo_nombre={nuevo_nombre}<br/> {nuevo_email}"
    else:
        id_usuario = request.args.get('id')
        if id_usuario:
            usuario = get_user_by_id(int(id_usuario))
            # Si no existe el usuario
            if not usuario:
                # Enviamos mensaje de usuario no encontrado
                flash('Usuario no encontrado')
            return  render_template('user-update.html', usuario = usuario)
        else:
            return render_template('user-update.html')

@user.route('/eliminar', methods = ('GET', 'POST'))
def eliminar_usuario():
    if request.method == 'POST':
        id_user = request.form['id']
        status = delete_user(id_user)
        return 'Deleted'
    else:
        return render_template('user-delete.html')

@user.route('/error-message')
def example_flash():
    mensaje = 'Hola soy un mensaje'
    r = randint(0,2)
    if r == 0:
        flash(mensaje)
    return render_template('error.html')


