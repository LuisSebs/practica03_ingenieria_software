from alchemyClasses.Pelicula import Pelicula

def get_all_peliculas():
    return Pelicula.query.all()

def get_pelicula_by_id(id):
    return Pelicula.query.filter(Pelicula.idPelicula == id)