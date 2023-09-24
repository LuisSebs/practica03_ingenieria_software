from flask import Flask, render_template, url_for, redirect
from alchemyClasses import db
from controller import bp
from controllers.UserController import user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://ferfong:Developer123!@localhost:3306/ing_soft"
app.config.from_mapping(
    SECRET_KEY='dev'
)
app.register_blueprint(bp) #esto agrega a un controlador a la aplicacion.
app.register_blueprint(user)
db.init_app(app)

@app.route('/') #localhost:5000/ endpoints
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/another-route')
def another_world():
    return render_template('another-index.html')

@app.route('/redirect')
def not_here():
    return redirect(url_for('another_world'))

if __name__ == '__main__':
    app.run()
