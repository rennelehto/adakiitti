import mysql.connector
import random

#Tähän listaan tulee kentän "Ident" -tunnus.
lista_kentistä=[]

def kenttäkysely():
    sql = f"select airport.name from airport, country where airport.iso_country = country.iso_country and country.iso_country = 'FI' and airport.type = 'medium_airport'"
   # print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            lista_kentistä.append(rivi[0])
    return

yhteys = mysql.connector.connect(
      #  host='127.0.0.1',
      #  port=3306,
        database='flight_game',
        user='python',
        password='1232',
        autocommit=True)

kenttäkysely()

#Tähän listaan tulee peliin arvotut kentät.

valitut_kentät=[]
määrä = 0
while määrä < 10:
    maa = lista_kentistä[random.randint(0, 29)]
    if maa not in valitut_kentät:
        valitut_kentät.append(maa)
        määrä=määrä+1

print(valitut_kentät)

#(k1, k2, k3, k4, k5, k6, k7, k8, k9, k10) = valitut_kentät
#print(k1)


def kenttähaku():
    sql = f'SELECT name FROM airport WHERE ident = "{valitut_kentät[0]}"'
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print('Valitun kentän nimi on ' + rivi[0] + '.')
    return tulos

def sijainnin_vaihto():
    sql = f"UPDATE peli SET sijainti = (SELECT ident FROM airport WHERE name = '{tulos}') WHERE nimi = 'pelaaja'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return

yhteys = mysql.connector.connect(
      #  host='127.0.0.1',
      #  port=3306,
        database='flight_game',
        user='python',
        password='1232',
        autocommit=True)

tulos = kenttähaku()

sijainnin_vaihto()



