import mysql.connector
from geopy import distance
'''Tässä on mallina vaan väärä kenttälista, saa kokeilla!
Tähän lisätään kans kertoimena kivien määrä, eli kolme kiveä = 3*500km jne'''

#tekee listan pelattavista kentistä
def pelattavat():
    sql = f"select ident from airport, country where airport.iso_country = country.iso_country and country.iso_country = 'FI' and airport.type = 'medium_airport'"
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            pelattavat_kentät.append(rivi[0])

    return tulos

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

#tämä hakee kentän koordinaatit
def kentän_etäisyys(pylly):
    sql = f"SELECT latitude_deg, longitude_deg from airport, country where airport.iso_country = country.iso_country and ident = '{pylly}'"
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

#etsii kentät joille pelaajalla on pääsy
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

#muuttaa kenttien ICAO-koodit nimiksi
def koodi_nimeksi(koodi):
    sql = f"SELECT name FROM airport WHERE ident = '{koodi}'"
    # print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            seuraavien_kenttien_nimet.append(rivi[0])
    return tulos

#käy koodit läpi nimenmuutosta varten
def listaus():
    x = 0
    while x < len(seuraavat_kentät):
        n = seuraavat_kentät[x]
        äh = koodi_nimeksi(n)
        x = x+1

#Luettelee pelaajalle kentät joille voi matkustaa
def kenttäluettelo():
    x=0
    print('Tässä kentät joille voit matkustaa:')
    print()
    for k in seuraavien_kenttien_nimet:
        print(f'{x+1}.  {k}')
        x=x+1
    return

#koko kierroksen silmukka
def uusi_kierros():
    seuraavat_kentät.clear()
    seuraavien_kenttien_nimet.clear()

    matkustettavat_kentät()
    listaus()
    kenttäluettelo()

yhteys = mysql.connector.connect(
        database='flight_game',
        user='python',
        password='1232',
        autocommit=True
)




#lista listoista hehe
pelattavat_kentät=[]
seuraavat_kentät=[]
seuraavien_kenttien_nimet=[]

sijainti = pelaajan_sijainti()
print()

pelattavat()

print(f'Pelattavia kenttiä: {len(pelattavat_kentät)}')

matkustettavat_kentät()

print()
listaus()

print()
kenttäluettelo()

print()

print(f'Nimettyjä kenttiä: {len(seuraavien_kenttien_nimet)}')
print(f'Matkustettavia kenttiä: {len(seuraavat_kentät)}')

print()

valinta = input('Seuraava kierros? (kyllä/ei) ')

while valinta == 'kyllä':
    uusi_kierros()
    print()
    valinta = input('Seuraava kierros? (kyllä/ei) ')
else:
    print()
    print('Kiitos pelistä!')









