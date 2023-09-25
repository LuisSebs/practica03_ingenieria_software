from alchemyClasses import db
from alchemyClasses.Pelicula import Pelicula

def get_all_peliculas():
    return Pelicula.query.all()

def get_pelicula_by_id(id):
    return Pelicula.query.filter(Pelicula.idPelicula == id)

def add_movie(name, gender, duration, stock):
    nueva_pelicula = Pelicula(name, gender, duration, stock)
    db.session.add(nueva_pelicula)
    db.session.commit()