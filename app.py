from sqlalchemy import exc
from flask import Flask, request, redirect, abort
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from convert_birth_date import convertBirthDate as cvbd
from numpy import full

LOGGED_IN = (False, "")

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
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    password = db.Column(db.String())
    email = db.Column(db.String(), primary_key=True, unique=True)

    # la méthode __repr__ représente a quoi va ressembler un tuple de la relation
    def __repr__(self):
        return f"Name : {self.first_name}, Age: {self.age}"

db.create_all()

@app.route('/')
def index():
    if LOGGED_IN[0]:
        if len(LOGGED_IN[1]) > 1:
            login = str(LOGGED_IN[1][0]) +" " + str(LOGGED_IN[1][1])
        else:
            login = LOGGED_IN[1]
    else:
        login = "Mon compte"
    return render_template("index.html", login=login)

@app.route('/creer-un-evenement')
def event():
    return render_template("soon.html")

@app.route('/réseaux')
def social():
    return render_template("social.html")

@app.route('/utilisateur')
@app.route('/utilisateur/<name>')
def affiche_nom(name="Kan-à-ille"):
    return 'Bienvenue ' + str(name)

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
    # ceci sera effectuté après que le formulaire ait été validé
    if request.method == 'POST':
        email = request.form.get('email')  # On récupère les valeurs dans le formulaire
        name = request.form.get('name')
        password = request.form.get('password')
        print(request.form.get("age"))
        age = cvbd(request.form.get('age'))  # On convertit notre date de naissance en age
        if " " in name:
            name = name.split()
            # on crée un nouveau profil avec ces valeurs
            new_profile = Profile(first_name=name[0], last_name=name[1], age=age, password=password, email=email)
        else:
            new_profile = Profile(first_name=name, last_name=None, age=age, password=password, email=email)
        try:
            db.session.add(new_profile)  # On les ajoute a la base de données
            db.session.commit()
        except exc.IntegrityError:  # si l'adresse email est déjà dans la base de données on affiche une erreur
            return render_template('already_known.html', email=email)
        print(f"name : {name}")
        return render_template("signedup.html", name=name)
    # au début on affiche la template de base
    return render_template("signup.html")


@app.route('/signin', methods=["GET", "POST"])
def signin():
    global LOGGED_IN
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        data = Profile.query.filter_by(email=email).first()
        if data is None:
            return render_template("unknown_email.html", email=email)
        if data.password == password:
            full_name = [data.first_name, data.last_name]
            LOGGED_IN = (True, full_name)
            return render_template("logged_in.html", name=full_name)
        return render_template("wrong_password.html")
    return render_template('signin.html')


@app.route("/dev")
def dev():
    data = Profile.query.filter_by(email='faust.nino@gmail.com').first()
    return render_template('dev.html', var=data)


# Si l'utilisateur rentre /login, ça le redirigera vers la page signin
@app.route('/login')
def login():
    return redirect('/signin')


@app.route('/account')
def account():
    if LOGGED_IN[0]:
        return render_template('account.html')
    else:
        return render_template('not_logged_in.html')

# On configure une page d'erreur personnalisée 
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run()