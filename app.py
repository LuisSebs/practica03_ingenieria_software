from flask import Flask, render_template, url_for, redirect
from alchemyClasses import db
from controllers.UserController import user
from controllers.MovieController import movie
from controllers.RentController import rent

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://ferfong:Developer123!@localhost:3306/ing_soft"
app.config.from_mapping(
    SECRET_KEY='dev'
)

app.register_blueprint(user) #esto agrega a un controlador a la aplicacion.
app.register_blueprint(movie)
app.register_blueprint(rent)
db.init_app(app)

@app.route('/') #localhost:5000/ endpoints
def main():  # put application's code here
    return render_template('index.html')

@app.route('/another-route')
def another_world():
    return render_template('another-index.html')

@app.route('/redirect')
def not_here():
    return redirect(url_for('another_world'))

if __name__ == '__main__':
    app.run()
