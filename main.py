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

if __name__ == "__main__":
    app.run()