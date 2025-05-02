import logging
import random

import mysql.connector

from flask import Flask, Response
import json
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.logger.setLevel(logging.INFO)


@app.route('/airport/')
def airport_name():
    yhteys = mysql.connector.connect(
        database='flight_game',
        user='eliell2',
        password='gr0ups',
        autocommit=True
    )

    mantereet = ['EU', 'AF', 'AS', 'OC', 'SA', 'NA']
    pelattavat_kentät_lista_2 = []
    kursori = yhteys.cursor()

    for m in mantereet:
        sql = f"""
            SELECT ident, airport.name, municipality, latitude_deg, longitude_deg
            FROM airport
            JOIN country ON airport.iso_country = country.iso_country
            WHERE country.continent = '{m}'
              AND airport.type = 'large_airport'
        """
        kursori.execute(sql)
        tulos = kursori.fetchall()
        kenttädata = [{
            'ICAO': r[0],
            'Name': r[1],
            'Location': r[2],
            'lat': r[3],
            'long': r[4]
        } for r in tulos]

        pelattavat_kentät_lista_2.extend(random.sample(kenttädata, min(15, len(kenttädata))))

    kursori.close()
    yhteys.close()

    return Response(
        response=json.dumps(pelattavat_kentät_lista_2, ensure_ascii=False),
        status=200,
        mimetype="application/json"
    )


if __name__ == '__main__': app.run(use_reloader=True, host='127.0.0.1', port=3000)
