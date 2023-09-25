from random import randint
from flask import Blueprint, request, render_template, redirect, url_for, flash
from model.model_usuario import get_all_users
from model.model_usuario import get_user_by_id
from model.model_usuario import update_user_name
from model.model_usuario import update_user_email
from model.model_usuario import update_user_passwrd
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

@user.route('/actualizar')
def actualizar_usuario():
    id_usuario = request.args.get('id')
    if id_usuario:
        usuario = get_user_by_id(int(id_usuario));
        # Si no existe el usuario
        if not usuario:
            # Enviamos mensaje de usuario no encontrado
            flash('Usuario no encontrado')
        return  render_template('user-update.html', usuario = usuario)
    else:
        return render_template('user-update.html')

@user.route('/nombre', methods = ('GET', 'POST'))
def actualizar_nombre():
    if request.method == 'POST':
        id_user  = request.args.get('id')
        nuevo_nombre = request.form['nombre'];
        status = update_user_name(id_user,nuevo_nombre)
        return f"id = {id_user} \n nuevo_nombre = {nuevo_nombre}"
    else:
        return render_template('user-update-name.html')

@user.route('/correo', methods = ('GET', 'POST'))
def actualizar_correo():
    if request.method == 'POST':
        id_user  = request.args.get('id')
        nuevo_correo = request.form['correo'];
        status = update_user_email(id_user,nuevo_correo)
        return f"id = {id_user} \n nuevo_email = {nuevo_correo}"
    else:
        return render_template('user-update-email.html')

@user.route('/contraseña', methods = ('GET', 'POST'))
def actualizar_contrasenia():
    if request.method == 'POST':
        id_user  = request.args.get('id')
        nuevo_password = request.form['password'];
        status = update_user_passwrd(id_user,nuevo_password)
        return f"id = {id_user} \n nuevo_password = {nuevo_password}"
    else:
        return render_template('user-update-password.html')

@user.route('/eliminar', methods = ('GET', 'POST'))
def eliminar_usuario():
    if request.method == 'POST':
        id_user = request.form['id']
        status = delete_user(id_user)
        return 'Deleted '
    else:
        return render_template('user-delete.html')

@user.route('/error-message')
def example_flash():
    mensaje = 'Hola soy un mensaje'
    r = randint(0,2)
    if r == 0:
        flash(mensaje)
    return render_template('error.html')


