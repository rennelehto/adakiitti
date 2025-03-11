import mysql.connector
import random
from geopy import distance

yhteys = mysql.connector.connect(
      #  host='127.0.0.1',
      #  port=3306,
        database='flight_game',
        user='eliell2',
        password='gr0ups',
        autocommit=True)

seuraavat_kentät = []
seuraavien_kenttien_nimet = []

lista_kentistäEU=[]
def kenttäkyselyEU():
    sql = f"select ident from airport, country where airport.iso_country = country.iso_country and country.continent = 'EU' and airport.type = 'large_airport'"
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if tulos:
        for rivi in tulos:
            lista_kentistäEU.append(rivi[0])
    return
lista_kentistäAF=[]
def kenttäkyselyAF():
    sql = f"select ident from airport, country where airport.iso_country = country.iso_country and country.continent = 'AF' and airport.type = 'large_airport'"
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if tulos:
        for rivi in tulos:
            lista_kentistäAF.append(rivi[0])
    return
lista_kentistäAS=[]
def kenttäkyselyAS():
    sql = f"select ident from airport, country where airport.iso_country = country.iso_country and country.continent = 'AS' and airport.type = 'large_airport'"
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if tulos:
        for rivi in tulos:
            lista_kentistäAS.append(rivi[0])
    return
lista_kentistäOC=[]
def kenttäkyselyOC():
    sql = f"select ident from airport, country where airport.iso_country = country.iso_country and country.continent = 'OC' and airport.type = 'large_airport'"
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if tulos:
        for rivi in tulos:
            lista_kentistäOC.append(rivi[0])
    return
lista_kentistäNA=[]
def kenttäkyselyNA():
    sql = f"select ident from airport, country where airport.iso_country = country.iso_country and country.continent = 'NA' and airport.type = 'large_airport'"
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if tulos:
        for rivi in tulos:
            lista_kentistäNA.append(rivi[0])
    return
lista_kentistäSA=[]
def kenttäkyselySA():
    sql = f"select ident from airport, country where airport.iso_country = country.iso_country and country.continent = 'SA' and airport.type = 'large_airport'"
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if tulos:
        for rivi in tulos:
            lista_kentistäSA.append(rivi[0])
    return
def pelattavat_kentät():
    määrä_dict = {"EU": 15, "AF": 15, "AS": 15, "OC": 15, "NA": 15, "SA": 15}
    kenttä_listat = {
        "EU": lista_kentistäEU,
        "AF": lista_kentistäAF,
        "AS": lista_kentistäAS,
        "OC": lista_kentistäOC,
        "NA": lista_kentistäNA,
        "SA": lista_kentistäSA
    }

    for maanosa, määrä in määrä_dict.items():
        pelattavat_kentät_lista_2.extend(random.sample(kenttä_listat[maanosa], min(määrä, len(kenttä_listat[maanosa]))))

def pelaajan_koordinaatit(sijainti_icao):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{sijainti_icao}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos_kordinaatit = kursori.fetchone()
    kursori.close()
    return tulos_kordinaatit if tulos_kordinaatit else (0, 0)
def pelaajan_sijainnin_nimi(sijainti_icao):
    sql = f"SELECT name FROM airport WHERE ident = '{sijainti_icao}'"
        # print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos_nimi = kursori.fetchall()
    if tulos_nimi:
       for rivi in tulos_nimi:
           sijainti_nimi.append(rivi[0])
    return tulos_nimi
    # tämä hakee kentän koordinaatit
def kentän_etäisyys(py):
    sql = f"SELECT latitude_deg, longitude_deg from airport, country where airport.iso_country = country.iso_country and ident = '{py}'"
    # print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos
def matkustettavat_kentät():
    for h in pelattavat_kentät_lista_2:
        seur = kentän_etäisyys(h)
        if seur:
            seur_lat, seur_lon = seur[0]

            if 0 < distance.distance(pelikoordinaatit, (seur_lat, seur_lon)).km < ((liikkeet + kerätyt_kivet) * 500):
                seuraavat_kentät.append(h)
def koodi_nimeksi(koodi):
    sql = f"SELECT name FROM airport WHERE ident = '{koodi}'"
    # print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if tulos:
        for rivi in tulos:
            if rivi not in seuraavien_kenttien_nimet:
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
    for x in range(min(20, len(seuraavien_kenttien_nimet))):
        print(f'{x + 1}. {seuraavien_kenttien_nimet[x]}')
        x = x + 1
    return
def peliluuppi1():
    print()
    print(f'Olet saapunut kentälle: {sijainti_nimi[0]}')
    print(f'Kentän koodi: {sijainti_icao}')
    print("Löysit täältä adakiitin jonka arvo on 5! ")
    print()
    pelaajan_koordinaatit(sijainti_icao)
    matkustettavat_kentät()
    listaus()
    kenttäluettelo()
    return
def peliluuppi2(eih):
    print()
    print(f'Olet saapunut kentälle: {sijainti_nimi[0]}')
    print(f'Kentän koodi: {sijainti_icao}')
    print()
    xx = kiviarpa()
    xy = eih + xx
    print(f'Kivien kerätty arvo: {xy}.')
    vastaus = input("1. Jee!"
                    "\n2. Voi ei :("
                    "\n3. Tiesitkö ")
    sijainti_nimi.clear()
    seuraavat_kentät.clear()
    seuraavien_kenttien_nimet.clear()
    pelaajan_koordinaatit(sijainti_icao)
    matkustettavat_kentät()
    listaus()
    return xy
def seuraava_kohde():
    while True:
        try:
            valinta = int(input('Mille kentälle seuraavaksi? ')) - 1
            if 0 <= valinta < len(seuraavat_kentät):
                return seuraavat_kentät[valinta]
            else:
                print("Virheellinen valinta, yritä uudelleen.")
        except ValueError:
            print("Syötä numero.")
def kiviarpa():

    tulos_kiviarpa = random.randint(1,6)
    if tulos_kiviarpa == 6:
        pöö = (random.randint(1,6) * 2)
        print("")
        print('Löysit suuren adakiitin!')
        print(f"Sen arvo on: {pöö}")



    elif tulos_kiviarpa in range(3,6):
        pöö = random.randint(1,6)
        print("")
        print('Löysit adakiitin!')
        print(f"Sen arvo on: {pöö}")



    elif tulos_kiviarpa < 3:
        pöö = 0
        print("")
        print('Kentällä ei ole adakiittiä.')


    return pöö
#    PÄÄOHJELMA



pelattavat_kentät_lista_2=[]



valitut_kentätEU = []
valitut_kentätAF = []
valitut_kentätAS = []
valitut_kentätOC = []
valitut_kentätNA = []
valitut_kentätSA = []

kenttäkyselyEU()
kenttäkyselyAF()
kenttäkyselyAS()
kenttäkyselyOC()
kenttäkyselyNA()
kenttäkyselySA()


pelattavat_kentät()
print(" ")
print("                                                                                         Adakite--Adakiitti")
pelaajan_nimi = input("Ole hyvä ja syötä nimesi: ")

def peli_alkaa():
    print(" ")
    print(f"Hei {pelaajan_nimi}! Tehtäväsi on pelastaa maailma ilkeältä velholta, joka pyrkii keräämään maagisia kiviä joilla hän haluaa aiheuttaa ilmastokatastrofin.")

    Pelin_aloitus = int(input(                          #Vastaus valinta
                    "\n1. Asia selvä. "
                    "\n2. Okei. "
                    "\n3. En halua. "
                    "\n: "))
    while Pelin_aloitus in [1,2,3]:
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
        if Pelin_aloitus not in [1,2,3]:
            print("--------------------------------------------------")
            print("Error,please try again")
            print("--------------------------------------------------")
            Pelin_aloitus = int(input(  # Vastaus valinta
                "\n1. Asia selvä. "
                "\n2. Okei. "
                "\n3. En halua. "
                "\n: "))

    print("Onnea matkaan, ja käytä voimiasi hyvään.")
    print("--------------------------------------------------")
    print(" ")


sijainti_icao = random.choice(pelattavat_kentät_lista_2)

sijainti_nimi = []
pelaajan_sijainnin_nimi(sijainti_icao)

liikkeet = 4
kerätyt_kivet = int(5)
kierrokset = 1

pelikoordinaatit = pelaajan_koordinaatit(sijainti_icao)

print()


peli_alkaa()

while kierrokset < 2:
    peliluuppi1()
    sijainti_icao = seuraava_kohde()
    pelaajan_sijainnin_nimi(sijainti_icao)
    if sijainti_icao in pelattavat_kentät_lista_2:
        pelattavat_kentät_lista_2.remove(sijainti_icao)
    kierrokset = kierrokset + 1

while kerätyt_kivet < 40:
    kerätyt_kivet = peliluuppi2(kerätyt_kivet)
    if kerätyt_kivet >= 40:
        kerätyt_kivet = 40
        break
    kenttäluettelo()
    sijainti_icao = seuraava_kohde()
    pelaajan_sijainnin_nimi(sijainti_icao)
    if sijainti_icao in pelattavat_kentät_lista_2:
        pelattavat_kentät_lista_2.remove(sijainti_icao)
    kierrokset = kierrokset + 1

    #muutokset peli tulostaa löydetyn kiven arvon, poistin valitutkentät:extend jutut, muokkasin kordinaatti hakuua, sekä sql hakua tekemällä if tulos: eikä if tulos >0:,
    # ja muokkasin myös seuraava kohde funktiota
    #sekä loin uuden pelattavat kentät funktion luomalla dictionaryn, jolla saimme poistettua kopioita.


print("Olet löytänyt 40 adakiittia! Onneksi olkoon, seuraavassa jaksossa loppuhuippennuksena kaksintaistelu vihollisen kanssa!")