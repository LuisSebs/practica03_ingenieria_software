from flask import Blueprint, request, render_template, redirect, url_for, flash

rent = Blueprint('rent', __name__, url_prefix='/rent')

@rent.route('/')
def main_view_rent_controller():
    return render_template('renta.html')