import logging
import mysql.connector
from flask import Flask, render_template, request, Response, jsonify
from flask_cors import CORS
import json


def nimi_tauluun(nimi):
    yhteys = mysql.connector.connect(
        database='flight_game',
        user='python',
        password='1232',
        autocommit=True)

    sql = f'INSERT INTO peli (nimi) VALUES ("{nimi}")'
    kursori = yhteys.cursor()
    kursori.execute(sql)

    kursori.close()
    yhteys.close()
    return
app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.logger.setLevel(logging.INFO)


@app.route('/')

def nimihaku():
    return render_template('Game_start_page2.html')

@app.route("/pelaaja", methods=["POST"])
def nimimerkki():
    nimi = request.form["nimi"]
    nimi_tauluun(nimi)
    return



if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)