from alchemyClasses import db
from alchemyClasses.Pelicula import Pelicula

def get_all_movies():
    return Pelicula.query.all()

def get_movie_by_id(id):
    return Pelicula.query.get(id)

def add_movie(name, gender, duration, stock):
    nueva_pelicula = Pelicula(name, gender, duration, stock)
    db.session.add(nueva_pelicula)
    db.session.commit()

def update_movie_name(id, name):
    movie = get_movie_by_id(id)
    movie.nombre = name
    db.session.commit()

def update_movie_gender(id,gender):
    movie = get_movie_by_id(id)
    movie.genero = gender
    db.session.commit()

def update_movie_duration(id,duration):
    movie = get_movie_by_id(id)
    movie.duracion = duration
    db.session.commit()

def update_movie_stock(id,stock):
    movie = get_movie_by_id(id)
    movie.inventario = stock
    db.session.commit()

def delete_movie(id):
    pelicula = get_movie_by_id(id)
    db.session.delete(pelicula)
    db.session.commit()
    return True
