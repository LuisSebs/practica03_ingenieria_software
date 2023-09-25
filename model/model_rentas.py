from alchemyClasses import db
from alchemyClasses.Renta import Renta

def get_all_rents():
    return Renta.query.all()

def get_rent_by_id(id):
    return Renta.query.get(id)

def add_rent(id_user, id_movie, rent_day, days_of_rent, status):
    nueva_renta = Renta(id_user, id_movie, rent_day)
    nueva_renta.dias_de_renta = days_of_rent
    nueva_renta.estatus = status
    db.session.add(nueva_renta)
    db.session.commit()
    return True

def update_rent_status(id,status):
    rent = get_rent_by_id(id)
    rent.estatus = status
    db.session.commit()
    return True