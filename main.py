import flask as f

config = {
    "DEBUG": True  # run app in debug mode
}

app = f.Flask(__name__)

# Flask to use the above defined config
app.config.from_mapping(config)

@app.route('/')
def index():
    return f.render_template("index.html")

@app.route('/creer-un-evenement')
def event():
    return f.render_template("soon.html")

@app.route('/réseaux')
def social():
    return f.render_template("social.html")

@app.route('/utilisateur')
@app.route('/utilisateur/<name>')
def affiche_nom(name="Kan-à-ille"):
    return 'Bienvenue à toi, ' + str(name)

@app.route('/somme/<int:num1>/<int:num2>')
def somme(num1, num2):
    return str(num1+num2)

if __name__ == "__main__":
    app.run()