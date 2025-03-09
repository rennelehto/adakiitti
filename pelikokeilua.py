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
    #if kursori.rowcount > 0:
     #  for rivi in tulos:
      #     pelikoordinaatit.append(rivi[0])
      #     pelikoordinaatit.append(rivi[1])
    return tulos

    # tämä hakee kentän koordinaatit
def kentän_etäisyys(pylly):
    sql = f"SELECT latitude_deg, longitude_deg from airport, country where airport.iso_country = country.iso_country and ident = '{pylly}'"
    # print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

def matkustettavat_kentät():
    k = 1
    while k <= len(pelattavat_kentät) - 1:
        h = pelattavat_kentät[k]
        pylly = h
        seur = kentän_etäisyys(pylly)

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
        äh = koodi_nimeksi(n)
        x = x + 1

def kenttäluettelo():
    x = 0
    print('Tässä kentät joille voit matkustaa:')
    print()
    for k in seuraavien_kenttien_nimet:
        print(f'{x + 1}.  {k}')
        x = x + 1
    return


def peliluuppi():
    print()
    print(f'Olet nyt kentällä {sijainti_nimi[0]}')
    print(f'Kentän koodi: {sijainti_icao}')
    print()
    #kivet, kerätyt_kivet = kiviarpa(kivet, kerätyt_kivet)
    kivet_pelissä(kivet, kerätyt_kivet)
    sijainti_nimi.clear()
    seuraavat_kentät.clear()
    seuraavien_kenttien_nimet.clear()
    pelaajan_koordinaatit(sijainti_icao)
    matkustettavat_kentät()
    # koodi_nimeksi()
    listaus()

    kenttäluettelo()

    #seuraava_kohde()
    return

def seuraava_kohde():
    print()
    tulos = seuraavat_kentät[int(input('Mille kentälle seuraavaksi? ')) - 1]
    #kiviarpa(kivet, kerätyt_kivet)
    #kivet_pelissä(kivet, kerätyt_kivet)
    return tulos

#Eli kun saapuu kentälle, arvotaan ensin löytyykö kivi.
#def kenttäarpa(kivet):
 #   if kivet >0:
 #       tulos = random.randint(0, 1)
 #   return
#def kivisekoilu(kivet):

   # kivet_pelissä(kivet, kerätyt_kivet)
   # return
#Jos on, arvotaan toisella funktiolla sen "arvo", tässä 1-6 (voi muuttaa vielä).

def kivisekoilu():
    kiviarpa
    return

def kiviarpa(kivet, kerätyt_kivet):
    tulos = random.randint(1,6)
    if tulos == 6:
        kivet = kivet - 1

        kerätyt_kivet = kerätyt_kivet + (random.randint(1,6) * 2)
        print('Löysit suuren kiven!')

    if tulos in range(1, 6):
        kivet = kivet - 1

        kerätyt_kivet = kerätyt_kivet + random.randint(1,6)
        print('Löysit kiven!')

    if tulos == 0:
        print('Kentällä ei ole kiveä.')

    return kivet, kerätyt_kivet


def kivet_pelissä(kivet, kerätyt_kivet):
    if kivet > 1:
        print(f'Pelissä on vielä  {kivet} kiveä.')
    if kivet == 1:
        print(f'Pelissä on vielä {kivet} kivi.')
    if kivet == 0:
        print('Lol.')

    print(f'Kivien kerätty arvo: {kerätyt_kivet}.')
    print()
    return

#    PÄÄOHJELMA

yhteys = mysql.connector.connect(
      #  host='127.0.0.1',
      #  port=3306,
        database='flight_game',
        user='python',
        password='1232',
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

print('Hyvä peli se on.')
'''
print('...')
print(' Ilmasto lämpenee lämpenemistään ja sen estämiseen kykenevät tahot'
'\n vain tahkoavat rahaa ympäristön kustannuksella. On aika tarttua'
'\n toimeen elinympäristön puolustamiseksi!')
input('')
print(' Ab Ruksi Oy Corporationin toimitusjohtaja velho Suur-Ruksi ylläpitää'
'\n portaaleja ympäri taiattoman maailman lentokenttiä adakiittimanaseoksesta'
'\n louhituilla kivillä, joiden korruptoitunut taikaenergia saastuttaa niin'
'\n lähiympäristöä kuin koko kotiplaneettaa.')
input('')
print(' Vaan velho Suur-Ruksi on saanut vihiä aikeistasi anastaa kivet ja puhdistaa'
'\n ne saastuttavasta energiasta ennen kuin jaat ne tarvitseville.'
'\n Tästä alkaa kilpajuoksu kivien luo!')
input('')
print(' Pystyt teleporttaamaan tukikohdastasi yhdelle ennalta määrittelemättömälle'
'\n kentälle, jonka jälkeen sinulla on rajattu määrä energiaa matkustaa portaalien'
'\n välillä. Kerättyäsi adakiitin, et voi enää palata kyseiselle kentälle.'
'\n Voit käyttää myös adakiitteja matkustamiseen, mutta muista että ne kuormittavat'
'\n ympäristöä. Harkitse tarkkaan liikkeesi!'
'\n')
'''
def alku():

    ala = input('Oletko valmis seikkailuun? (k/e) ')

    if ala == 'e':
        print('\n '
              '\nNojoo väsyttää kyl aika paljo, ehkä huomenna...')
    if ala == 'k':
        print('\n '
            '\nMatkaan!')
    else:
        alku()

alku()

#Pelaajan alkukentän arvonta
sijainti_icao = pelattavat_kentät[random.randint(0,89)]
#print(f'Tässä on pelaajan kentän ICAO-koodi: {sijainti_icao}')
sijainti_nimi = []
pelaajan_sijainnin_nimi(sijainti_icao)

#liikkuminen ja kivet
liikkeet = 4 #alussa
kivet = 10
kerätyt_kivet = 0
kerätyt_pisteet = 0

pelikoordinaatit = pelaajan_koordinaatit(sijainti_icao)
print()
#print(f'Olet kentällä {sijainti_nimi[0]}.')
print()

seuraavat_kentät = []
seuraavien_kenttien_nimet = []


while kivet != 0:
    peliluuppi()
    kivet, kerätyt_kivet = kiviarpa(kivet, kerätyt_kivet)
    #kivet_pelissä(kivet, kerätyt_kivet)
    sijainti_icao = seuraava_kohde()
    #print(sijainti_icao)
    pelaajan_sijainnin_nimi(sijainti_icao)
    #print(sijainti_nimi[0])
    pelattavat_kentät.remove(sijainti_icao)

    #kenttäarpa(kivet, kerätyt_kivet)


#tulos = kenttäarpa(kivet, kerätyt_kivet)










