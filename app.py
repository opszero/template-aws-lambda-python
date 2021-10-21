from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def cats():
    return render_template('index.html')

@app.route("/dogs/<id>")
def dog(id):
    return "Dog"

@app.route("/health")
def health():
    return { "status": "Success" }