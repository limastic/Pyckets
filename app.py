from flask import Flask, request, redirect
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate, migrate

config = {
    "DEBUG": True,  # run app in debug mode
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///site.db'
}

app = Flask(__name__)
db = SQLAlchemy(app)
# migrate = Migrate(app, db)


# Flask to use the above defined config
app.config.from_mapping(config)


# db.create_all()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/creer-un-evenement')
def event():
    return render_template("soon.html")

@app.route('/réseaux')
def social():
    return render_template("social.html")

@app.route('/utilisateur')
@app.route('/utilisateur/<name>')
def affiche_nom(name="Kan-à-ille"):
    return 'Bienvenue à toi, ' + str(name)

@app.route('/somme/<int:num1>/<int:num2>')
def somme(num1, num2):
    return str(num1+num2)


@app.route('/db')
def db(var_test = 12345):
    return render_template('db.html')

if __name__ == "__main__":
    app.run()