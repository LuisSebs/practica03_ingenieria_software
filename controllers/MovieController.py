from flask import Blueprint, request, render_template, redirect, url_for, flash
from model.model_peliculas import add_movie
from model.model_peliculas import get_all_movies
from model.model_peliculas import get_movie_by_id
from model.model_peliculas import update_movie_name
from model.model_peliculas import update_movie_gender
from model.model_peliculas import update_movie_duration
from model.model_peliculas import update_movie_stock
from model.model_peliculas import delete_movie

movie = Blueprint('movie', __name__, url_prefix='/movie')

@movie.route('/')
def main_view_movie_controller():
    return render_template('pelicula.html', peliculas = get_all_movies())

@movie.route('/registrar', methods=('GET', 'POST'))
def registrar_pelicula():
    if request.method == 'POST':
        nombre = request.form['nombre']
        genero = request.form['genero']
        duracion = request.form['duracion']
        inventario = request.form['inventario']
        status = add_movie(nombre,genero,duracion,inventario)
    return redirect(url_for('movie.main_view_movie_controller'))

@movie.route('/actualizar/<string:id>', methods=('GET', 'POST'))
def actualizar_pelicula(id):
    if request.method == 'POST':
        id_movie = request.form['id'];
        nombre = request.form['nombre']
        genero = request.form['genero']
        duracion = request.form['duracion']
        inventario = request.form['inventario']
        status1 = update_movie_name(id_movie, nombre)
        status2 = update_movie_gender(id_movie, genero)
        status3 = update_movie_duration(id_movie, duracion)
        status4 = update_movie_stock(id_movie, inventario)
        return redirect(url_for('movie.main_view_movie_controller'))
    else:
        pelicula = get_movie_by_id(int(id))
        return render_template('pelicula.html', peliculas = get_all_movies(), pelicula=pelicula)

@movie.route('/eliminar/<string:id>', methods = ('GET', 'POST'))
def eliminar_pelicula(id):
    status = delete_movie(id)
    return redirect(url_for('movie.main_view_movie_controller'))
