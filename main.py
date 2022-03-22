import flask as f
from flask_sqlalchemy import SQLAlchemy
from Hamstergram import hamstergram_api as hs
from flask_migrate import Migrate, migrate

config = {
    "DEBUG": True,  # run app in debug mode
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///hamstergram.db'
}

app = f.Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Flask to use the above defined config
app.config.from_mapping(config)


db.create_all()

@app.route('/')
def index():
    return f.render_template("index.html")

@app.route('/creer-un-evenement')
def event():
    return f.render_template("soon.html")

@app.route('/réseaux')
def social():
    return f.render_template("social.html")

@app.route('/db')
def db():
    return f.render_template('db.html')

if __name__ == "__main__":
    app.run()