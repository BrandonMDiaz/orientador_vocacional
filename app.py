from flask import Flask, render_template, request, jsonify, make_response
from flask import jsonify
from pyswip import Prolog
import json
app = Flask(__name__) #el nombre del modulo

# instansia de Prolog
@app.route("/")
def index():
    return render_template('index.html');
@app.route("/api", methods=['POST'])
def api():
    prolog = Prolog();
    data = request.get_json();
    prolog.consult("engine.pl");
    if data['linguistico'] > 0:
        prolog.assertz("persona(linguistico)");
    if data['mate'] > 0:
        prolog.assertz("persona(matematico)");
    if data['espacio'] > 0:
        prolog.assertz("persona(espacio)");
    if data['interpersonal'] > 0:
        prolog.assertz("persona(interpersonal)");
    if data['creativa'] > 0:
        prolog.assertz("persona(creativo)");

    carrera = [];

    abogado = list(prolog.query("abogado(A)"));
    arquitecto = list(prolog.query("arquitecto(A)"));
    civil = list(prolog.query("civil(A)"));
    electronico = list(prolog.query("electronico(A)"));
    informatico = list(prolog.query("informatico(A)"));

    if(abogado[0]["A"] == 1):
        carrera.append('abogado');
    if(arquitecto[0]["A"] == 1):
        carrera.append('arquitecto');
    if(civil[0]["A"] == 1):
        carrera.append('civil');
    if(electronico[0]["A"] == 1):
        carrera.append('electronico');
    if(informatico[0]["A"] == 1):
        carrera.append('informatico');

    # print(list(prolog.query('getConocimientos(A).')))
    res = make_response(jsonify({"message": carrera}), 200);
    return res;
