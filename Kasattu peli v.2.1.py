import mysql.connector
import random
from geopy import distance

#Euroopassa on 118 suurta kenttää.

lista_kentistäEU=[]
def kenttäkyselyEU():
    sql = f"select ident from airport, country where airport.iso_country = country.iso_country and country.continent = 'EU' and airport.type = 'large_airport'"
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            lista_kentistäEU.append(rivi[0])
    return

#Afrikassa on 45 suurta kenttää.
lista_kentistäAF=[]

def kenttäkyselyAF():
    sql = f"select ident from airport, country where airport.iso_country = country.iso_country and country.continent = 'AF' and airport.type = 'large_airport'"
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            lista_kentistäAF.append(rivi[0])
    return

#Aasiassa on 137 suurta kenttää.
lista_kentistäAS=[]

def kenttäkyselyAS():
    sql = f"select ident from airport, country where airport.iso_country = country.iso_country and country.continent = 'AS' and airport.type = 'large_airport'"
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            lista_kentistäAS.append(rivi[0])
    return

#Oseaniassa on 17 suurta kenttää.
lista_kentistäOC=[]
def kenttäkyselyOC():
    sql = f"select ident from airport, country where airport.iso_country = country.iso_country and country.continent = 'OC' and airport.type = 'large_airport'"
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            lista_kentistäOC.append(rivi[0])
    return

#Pohjois-Amerikassa on 108 suurta kenttää.
lista_kentistäNA=[]
def kenttäkyselyNA():
    sql = f"select ident from airport, country where airport.iso_country = country.iso_country and country.continent = 'NA' and airport.type = 'large_airport'"
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            lista_kentistäNA.append(rivi[0])
    return

#Etelä-Amerikassa on 22 suurta kenttää.
lista_kentistäSA=[]
def kenttäkyselySA():
    sql = f"select ident from airport, country where airport.iso_country = country.iso_country and country.continent = 'SA' and airport.type = 'large_airport'"
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            lista_kentistäSA.append(rivi[0])
    return


#Nämä funktiot tuo kaikki valittujen mantereiden kentät omiksi listoikseen.


#Seuraava funktio arpoo pelattavat kentät

def pelattavat_kentät():
    määräEU = 0
    while määräEU < 15:
        maa = lista_kentistäEU[random.randint(0, 116)]
        valitut_kentätEU.append(maa)
        määräEU = määräEU + 1

    määräAF = 0
    while määräAF < 15:
        maa = lista_kentistäAF[random.randint(0, 44)]
        if maa not in valitut_kentätAF:
            valitut_kentätAF.append(maa)
            määräAF = määräAF + 1

    määräAS = 0
    while määräAS < 15:
        maa = lista_kentistäAS[random.randint(0, 36)]
        if maa not in valitut_kentätAS:
            valitut_kentätAS.append(maa)
            määräAS = määräAS + 1

    määräOC = 0
    while määräOC < 15:
        maa = lista_kentistäOC[random.randint(0, 16)]
        if maa not in valitut_kentätOC:
            valitut_kentätOC.append(maa)
            määräOC = määräOC + 1

    määräNA = 0
    while määräNA < 15:
        maa = lista_kentistäNA[random.randint(0, 107)]
        if maa not in valitut_kentätNA:
            valitut_kentätNA.append(maa)
            määräNA = määräNA + 1

    määräSA = 0
    while määräSA < 15:
        maa = lista_kentistäSA[random.randint(0, 21)]
        if maa not in valitut_kentätSA:
            valitut_kentätSA.append(maa)
            määräSA = määräSA + 1
    return




#tähän loppuu pelattavien kenttien valinta

def pelaajan_koordinaatit(sijainti_icao):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{sijainti_icao}'"
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    #if kursori.rowcount > 0:
     #   for rivi in tulos:
     #       print(f"Pelaajan  koordinaatit: {rivi[0]}, {rivi[1]}.")
    return tulos

def pelaajan_sijainnin_nimi(sijainti_icao):
    sql = f"SELECT name FROM airport WHERE ident = '{sijainti_icao}'"
        # print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
       for rivi in tulos:
           sijainti_nimi.append(rivi[0])
    return tulos

def pelaajan_koordinaatit(sijainti_icao):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE airport.ident = '{sijainti_icao}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

    # tämä hakee kentän koordinaatit

def kentän_etäisyys(py):
    sql = f"SELECT latitude_deg, longitude_deg from airport, country where airport.iso_country = country.iso_country and ident = '{py}'"
    # print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

def matkustettavat_kentät():
    k = 1
    while k <= len(pelattavat_kentät) - 1:
        h = pelattavat_kentät[k]
        seur = kentän_etäisyys(h)

        if ((liikkeet + kerätyt_kivet) * 500) > distance.distance(pelikoordinaatit, seur).km > 0:
            seuraavat_kentät.append(h)
        k = k + 1
    return

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

def listaus():
    x = 0
    while x < len(seuraavat_kentät):
        n = seuraavat_kentät[x]
        koodi_nimeksi(n)
        x = x + 1

def kenttäluettelo():
    x = 0
    print('Tässä kentät joille voit matkustaa:')
    print()
    for k in seuraavien_kenttien_nimet:
        print(f'{x + 1}.  {k}')
        x = x + 1
    return

def peliluuppi2(t2):
    print(f'\nOlet saapunut kentälle: {sijainti_nimi[0]}')
    print(f'Kentän koodi: {sijainti_icao}\n')
    t1 = kiviarpa()
    t3 = t1 + t2
    print(f'Kivien kerätty arvo: {T}.\n')
    sijainti_nimi.clear()
    seuraavat_kentät.clear()
    seuraavien_kenttien_nimet.clear()
    pelaajan_koordinaatit(sijainti_icao)
    matkustettavat_kentät()
    listaus()
    kenttäluettelo()
    return t3

def peliluuppi(i):
    print(f'\nOlet saapunut kentälle: {sijainti_nimi[0]}')
    print(f'Kentän koodi: {sijainti_icao}\n')
    kiviarpa(i)
    sijainti_nimi.clear()
    seuraavat_kentät.clear()
    seuraavien_kenttien_nimet.clear()
    pelaajan_koordinaatit(sijainti_icao)
    matkustettavat_kentät()
    listaus()
    kenttäluettelo()
    return

def seuraava_kohde():
    print()
    tulos = seuraavat_kentät[int(input('Mille kentälle seuraavaksi? ')) - 1]
    return tulos

def kiviarpa():
    tulos = random.randint(1,6)
    if tulos == 6:
        xy = (random.randint(1,6) * 2)
        print('\nLöysit suuren kiven!')

    if tulos in range(3,6):
        xy = random.randint(1,6)
        print('\nLöysit kiven!')

    if tulos in range(0,3):
        print('\nKentällä ei ole kiveä.')

    return xy

#    PÄÄOHJELMA

yhteys = mysql.connector.connect(
      #  host='127.0.0.1',
      #  port=3306,
        database='flight_game',
        user='pythonuser',
        password='salasana',
        autocommit=True)


kenttäkyselyEU()
kenttäkyselyAF()
kenttäkyselyAS()
kenttäkyselyOC()
kenttäkyselyNA()
kenttäkyselySA()

valitut_kentätEU=[]
valitut_kentätAF=[]
valitut_kentätAS=[]
valitut_kentätOC=[]
valitut_kentätNA=[]
valitut_kentätSA=[]


pelattavat_kentät()

#pelattavat kentät samaan listaan
pelattavat_kentät=[]
pelattavat_kentät.extend(valitut_kentätEU)
pelattavat_kentät.extend(valitut_kentätAF)
pelattavat_kentät.extend(valitut_kentätAS)
pelattavat_kentät.extend(valitut_kentätOC)
pelattavat_kentät.extend(valitut_kentätNA)
pelattavat_kentät.extend(valitut_kentätSA)

print("\n                                                                                         Adakite--Adakiitti")
pelaajan_nimi = input("Ole hyvä ja syötä nimesi: ")

def peli_alkaa():
    print(f"\nHei {pelaajan_nimi}! Tehtäväsi on pelastaa maailma ilkeältä velholta, joka pyrkii keräämään maagisia kiviä joilla hän haluaa aiheuttaa ilmastokatastrofin.")

    Pelin_aloitus = int(input(                          #Vastaus valinta
                    "\n1. Asia selvä. "
                    "\n2. Okei. "
                    "\n3. En halua. "
                    "\n: "))
    while int(Pelin_aloitus) == 1 or 2 or 3:
        if Pelin_aloitus == 1:
            print("--------------------------------------------------")
            print("Asia selvä.")
            print("--------------------------------------------------")
            break
        if Pelin_aloitus == 2 :
            print("--------------------------------------------------")
            print("Okei.")
            print("--------------------------------------------------")
            break
        if Pelin_aloitus == 3:
            print("--------------------------------------------------")
            print("Valitettavasti et saa jatkaa.")
            print("--------------------------------------------------")
            quit()
        if Pelin_aloitus != [1,2,3]:
            print("--------------------------------------------------")
            print("Error,please try again")
            print("--------------------------------------------------")
            Pelin_aloitus = int(input(  # Vastaus valinta
                "\n1. Asia selvä. "
                "\n2. Okei. "
                "\n3. En halua. "
                "\n: "))

    print("Onnea matkaan, ja käytä voimiasi hyvään.")
    print("--------------------------------------------------\n")


sijainti_icao = pelattavat_kentät[random.randint(0,89)]

sijainti_nimi = []
pelaajan_sijainnin_nimi(sijainti_icao)

#liikkuminen ja kivet
liikkeet = 4 #alussa
kivet = 10
kerätyt_kivet = 5
kerätyt_pisteet = 0
kierrokset = 1

pelikoordinaatit = pelaajan_koordinaatit(sijainti_icao)

seuraavat_kentät = []
seuraavien_kenttien_nimet = []

peli_alkaa()
while kierrokset < 2:
    kerätyt_kivet = peliluuppi2(kerätyt_kivet)
    sijainti_icao = seuraava_kohde()
    pelaajan_sijainnin_nimi(sijainti_icao)
    pelattavat_kentät.remove(sijainti_icao)
    kierrokset = kierrokset + 1
while kerätyt_kivet < 40:
    peliluuppi(kerätyt_kivet)
    sijainti_icao = seuraava_kohde()
    pelaajan_sijainnin_nimi(sijainti_icao)
    pelattavat_kentät.remove(sijainti_icao)
    kierrokset = kierrokset + 1
