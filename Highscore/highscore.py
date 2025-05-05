import logging
import mysql.connector
from flask import Flask, Response, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.logger.setLevel(logging.INFO)


@app.route('/highscore/')

def highscores():
    yhteys = mysql.connector.connect(
        database='flight_game',
        user='python',
        password='1232',
        autocommit=True)

    huipputulokset = []
    sql = f'select peli.nimi, highscore.pisteet from peli, highscore where peli.id = highscore.id order by highscore.pisteet desc, pisteet asc limit 10'
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    pistedata = [{
        'Nimi': r[0],
        'Pisteet': r[1]
    } for r in tulos]
    kursori.close()
    yhteys.close()
    huipputulokset.extend(pistedata)

    return Response(
        response=json.dumps(huipputulokset, ensure_ascii=False),
        status=200,
        mimetype="application/json"
    )
if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)