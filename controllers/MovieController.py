from flask import Blueprint, request, render_template, redirect, url_for, flash
from model.model_peliculas import add_movie
movie = Blueprint('movie', __name__, url_prefix='/movie')

@movie.route('/')
def main_view_movie_controller():
    return render_template('pelicula.html')

@movie.route('/registrar', methods=('GET', 'POST'))
def registrar_pelicula():
    if request.method == 'POST':
        nombre = request.form['nombre']
        genero = request.form['genero']
        duracion = request.form['duracion']
        inventario = request.form['inventario']
        status = add_movie(nombre,genero,duracion,inventario)
        if status:
            return 'OK'
        else:
            return 'ERROR'
    return render_template('user-registration.html')