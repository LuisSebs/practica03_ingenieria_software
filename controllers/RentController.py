from flask import Blueprint, request, render_template, redirect, url_for, flash
from model.model_rentas import get_all_rents
from model.model_rentas import get_rent_by_id
from model.model_rentas import add_rent
from model.model_rentas import update_rent_status
rent = Blueprint('rent', __name__, url_prefix='/rent')

@rent.route('/')
def main_view_rent_controller():
    return render_template('renta.html', rentas = get_all_rents())

@rent.route('/registrar', methods=('GET', 'POST'))
def registrar_renta():
    if request.method == 'POST':
        id_usuario = request.form['id_usuario']
        id_pelicula = request.form['id_pelicula']
        fecha_renta = request.form['fecha_renta']
        dias_de_renta = request.form['dias_de_renta']
        estatus = request.form['estatus']
        print(f"id_usuario: {id_usuario}\n id_pelicula: {id_pelicula}\n fecha_renta: {type(fecha_renta)}\n dias_renta: {dias_de_renta}\n estatus: {estatus}")
        status = add_rent(id_usuario,id_pelicula,fecha_renta,int(dias_de_renta),int(estatus))
    return redirect(url_for('rent.main_view_rent_controller'))

@rent.route('/actualizar/<string:id>', methods=('GET', 'POST'))
def actualizar_renta(id):
    if request.method == 'POST':
        id_renta = request.form['id'];
        estatus = request.form['estatus']
        status = update_rent_status(id_renta, int(estatus))
        return redirect(url_for('rent.main_view_rent_controller'))
    else:
        renta = get_rent_by_id(int(id))
        return render_template('renta.html', rentas = get_all_rents(), renta=renta)
