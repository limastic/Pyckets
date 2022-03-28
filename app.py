from flask import Flask, request, redirect
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy

config = {
    "DEBUG": True,  # activer le mode debug
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///database/site.db'
}

app = Flask(__name__)
db = SQLAlchemy(app)

class Profile(db.Model):  # Création de la table Profile avec sql al-chemy
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), unique=False, nullable=False)
    last_name = db.Column(db.String(20), unique=False, nullable=False)
    age = db.Column(db.Integer, nullable=False)

    # la méthode __repr__ représente a quoi va ressembler un tuple de la relation
    def __repr__(self):
        return f"Name : {self.first_name}, Age: {self.age}"

# Dire a Flask d'utiliser la configuration définie plus tot 
app.config.from_mapping(config)


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

@app.route("/db", methods=['POST'])
def display_db():
    default_value = "NONE"
    data = request.form.get('fname', default_value)
    return render_template("db.html", data=data)
    
if __name__ == "__main__":
    app.run()