import mysql.connector
from geopy import distance
'''Tässä on mallina vaan väärä kenttälista, saa kokeilla!
Tähän lisätään kans kertoimena kivien määrä, eli kolme kiveä = 3*500km jne'''
#TOIMII
#tekee listan pelattavista kentistä
def pelattavat():
    sql = f"select ident from airport, country where airport.iso_country = country.iso_country and country.iso_country = 'FI' and airport.type = 'medium_airport'"
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    pelattavat_kentät.append(tulos)
    if kursori.rowcount > 0:
        for rivi in tulos:
            pelattavat_kentät.append(rivi[0])
    return

#TOIMII
#hakee pelaajan koordinaatit
def pelaajan_sijainti():
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE airport.ident = 'EFHK'"
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Pelaajan  koordinaatit: {rivi[0]}, {rivi[1]}.")
    return tulos

#TOIMII
#tämä hakee kentän koordinaatit
def kentän_etäisyys(pylly):
    sql = f"SELECT latitude_deg, longitude_deg from airport, country where airport.iso_country = country.iso_country and ident = '{pylly}'"
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    #if kursori.rowcount > 0:
       # for rivi in tulos:
           #print(f"{rivi[0]}, {rivi[1]}.")
    return tulos

#TOIMII
#Jostain syystä pelattavien kenttien eka alkio on koko lista, korjaan myöhemmin
def matkustettavat_kentät():
    k=1
    while k <= len(pelattavat_kentät)-1:
        h = pelattavat_kentät[k]
        pylly = h
        seur = kentän_etäisyys(pylly)

        if distance.distance(sijainti, seur).km <= 500:
            seuraavat_kentät.append(h)
        k = k + 1
    return

yhteys = mysql.connector.connect(
        database='flight_game',
        user='python',
        password='1232',
        autocommit=True
)




pelattavat_kentät=[]
seuraavat_kentät=[]

sijainti = pelaajan_sijainti()
pelattavat()
matkustettavat_kentät()
print(f'Pelattavia kenttiä: {len(pelattavat_kentät)}')
print(f'Matkustettavia kenttiä: {len(seuraavat_kentät)}')




