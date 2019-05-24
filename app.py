from flask import Flask, render_template, request, jsonify, make_response
from flask import jsonify
from pyswip import Prolog
from flask_cors import CORS
import json

app = Flask(__name__) #el nombre del modulo
CORS(app)
# cors = CORS(app, resources={r"/foo": {"origins": "http://localhost:port"}})

@app.route("/")
def index():
    return render_template('index.html');
@app.route("/api", methods=['POST'])
def api():
    # instanciamos prolog
    prolog = Prolog();
    # obtenemos la peticion con los datos
    data = request.get_json();
    print(data);
    # consultamos nuestro archivo de prolog
    prolog.consult("engine.pl");
    prolog.assertz("persona(fs)");
    #vemos que conocimientos tiene el usuario y los agregamos
    # a la DB de prolog
    if data['linguistico'] > 0:
        # prolog.query("ling(A).");
        prolog.assertz("persona(linguistico)");
    if data['mate'] > 0:
        # prolog.query("mate(A).");
        prolog.assertz("persona(matematico)");
    if data['espacio'] > 0:
        # prolog.query("esp(A).");
        prolog.assertz("persona(espacio)");
    if data['interpersonal'] > 0:
        # prolog.query("inte(A).");
        prolog.assertz("persona(interpersonal)");
    if data['creativa'] > 0:
        # prolog.query("cre(A).");
        prolog.assertz("persona(creativo)");

    carrera = [];
    # hacemos un query para ver si cumple con alguna carrera
    abogado = list(prolog.query("abogado(A)"));
    arquitecto = list(prolog.query("arquitecto(A)"));
    civil = list(prolog.query("civil(A)"));
    electronico = list(prolog.query("electronico(A)"));
    informatico = list(prolog.query("informatico(A)"));

    if  len(abogado) > 0 and (abogado[0]["A"] == 1):
        carrera.append('abogado');
    if len(arquitecto) > 0 and (arquitecto[0]["A"] == 1):
        carrera.append('arquitecto');
    if len(civil) > 0 and (civil[0]["A"] == 1):
        carrera.append('civil');
    if len(electronico) > 0 and (electronico[0]["A"] == 1):
        carrera.append('electronico');
    if len(informatico) > 0 and (informatico[0]["A"] == 1):
        carrera.append('informatico');

    # prolog.query("retractall(persona(_))");
    # prolog.query("purgar");
    prolog.retractall("persona(_)");
    print(list(prolog.query('getConocimientos(A).')))
    del prolog;
    res = make_response(jsonify({"message": carrera}), 200);
    return res;
