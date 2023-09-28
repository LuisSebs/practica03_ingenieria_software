from alchemyClasses import db
from alchemyClasses.Usuario import Usuario
from hashlib import sha256
from CryptoUtils.CryptoUtils import cipher

def get_all_users():
    return Usuario.query.all()

def get_user_by_id(id):
    return Usuario.query.get(id)

def add_user(name, email, password, photo=None):

    # Verificamos que el correo no exista
    exists_email = Usuario.query.filter(Usuario.email == email).all();

    if exists_email:
        return False;
    
    # Contraseña encriptada
    password = sha256(cipher(password)).hexdigest()
    nuevo_usuario = Usuario(name, email, password)
    db.session.add(nuevo_usuario)
    db.session.commit()

    return True

def update_user_name(id, new_name):
    usuario = get_user_by_id(id)
    usuario.nombre = new_name
    db.session.commit()
    return True

def update_user_email(id, new_email):
    usuario = get_user_by_id(id)
    usuario.email = new_email
    db.session.commit()
    return True

def delete_user(id):
    usuario = get_user_by_id(id)
    db.session.delete(usuario)
    db.session.commit()
    return True
