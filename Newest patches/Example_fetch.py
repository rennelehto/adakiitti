import logging

import mysql.connector

from flask import Flask, Response
import json
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.logger.setLevel(logging.INFO)


@app.route('/airport/<code>')
def airport_name(code):
    yhteys = mysql.connector.connect(
        database='flight_game',
        user='eliell2',
        password='gr0ups',
        autocommit=True)

    sql = f"select ident, name, municipality,latitude_deg,longitude_deg from airport where ident = %s"
    kursori = yhteys.cursor()
    kursori.execute(sql,(code,))
    tulos = kursori.fetchone()
    try:
        status = 200
        answer = {
            'ICAO': tulos[0],
            'Name': tulos[1],
            'Location': tulos[2],
            'lat' : tulos[3],
            'long': tulos[4]
        }
    except ValueError:
        status = 400
        answer = {
            "status": status,
            "teksti": "Virheellinen yhteenlaskettava"
        }
    jsonansw = json.dumps(answer)
    return Response(response=jsonansw, status=status,mimetype="application/json")

if __name__ == '__main__': app.run(use_reloader=True, host='127.0.0.1', port=3000)