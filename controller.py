from flask import Blueprint, render_template

bp = Blueprint('bp1', __name__, url_prefix='/bp') #localhost:5000/bp/adssfgdjhgf

@bp.route('/')
def hello_controller():
    return render_template('new-controller.html')

@bp.route('/ejemplo')
def ej():
    return 'hola'