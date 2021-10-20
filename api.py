from flask import Flask
app = Flask(__name__)


@app.route("/cats")
def cats():
    return "Cats"

@app.route("/dogs/<id>")
def dog(id):
    return "Dog"

@app.route("/health")
def health():
    return { "status": "Success" }