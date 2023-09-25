from flask import Blueprint, request, render_template, redirect, url_for, flash

movie = Blueprint('movie', __name__, url_prefix='/movie')

@movie.route('/')
def main_view_movie_controller():
    return render_template('pelicula.html')