from ast import stmt
from flask import Flask, request
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy

# créer l'application et lier la base de données
app = Flask(__name__)
db = SQLAlchemy(app)


# Configurer l'application
app.config.from_mapping(
    DEBUG = True,  # activer le mode debug
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database/site.db',  # dire ou est la bdd
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Désactiver cette option comme conseillé
    )  

class Profile(db.Model):  # Création de la table Profile avec sql al-chemy
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    password = db.Column(db.String())
    email = db.Column(db.String())

    # la méthode __repr__ représente a quoi va ressembler un tuple de la relation
    def __repr__(self):
        return f"Name : {self.first_name}, Age: {self.age}"




db.create_all()

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
def affiche_nom(name="Sacha le plus beau"):
    return 'merci esclave, ' + str(name)

@app.route('/somme/<int:num1>/<int:num2>')
def somme(num1, num2):
    return str(num1+num2)

@app.route("/db", methods=['POST', 'GET'])
def display_db():
    default_value = "NONE"
    data = request.form.get('fname', default_value)
    return render_template("db.html", data=data)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    # handle the POST request
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        email = request.form.get('email')
        name = name.split()
        print(name, type(name))
        new_profile = Profile(id=None, first_name=name[0], last_name=name[1], age=None, password=password, email=email)
        db.session.add(new_profile)
        db.session.commit()
        return render_template("signedup.html", name=name)
        # otherwise handle the GET request
    return render_template("signup.html")


@app.route('/signin')
def signin():
    return render_template('soon.html')

if __name__ == "__main__":
    app.run()