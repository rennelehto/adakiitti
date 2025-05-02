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

seuraavat_kentät = []
seuraavien_kenttien_nimet = []
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

            while len(pelattavat_kentät_lista_2) < 15*y:
                x = lista_kentistä[random.randint(1, len(lista_kentistä)) - 1]
                if x not in pelattavat_kentät_lista_2:
                    pelattavat_kentät_lista_2.append(x)
            lista_kentistä.clear()
            y+=1
    return



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

vastausvaihtoehdot_pos1 = ["Jee!","Hienoa!","Mahtavaa!","Upeaa!","Oi onnen päivää!"]
vastausvaihtoehdot_pos2 = ["Voisin itkeä ilosta :')","Ou jee!","Erinomaista!","Hieno homma!",":)"]
vastausvaihtoehdot_neg1 = ["Voi ei! :(","Höh..","EIIIII!!",":(","Epäreilua..","Ei voi olla totta..."]
vastausvaihtoehdot_neg2 = ["Himputti..!!","No onpa kiva","Millon pääsee kotiin...","Yhyy...","Taasko.."]
def kenttäluettelo():
    x = 0
    print("")
    print('Tässä kentät joille voit matkustaa:')
    print("")
    for x in range(min(20, len(seuraavien_kenttien_nimet))):
        print(f'{x + 1}. {seuraavien_kenttien_nimet[x]}')
        x = x + 1
    return
def kivi_väli_lauseet(xy):
    if xy == 20 or xy == 21:
        print("---------------------------------------------------------------------------")
        print("Olet jo puolessa välissä! Jaksa vielä vähän. ")
        print("---------------------------------------------------------------------------")
    if xy == 23 or xy == 24:
        print("---------------------------------------------------------------------------")
        print("Tiesitkö että maailmassa on noin 1.5 miljardia lehmää?")
        print("---------------------------------------------------------------------------")
    if xy == 25 or xy == 26:
        print("---------------------------------------------------------------------------")
        print("Tiesitkö että lehmillä voi olla paras ystävä, ja ne stressaantuvat jos heidät erotetaan toisistaan. ")
        print("---------------------------------------------------------------------------")
    if xy == 28 or xy == 29:
        print("---------------------------------------------------------------------------")
        print("Tiesitkö että lehmät katsovat auringonlaksua vain sen kauneuden vuoksi? ")
        print("---------------------------------------------------------------------------")
    else:
        return
    return

def peliluuppi1():
    print()
    print(f'Olet saapunut kentälle: {sijainti_nimi[0]}')
    print("")
    print("Löysit täältä adakiitin jonka arvo on 5! ")
    print()
    pelaajan_koordinaatit(sijainti_icao)
    matkustettavat_kentät()
    listaus()
    kenttäluettelo()
    sijainti_nimi.clear()
    return
def peliluuppi2(eih):
    print()
    print(f'Olet saapunut kentälle: {sijainti_nimi[0]}')
    print()
    xx = kiviarpa()
    xy = eih + xx
    if xy > 40:
        print("Kivien kerätty arvo on 40!")
        print("")
    if xy <= 40:
        print(f'Kivien kerätty arvo: {xy}.')
        print("")
    kivi_väli_lauseet(xy)
    if xx == 0:
        vastaus = input(f"1. {random.choice(vastausvaihtoehdot_neg1)} "
                    f"\n2. {random.choice(vastausvaihtoehdot_neg2)}"
                    "\n: ")
    else:
        vastaus = input(f"1. {random.choice(vastausvaihtoehdot_pos1)} "
                        f"\n2. {random.choice(vastausvaihtoehdot_pos2)}"
                        "\n: ")
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
            print("")
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




kenttäkysely()

print(" ")
print("                                                                                         Adakite--Adakiitti")
pelaajan_nimi = input("Ole hyvä ja syötä nimesi: ").capitalize()
def pelaajat():
    sql = f"insert into peli (nimi) values ('{pelaajan_nimi}')"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return
pelaajat()
def peli_alkaa():
    print(" ")
    print("▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"
        "\n▒▒▒▒▒█▒▒▒███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"
        "\n▒▒▒▒▒▒▒▒█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒█▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒█▒▒▒▒█▒▒▒█▒▒█▒▒█▒▒█▒▒█▒▒█▒▒█▒▒▒█▒█▒█▒█▒█▒█▒█▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"
        "\n▒▒▒▒▒▒██████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒█▒▒▒▒▒▒▒▒▒▒█▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒█▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒█▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"
        "\n▒▒▒▒███████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒█▒▒▒▒▒▒▒▒▒█▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒█▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒█▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"
        "\n▒▒▒▒▒▒██▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒█▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒█▒▒▒▒▒▒▒▒█▒▒▒▒█▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"
        "\n▒▒▒▒▒▒█▒▒▒█▒▒█▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒█▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒█▒▒█▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒█▒█▒█▒█▒█▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"
        "\n▒▒▒▒▒▒▒██████████▒▒▒▒▒▒▒▒▒▒▒▒▒███▒▒▒██▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒█▒█▒█▒█▒█▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒█▒█▒█▒▒█▒█▒█▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"
        "\n▒▒▒▒▒▒▒▒▒██████▒▒▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒█▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒█▒▒▒▒▒▒▒▒█▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒█▒▒█▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"
        "\n▒▒▒▒▒███▒▒████▒▒███▒▒▒▒▒█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒█▒▒▒▒▒▒▒█▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒█▒▒▒▒█▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"
        "\n▒▒▒▒▒▒█▒▒▒▒██▒▒▒▒█▒▒▒▒███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒█▒▒▒▒▒▒█▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒█▒▒▒▒▒▒█▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"
        "\n▒▒▒▒▒██▒█▒▒▒▒▒█▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒█▒█▒█▒█▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒█▒▒▒▒▒▒▒▒█▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒█▒█▒█▒█▒█▒█▒█▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"
        "\n▒▒▒████▒▒█▒█▒█▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"
        "\n▒▒▒▒▒▒█▒▒▒█▒█▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"
        "\n▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"
        "\n▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"
        "\n▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"
        "\n▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"
        "\n▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"
        "\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    väli = input(' Paina mitä vain jatkaaksesi: ')
    print(f" Hei {pelaajan_nimi}! Muinaiset tietäjälahkot ovat sodassa! Vanhat lahkot, joiden tavoite on ilmastonmuutos,"
    "\n ovat kaavailleet suunnitelman tuodakseen lopun konfliktille:"
    "\n Suur-Velho Kaik-Oo-Koolle on annettu tehtäväksi kerätä kaikki adakiittikivet maailmasta"
    "\n voittaakseen velhojen taisto.")
    väli = input('')
    print(" Uudet lahkot ovat päättäneet pysäyttää heidän aikeensa"
    "\n lähettämällä oman valittunsa keräämään kaikki kivet ensin."
    "\n Toteuttaakseen tämän tehtävän, uudet lahkot valitsivat: sinut!")
    väli2 = input('')
    print("\n Nyt, sinun kuuluu kerätä niin paljon adakiittitaikakiviä kuin voit,"
    "\n käyttämällä maailman lentokenttiä kiintopisteinä ja"
    "\n pysäyttää Kaik-Oo-Koo ennen kuin hän ehtii tuhota ilmaston! ")

    Pelin_aloitus = input(                          #Vastaus valinta
                "\n1. Asia selvä. "
                "\n2. En halua. "
                "\n: ")
    while Pelin_aloitus == (""):
        print("--------------------------------------------------")
        print("Error,please try again")
        print("--------------------------------------------------")
        Pelin_aloitus = input(  # Vastaus valinta
            "\n1. Asia selvä. "
            "\n2. En halua. "
            "\n: ")
    while int(Pelin_aloitus) in [1,2]:
        if int(Pelin_aloitus) == 1:
            print("--------------------------------------------------")
            print("Asia selvä.")
            print("--------------------------------------------------")
            break
        if int(Pelin_aloitus) == 2:
            print("--------------------------------------------------")
            print("Valitettavasti et saa jatkaa.")
            print("--------------------------------------------------")
            quit()
        if int(Pelin_aloitus) not in [1,2]:
            print("--------------------------------------------------")
            print("Yritä uudelleen.")
            print("--------------------------------------------------")
            Pelin_aloitus = input(  # Vastaus valinta
                "\n1. Asia selvä. "
                "\n2. En halua. "
                "\n: ")

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
def demoloppu():
    ö = 0
    pisteet = 0
    while ö < kerätyt_kivet:
        pisteet = pisteet + (random.randint(1, 6))
        ö = ö + 1
    return pisteet


pisteet = demoloppu()
print(f"Sait {pisteet} pistettä!")