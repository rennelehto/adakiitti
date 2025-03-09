import mysql.connector
import random
'''
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
            lista.append(rivi[0])
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

#Kivikoodi

kivet = 5

while kivet > 0:
    tulos = random.randint(0,1)
    if tulos == 1:
        print(kivet)
        kivet = kivet - 1
    else:
        print('Ei kiviä')

kivet = 5
kerätyt_kivet=0

def kiviarpa(kivet):
    if kivet >0:
        tulos = random.randint(0, 1)
        if tulos == 1:
            kerätyt_kivet = kerätyt_kivet + random.randint(1, 6)
            print(kerätyt_kivet)
            kivet = kivet - 1
        else:
            print('Ei kiviä')'''
'''
def pelaajat():
    nimimerkki = input("Ole hyvä ja syötä nimesi: ")
    sql = f"insert into peli (nimi) values ('{nimimerkki}')"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return
'''

def sijainnin_vaihto():
    sql = f"ALTER TABLE peli SET sijainti as (select ident from airport where name = '{}') WHERE nimi = 'pelaaja';"
        # print(sql)
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

sijainnin_vaihto()