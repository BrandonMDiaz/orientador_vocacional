from flask import Flask, render_template
from pyswip import Prolog
app = Flask(__name__) #el nombre del modulo

@app.route("/")
@app.route("/home")

def home():
    return render_template('index.html');
