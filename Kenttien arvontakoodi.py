import mysql.connector
import random

#Tähän listaan tulee kentän "Ident" -tunnus.
lista_kentistä=[]

def kenttäkysely():
    sql = f"select ident from airport, country where airport.iso_country = country.iso_country and country.iso_country = 'FI' and airport.type = 'medium_airport'"
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
    valitut_kentät.append(lista_kentistä[random.randint(0, 29)])
    määrä=määrä+1

#(k1, k2, k3, k4, k5, k6, k7, k8, k9, k10) = valitut_kentät
#print(k1)

def kenttähaku():
    sql = f'SELECT name FROM airport WHERE ident = "{valitut_kentät[0]}"'
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print('Kentän nimi on ' + rivi[0] + '.')
    return

yhteys = mysql.connector.connect(
      #  host='127.0.0.1',
      #  port=3306,
        database='flight_game',
        user='python',
        password='1232',
        autocommit=True)

kenttähaku()





