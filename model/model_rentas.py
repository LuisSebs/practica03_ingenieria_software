from alchemyClasses import db
from alchemyClasses.Renta import Renta
from model.model_peliculas import get_movie_by_id
from model.model_peliculas import update_movie_stock
from datetime import date

def get_all_rents():
    r = Renta.query.all()
    for re in r:
        print(type(re.fecha_renta))
    return r

def get_rent_by_id(id):
    return Renta.query.get(id)

def add_rent(id_user, id_movie, rent_day, days_of_rent):

    pelicula = get_movie_by_id(id_movie)
    stock = pelicula.inventario
    if (stock <= 0):
        return False
    update_movie_stock(pelicula.idPelicula, stock=stock-1)

    year = int(rent_day[0:4])
    month = int(rent_day[5:7])
    day = int(rent_day[8::])

    date1 = date(year,month,day)
    date2 = date.today()
    delta = date1 - date2
    days = abs(delta.days)

    nueva_renta = Renta(id_user, id_movie, rent_day)
    nueva_renta.dias_de_renta = days_of_rent
    nueva_renta.estatus = not(days > days_of_rent)
    db.session.add(nueva_renta)
    db.session.commit()
    return True

def update_rent_status(id,status):
    rent = get_rent_by_id(id)
    rent.estatus = status
    db.session.commit()
    return True
