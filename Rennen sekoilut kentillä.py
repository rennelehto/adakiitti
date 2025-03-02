import mysql.connector
import random

#Tähän kokeiluun otin Suomen keskikokoiset kentät ja arvoin niistä 10 listalle.
lista=[]
def kysely():
    sql = f"select ident from airport, country where airport.iso_country = country.iso_country and country.iso_country = 'FI' and airport.type = 'medium_airport'"
   # print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            lista.append(rivi)
    return

yhteys = mysql.connector.connect(
      #  host='127.0.0.1',
      #  port=3306,
        database='flight_game',
        user='python',
        password='1232',
        autocommit=True)
kysely()

valitut=[]
määrä = 0
while määrä < 10:
    valitut.append(lista[random.randint(0, 29)])
    määrä=määrä+1

print(valitut)
print(lista)

#Tähän saakka toimii

kivet = 5

while kivet > 0:
    tulos = random.randint(0,1)
    if tulos == 1:
        print(kivet)
        kivet = kivet - 1
    else:
        print('Ei kiviä')