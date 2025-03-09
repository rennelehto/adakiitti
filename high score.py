import mysql.connector

yhteys = mysql.connector.connect(
      #  host='127.0.0.1',
      #  port=3306,
        database='flight_game',
        user='pythonuser',
        password='salasana',
        autocommit=True)

def highscore(pisteet):
    sql = f"update highscore set score as {pisteet} where nimi = 'Pelaaja';"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return