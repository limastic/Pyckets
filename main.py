import flask as f

config = {
    "DEBUG": True  # run app in debug mode
}

app = f.Flask(__name__)

# Flask to use the above defined config
app.config.from_mapping(config)

@app.route('/')
def index():
    return f.render_template("Pyckets/Frontend/index.html")

if __name__ == "__main__":
    app.run()