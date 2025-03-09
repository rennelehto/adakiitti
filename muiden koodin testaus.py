import mysql.connector
import random
from geopy import distance

#                             MUISTAKAA VAIHTAA OMAT TIETOKANTATUNNUKSET!!

#Näihin listoihin tulee nyt kenttien nimet.

#Euroopassa on 118 suurta kenttää.

yhteys = mysql.connector.connect(
      #  host='127.0.0.1',
      #  port=3306,
        database='flight_game',
        user='python',
        password='1232',
        autocommit=True)

lista_kentistäEU=[]
def kenttäkyselyEU():
    sql = f"select airport.name from airport, country where airport.iso_country = country.iso_country and country.continent = 'EU' and airport.type = 'large_airport'"
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
    sql = f"select airport.name from airport, country where airport.iso_country = country.iso_country and country.continent = 'AF' and airport.type = 'large_airport'"
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
    sql = f"select airport.name from airport, country where airport.iso_country = country.iso_country and country.continent = 'AS' and airport.type = 'large_airport'"
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
    sql = f"select airport.name from airport, country where airport.iso_country = country.iso_country and country.continent = 'OC' and airport.type = 'large_airport'"
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
    sql = f"select airport.name from airport, country where airport.iso_country = country.iso_country and country.continent = 'NA' and airport.type = 'large_airport'"
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
    sql = f"select airport.name from airport, country where airport.iso_country = country.iso_country and country.continent = 'SA' and airport.type = 'large_airport'"
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            lista_kentistäSA.append(rivi[0])
    return


#Nämä funktiot tuo kaikki valittujen mantereiden kentät omiksi listoikseen.
kenttäkyselyEU()
kenttäkyselyAF()
kenttäkyselyAS()
kenttäkyselyOC()
kenttäkyselyNA()
kenttäkyselySA()
#print(lista_kentistä)

#Seuraavat pätkät arpoo 15 kenttää per mantere listalle.
valitut_kentätEU=[]
määräEU = 0
while määräEU < 15:
    maa=lista_kentistäEU[random.randint(0, 116)]
    valitut_kentätEU.append(maa)
    määräEU=määräEU+1

valitut_kentätAF=[]
määräAF = 0
while määräAF < 15:
    maa=lista_kentistäAF[random.randint(0, 44)]
    if maa not in valitut_kentätAF:
        valitut_kentätAF.append(maa)
        määräAF=määräAF+1

valitut_kentätAS=[]
määräAS = 0
while määräAS < 15:
    maa = lista_kentistäAS[random.randint(0, 36)]
    if maa not in valitut_kentätAS:
        valitut_kentätAS.append(maa)
        määräAS = määräAS + 1

valitut_kentätOC=[]
määräOC = 0
while määräOC < 15:
    maa = lista_kentistäOC[random.randint(0, 16)]
    if maa not in valitut_kentätOC:
        valitut_kentätOC.append(maa)
        määräOC = määräOC + 1

valitut_kentätNA=[]
määräNA = 0
while määräNA < 15:
    maa = lista_kentistäNA[random.randint(0, 107)]
    if maa not in valitut_kentätNA:
        valitut_kentätNA.append(maa)
        määräNA = määräNA + 1

valitut_kentätSA=[]
määräSA = 0
while määräSA < 15:
    maa = lista_kentistäSA[random.randint(0, 21)]
    if maa not in valitut_kentätSA:
        valitut_kentätSA.append(maa)
        määräSA = määräSA + 1

#Tässä valitut kentät yhdistyy yhdeksi listaksi kenttiä, joille pelaajalla on pääsy.

pelattavat_kentät=[]
pelattavat_kentät.extend(valitut_kentätEU)
pelattavat_kentät.extend(valitut_kentätAF)
pelattavat_kentät.extend(valitut_kentätAS)
pelattavat_kentät.extend(valitut_kentätOC)
pelattavat_kentät.extend(valitut_kentätNA)
pelattavat_kentät.extend(valitut_kentätSA)

#tähän loppuu pelattavien kenttien valinta

#pelaaja syöttää nimensä


def pelaajat():
    nimimerkki = input("Ole hyvä ja syötä nimesi: ")
    sql = f"insert into peli (nimi) values ('{nimimerkki}')"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return





pelaajan_nimi = input("Ole hyvä ja syötä nimesi: ")
#def pelaajat():
    #sql = f"insert into peli (nimi) values ('{pelaajan_nimi}')"
    #kursori = yhteys.cursor()
    #kursori.execute(sql)
    #return


def peli_alkaa():
    print(" ")
    print("                                                                                         Adakite--Adakiitti")
    print(" ")
    print(f"Hei {pelaajan_nimi}! Tehtäväsi on pelastaa maailma ilkeältä velholta, joka pyrkii keräämään maagisia kiviä joilla hän haluaa aiheuttaa ilmastokatastrofin.")

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
        if Pelin_aloitus != 1 or 2 or 3:
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
    print("Ole hyvä ja valitse mantere josta haluat valita lentokentän josta aloittaa pelin: ")






valittumantere = []
def lentokenttä_mantere_lista():
    if mantere == 1:
        valittumantere.extend(valitut_kentätEU)
    if mantere == 2:
        valittumantere.extend(valitut_kentätAS)
    if mantere == 3:
        valittumantere.extend(valitut_kentätOC)
    if mantere == 4:
        valittumantere.extend(valitut_kentätAF)
    if mantere == 5:
        valittumantere.extend(valitut_kentätSA)
    if mantere == 6:
        valittumantere.extend(valitut_kentätNA)
    return valittumantere





    #pelattavat_kentät=["Helsinki-Vantaa airport", "JFK international airport", "LAX international airport", "Arlanda airport","London Heathrow airport"]
def lentokenttävalinta(mantere):
    numero = 1
    while mantere in range (0,7):
        if mantere == 1:
            print("")
            print("Euroopan kentät: ")
            print(" ")
            for kenttä in valitut_kentätEU:
                print(f"{numero}. {kenttä}.")
                numero = numero + 1
        if mantere == 2:
            print("")
            print("Aasian kentät: ")
            print(" ")
            for kenttä in valitut_kentätAS:
                print(f"{numero}. {kenttä}.")
                numero = numero + 1
            break
        if mantere == 3:
            print("")
            print("Oseanian kentät: ")
            print(" ")
            for kenttä in valitut_kentätOC:
                print(f"{numero}. {kenttä}.")
                numero = numero + 1
            break
        if mantere == 4:
            print("")
            print("Afrikan kentät: ")
            print(" ")
            for kenttä in valitut_kentätAF:
                print(f"{numero}. {kenttä}.")
                numero = numero + 1
            break
        if mantere == 5:
            print("")
            print("Etelä-Amerikan kentät: ")
            print("")
            for kenttä in valitut_kentätSA:
                print(f"{numero}. {kenttä}.")
                numero = numero + 1
            break
        if mantere == 6:
            print("")
            print("Pohjois-Amerikan kentät: ")
            print("")
            for kenttä in valitut_kentätNA:
                print(f"{numero}. {kenttä}.")
                numero = numero + 1
        break


peli_alkaa()

mantere = int(input(                # mantereen valinta
                "\n1. Eurooppa "
                "\n2. Aasia"
                "\n3. Oseania "
                "\n4. Afrikka "
                "\n5. Etelä-Amerikka"
                "\n6. Pohjois-Amerikka "
                "\n: "))
#pelaajat()
lentokenttävalinta(mantere)
lentokenttä_mantere_lista()
alkupiste = int(input(": "))
print(f"Olet kentällä : {valittumantere[alkupiste-1]}")


#airport.name is in = ('{pelattavat_kentät}')

'''Tässä on mallina vaan väärä kenttälista, saa kokeilla!
Tähän lisätään kans kertoimena kivien määrä, eli kolme kiveä = 3*500km jne'''
#TOIMII
#tekee listan pelattavista kentistä
def pelattavat():
    sql = f"select airport.ident from airport, country where airport.iso_country = country.iso_country and airport.name in ('{pelattavat_kentät}') and airport.type = 'large_airport'"
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
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE airport.name = ('{valittumantere[alkupiste-1]}')"
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    #if kursori.rowcount > 0:
       # for rivi in tulos:
       #     print(f"Pelaajan  koordinaatit: {rivi[0]}, {rivi[1]}.")
    return tulos

#TOIMII
#tämä hakee kentän koordinaatit
def kentän_etäisyys(Pip):
    sql = f"SELECT latitude_deg, longitude_deg from airport, country where airport.iso_country = country.iso_country and airport.ident = '{Pip}'"
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
    while k <= (len(pelattavat_kentät)-1):
        h = pelattavat_kentät[k]
        Pip = h
        seur = kentän_etäisyys(Pip)

        if distance.distance(sijainti, seur).km <= 500:
            seuraavat_kentät.append(h)
        k = k + 1
    return




pelattavat_kentät=[]
seuraavat_kentät=[]
pelattavat()
sijainti = pelaajan_sijainti()
matkustettavat_kentät()
print(f'Pelattavia kenttiä: {len(pelattavat_kentät)}')
print(f'Matkustettavia kenttiä: {len(seuraavat_kentät)}')

#def kentännimi(Pip):
 #   sql = f"SELECT airport.name from airport where airport.ident = ('{Pip}')"
  #  kursori = yhteys.cursor()
   # kursori.execute(sql)
    #tulos = kursori.fetchall()
    #return tulos