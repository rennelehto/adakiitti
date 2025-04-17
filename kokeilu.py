import mysql.connector
import random
from geopy import distance

yhteys = mysql.connector.connect(
      #  host='127.0.0.1',
      #  port=3306,
        database='flight_game',
        user='python',
        password='1232',
        autocommit=True)




pelattavat_kentät=[]
def kenttäkysely():
    mantereet = 'EU', 'AF', 'AS', 'OC', 'SA', 'NA'
    lista_kentistä = []
    y = 1
    for m in mantereet:
        sql = f"select ident from airport, country where airport.iso_country = country.iso_country and country.continent = '{m}' and airport.type = 'large_airport'"
        #print(sql)
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchall()
        if tulos:
            for rivi in tulos:
                lista_kentistä.append(rivi[0])

            while len(pelattavat_kentät) < 15*y:
                x = lista_kentistä[random.randint(1, len(lista_kentistä)) - 1]
                if x not in pelattavat_kentät:
                    pelattavat_kentät.append(x)
            lista_kentistä.clear()
            y+=1
    return
kenttäkysely()
print(pelattavat_kentät)
print(len(pelattavat_kentät))
