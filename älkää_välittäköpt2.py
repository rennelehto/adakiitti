
import mysql.connector
import random
from geopy import distance

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
def pelaajan_koordinaatit(sijainti_icao):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{sijainti_icao}'"
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos
def pelaajan_sijainnin_nimi(sijainti_icao):
    sql = f"SELECT name FROM airport WHERE ident = '{sijainti_icao}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
       for rivi in tulos:
           hyviksen_sijainti_nimi.append(rivi[0])
    return tulos
#-----------------------------------------------------------------------------------------------------------------------
#Vihollisen lokaatio

def kentän_etäisyys_pahis(py):
    sql = f"SELECT latitude_deg, longitude_deg from airport, country where airport.iso_country = country.iso_country and ident = '{py}'"
    # print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos
def matkustettavat_kentät_pahis():
    k = 1
    while k <= 20: #Hakee vain ensimmäiset 20 kenttää
        h = pelattavat_kentät[k]
        py = h
        seur = kentän_etäisyys_pahis(py)

        if ((liikkeet_pahis + kerätyt_kivet_pahis) * 500) > distance.distance(pelikoordinaatit_pahis, seur).km > 0:
            seuraavat_kentät_pahis.append(h)
        k = k + 1
    return
def koodi_nimeksi_pahis(koodi):
    sql = f"SELECT distinct name FROM airport WHERE ident = '{koodi}'"
    # print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount < 20:
        for rivi in tulos:
            seuraavien_kenttien_nimet_pahis.append(rivi[0])
    return tulos
def listaus_pahis():
    x = 1
    while x < len(seuraavat_kentät_hyvis):
        n = seuraavat_kentät_pahis[x]
        äh_p = koodi_nimeksi_pahis(n)
        x = x + 1
def pahiksen_koordinaatit(sijainti_icao):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{sijainti_icao}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos
def pahiksen_sijainnin_nimi(sijainti_icao):
    sql = f"SELECT name FROM airport WHERE ident = '{sijainti_icao}'"
        # print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
       for rivi in tulos:
           pahiksen_sijainti_nimi.append(rivi[0])
    return tulos
def peliluuppi3():
    pahiksen_sijainti_nimi.clear()
    seuraavat_kentät_pahis.clear()
    seuraavien_kenttien_nimet_pahis.clear()
    pahiksen_koordinaatit(pahiksen_sijainti_icao)
    matkustettavat_kentät_pahis()
    listaus_pahis()
    return
def peliluuppi4(eih):
    xx = kiviarpa_pahis()
    xy = eih + xx
    pahiksen_sijainti_nimi.clear()
    seuraavat_kentät_pahis.clear()
    seuraavien_kenttien_nimet_pahis.clear()
    pahiksen_koordinaatit(pahiksen_sijainti_icao)
    matkustettavat_kentät_pahis()
    listaus_pahis()
    return xy
def kiviarpa_pahis():
    tulos = random.randint(1,6)
    if tulos == 6:
        pöö_pahis = (random.randint(1,6) * 2)
    elif tulos in range(3,6):
        pöö_pahis = random.randint(1,6)
    elif tulos < 3:
        pöö_pahis = 0
    return pöö_pahis

def seuraava_kohde_pahis():
    tulos = seuraavat_kentät_hyvis[len(pelattavat_kentät[random.randint(1,len(pelattavat_kentät))]- 1)]
    return tulos
#-----------------------------------------------------------------------------------------------------------------------
    # tämä hakee kentän koordinaatit
def kentän_etäisyys_hyvis(py):
    sql = f"SELECT latitude_deg, longitude_deg from airport, country where airport.iso_country = country.iso_country and ident = '{py}'"
    # print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos
def matkustettavat_kentät_hyvis():
    k = 1
    while k <= 20: #Hakee vain ensimmäiset 20 kenttää
        h = pelattavat_kentät[k]
        py = h
        seur = kentän_etäisyys_hyvis(py)

        if ((liikkeet_hyvis + kerätyt_kivet_hyvis) * 500) > distance.distance(pelikoordinaatit_hyvis, seur).km > 0:
            seuraavat_kentät_hyvis.append(h)
        k = k + 1
    return
def koodi_nimeksi_hyvis(koodi):
    sql = f"SELECT distinct name FROM airport WHERE ident = '{koodi}'"
    # print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount < 20:
        for rivi in tulos:
            seuraavien_kenttien_nimet_hyvis.append(rivi[0])
    return tulos
def listaus_hyvis():
    x = 1
    while x < len(seuraavat_kentät_hyvis):
        n = seuraavat_kentät_hyvis[x]
        äh_h = koodi_nimeksi_hyvis(n)
        x = x + 1
def kenttäluettelo_hyvis():
    x = 0
    print('Tässä kentät joille voit matkustaa:')
    print()
    for k in seuraavien_kenttien_nimet_hyvis:
        print(f'{x + 1}.  {k}')
        x = x + 1
    return
def peliluuppi1():
    print()
    print(f'Olet saapunut kentälle: {hyviksen_sijainti_nimi[0]}')
    print(f'Kentän koodi: {hyviksen_sijainti_icao}')
    print()
    hyviksen_sijainti_nimi.clear()
    seuraavat_kentät_hyvis.clear()
    seuraavien_kenttien_nimet_hyvis.clear()
    pelaajan_koordinaatit(hyviksen_sijainti_icao)
    matkustettavat_kentät_hyvis()
    listaus_hyvis()
    kenttäluettelo_hyvis()
    return
def peliluuppi2(eih):
    print()
    print(f'Olet saapunut kentälle: {hyviksen_sijainti_nimi[0]}')
    print(f'Kentän koodi: {hyviksen_sijainti_icao}')
    print()
    xx = kiviarpa_hyvis()
    xy = eih + xx
    print(f'Hallussasi olevien adakiittien arvo: {xy}.')
    hyviksen_sijainti_nimi.clear()
    seuraavat_kentät_hyvis.clear()
    seuraavien_kenttien_nimet_hyvis.clear()
    pelaajan_koordinaatit(hyviksen_sijainti_icao)
    matkustettavat_kentät_hyvis()
    listaus_hyvis()
    kenttäluettelo_hyvis()
    return xy
def seuraava_kohde_hyvis():
    print()
    tulos = seuraavat_kentät_hyvis[int(input('Mille kentälle seuraavaksi? ')) - 1]
    return tulos
def kiviarpa_hyvis():

    tulos = random.randint(1,6)
    if tulos == 6:
        pöö = (random.randint(1,6) * 2)
        print("")
        print('Löysit suuren adakiitin!')
        print(f"Kivesi arvo on: {pöö}")



    elif tulos in range(3,6):
        pöö = random.randint(1,6)
        print("")
        print('Löysit adakiitin!')
        print(f"Kivesi arvo on: {pöö}")



    elif tulos < 3:
        pöö = 0
        print("")
        print('Kentällä ei ole adakiittiä.')


    return pöö

#    PÄÄOHJELMA

yhteys = mysql.connector.connect(
      #  host='127.0.0.1',
      #  port=3306,
        database='flight_game',
        user='eliell2',
        password='gr0ups',
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

pelattavat_kentät=[]
pelattavat_kentät.extend(valitut_kentätEU)
pelattavat_kentät.extend(valitut_kentätAF)
pelattavat_kentät.extend(valitut_kentätAS)
pelattavat_kentät.extend(valitut_kentätOC)
pelattavat_kentät.extend(valitut_kentätNA)
pelattavat_kentät.extend(valitut_kentätSA)

print(" ")
print("                                                                                         Adakite--Adakiitti")
pelaajan_nimi = input("Ole hyvä ja syötä nimesi: ").capitalize()

def peli_alkaa():
    print(" ")
    print(f"Hei {pelaajan_nimi}! Tehtäväsi on pelastaa maailma ilkeältä velholta, joka pyrkii keräämään maagisia adakiittiä joilla hän haluaa aiheuttaa ilmastokatastrofin."
          " \n Sinun täytyy kerätä adakiittiä, ja kerätä ilmatopisteitä voidaksesi päihittää velhon. ")

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
    print("--------------------------------------------------")
    print(" ")


hyviksen_sijainti_icao = pelattavat_kentät[random.randint(0,89)]
pahiksen_sijainti_icao = pelattavat_kentät[random.randint(0,89)]

hyviksen_sijainti_nimi = []
pelaajan_sijainnin_nimi(hyviksen_sijainti_icao)

pahiksen_sijainti_nimi = []
pahiksen_sijainnin_nimi(pahiksen_sijainti_icao)





liikkeet_hyvis = 4
liikkeet_pahis = 4
kerätyt_kivet_hyvis = 5
kerätyt_kivet_pahis = 5
kierrokset_hyvis = 1
kierrokset_pahis = 1

pelikoordinaatit_hyvis = pelaajan_koordinaatit(hyviksen_sijainti_icao)
pelikoordinaatit_pahis = pahiksen_koordinaatit(pahiksen_sijainti_icao)
print()
seuraavat_kentät_hyvis = []
seuraavien_kenttien_nimet_hyvis = []

seuraavat_kentät_pahis = []
seuraavien_kenttien_nimet_pahis = []




peli_alkaa()
while kierrokset_hyvis < 2:
    peliluuppi1()
    hyviksen_sijainti_icao = seuraava_kohde_hyvis()
    pelaajan_sijainnin_nimi(hyviksen_sijainti_icao)
    pelattavat_kentät.remove(hyviksen_sijainti_icao)
    kierrokset_hyvis = kierrokset_hyvis + 1

while kerätyt_kivet_hyvis < 40:
    kerätyt_kivet_hyvis = peliluuppi2(kerätyt_kivet_hyvis)
    if kerätyt_kivet_hyvis >= 40: #Lopettaa pelin jos kivien määrä on 40 tai yli
        kerätyt_kivet_hyvis = 40
        break
    hyviksen_sijainti_icao = seuraava_kohde_hyvis()
    pelaajan_sijainnin_nimi(hyviksen_sijainti_icao)
    pelattavat_kentät.remove(hyviksen_sijainti_icao)
    kierrokset_hyvis = kierrokset_hyvis + 1
#pahiksen looppi
while kierrokset_pahis < 2:
    peliluuppi3()
    pahiksen_sijainti_icao = seuraava_kohde_pahis()
    pahiksen_sijainnin_nimi(pahiksen_sijainti_icao)
    pelattavat_kentät.remove(pahiksen_sijainti_icao)
    kierrokset_pahis = kierrokset_pahis + 1

while kerätyt_kivet_pahis < 40:
    kerätyt_kivet_pahis = peliluuppi4(kerätyt_kivet_pahis)
    if kerätyt_kivet_pahis >= 40: #Lopettaa pelin jos kivien määrä on 40 tai yli
        kerätyt_kivet_pahis = 40
        break
    pahiksen_sijainti_icao = seuraava_kohde_pahis()
    pahiksen_sijainnin_nimi(pahiksen_sijainti_icao)
    pelattavat_kentät.remove(pahiksen_sijainti_icao)
    kierrokset = kierrokset_pahis + 1