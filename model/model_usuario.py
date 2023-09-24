from alchemyClasses.Usuario import Usuario

def get_all_users():
    return Usuario.query.all()

def get_user_by_id(id):
    return Usuario.query.filter(Usuario.idUsuario == id) 