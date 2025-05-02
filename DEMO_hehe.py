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
pelattavat_kentät_lista_2=[]
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

class Pelaaja:
    def __init__(self, sijainti, kivet):
        self.sijainti = sijainti
        self.kivet = kivet


    def koordinaatit(self, icao):
        sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{icao}'"
        # print(sql)
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos_kordinaatit = kursori.fetchone()
        kursori.close()
        return tulos_kordinaatit if tulos_kordinaatit else (0, 0)
    def sijainnin_nimi(self, icao):
        sql = f"SELECT name FROM airport WHERE ident = '{icao}'"
        # print(sql)
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos_nimi = kursori.fetchall()
        if tulos_nimi:
           for rivi in tulos_nimi:
               nimi = rivi[0]
        return nimi
    def seuraava_kohde(self):
        while True:
            try:
                print("")
                valinta = int(input('Mille kentälle seuraavaksi? ')) - 1
                if 0 <= valinta < len(seuraavat_kentät):
                    self.sijainti = seuraavat_kentät[valinta]
                    return seuraavat_kentät[valinta]
                else:
                    print("Virheellinen valinta, yritä uudelleen.")
            except ValueError:
                print("Syötä numero.")

    def kiviarpa(self):
        tulos_kiviarpa = random.randint(1, 6)
        if tulos_kiviarpa == 6:
            pöö = (random.randint(1, 6) * 2)
            print("")
            print('Löysit suuren adakiitin!')
            print(f"Sen arvo on: {pöö}")
        elif tulos_kiviarpa in range(3, 6):
            pöö = random.randint(1, 6)
            print("")
            print('Löysit adakiitin!')
            print(f"Sen arvo on: {pöö}")
        elif tulos_kiviarpa < 3:
            pöö = 0
            print("")
            print('Kentällä ei ole adakiittiä.')
        return pöö

class Vihollinen(Pelaaja):
    def __init__(self, sijainti, kivet):
        super().__init__(sijainti, kivet)

    def vihollinen_liikkuu(self):
        while True:
            try:
                print("")
                print("Vihollinen liikkuu!")
                valinta = random.choice(seuraavat_kentät)
                if valinta in seuraavat_kentät:
                    self.sijainti = valinta
                    pelattavat_kentät_lista_2.remove(valinta)
                    return
            except ValueError:
                print("vihollinen ei osaa :(.")

    def vihollisen_arpa(self):
        tulos_kiviarpa = random.randint(1, 6)
        if tulos_kiviarpa == 6:
            pöö = (random.randint(1, 6) * 2)
        elif tulos_kiviarpa in range(3, 6):
            pöö = random.randint(1, 6)
        elif tulos_kiviarpa < 3:
            pöö = 0
        return pöö


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

            if 0 < distance.distance(pelikoordinaatit, (seur_lat, seur_lon)).km < ((liikkeet + p.kivet) * 500):
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
def sijainti_nimeksi(si):
    sql = f"SELECT name FROM airport WHERE ident = '{si}'"
    # print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if tulos:
        for rivi in tulos:
            sijainti = rivi[0]
    return sijainti
def peliluuppi1():
    paikka = sijainti_nimeksi(p.sijainti)
    print()
    print(f'Olet saapunut kentälle: {paikka}')
    print("")
    print("Löysit täältä adakiitin jonka arvo on 5! ")
    print()
    pelattavat_kentät_lista_2.remove(p.sijainti)
    p.koordinaatit(sijainti_icao1)
    matkustettavat_kentät()
    listaus()
    kenttäluettelo()
    sijainti_nimi.clear()
    return
def peliluuppi2(eih):
    paikka = sijainti_nimeksi(p.sijainti)
    print()
    print(f'Olet saapunut kentälle: {paikka}')
    print()
    if p.sijainti in pelattavat_kentät_lista_2:
        pelattavat_kentät_lista_2.remove(p.sijainti)
    xx = p.kiviarpa()
    xy = eih + xx
    if xy > 50:
        print("Kivien kerätty arvo on 50!")
        print("")
    if xy <= 50:
        print(f'Kivien kerätty arvo: {xy}.')
        print("")
    kivi_väli_lauseet(xy)
    if xx == 0:
        input(f"1. {random.choice(vastausvaihtoehdot_neg1)} "
                f"\n2. {random.choice(vastausvaihtoehdot_neg2)}"
                "\n: ")
    else:
        input(f"1. {random.choice(vastausvaihtoehdot_pos1)} "
                    f"\n2. {random.choice(vastausvaihtoehdot_pos2)}"
                    "\n: ")
    sijainti_nimi.clear()
    seuraavat_kentät.clear()
    seuraavien_kenttien_nimet.clear()
    p.koordinaatit(sijainti_icao1)
    matkustettavat_kentät()
    listaus()
    return xy


def heita_noppaa(maara, ymp):
    return sum(random.randint(1, 6) for i in range(maara + ymp))

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
    input(' Paina mitä vain jatkaaksesi: ')
    print(f" Hei {pelaajan_nimi}! Muinaiset tietäjälahkot ovat sodassa! Vanhat lahkot, joiden tavoite on ilmastonmuutos,"
    "\n ovat kaavailleet suunnitelman tuodakseen lopun konfliktille:"
    "\n Suur-Velho Kaik-Oo-Koolle on annettu tehtäväksi kerätä kaikki adakiittikivet maailmasta"
    "\n voittaakseen velhojen taisto.")
    input('')
    print(" Uudet lahkot ovat päättäneet pysäyttää heidän aikeensa"
    "\n lähettämällä oman valittunsa keräämään kaikki kivet ensin."
    "\n Toteuttaakseen tämän tehtävän, uudet lahkot valitsivat: sinut!")
    input('')
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
def loppu():
    ö = 0
    pisteet = 0
    while ö < p.kivet:
        pisteet = pisteet + (random.randint(1, 6))
        ö = ö + 1
    return pisteet
#    PÄÄOHJELMA
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

sijainti_icao1 = random.choice(pelattavat_kentät_lista_2)
sijainti_icao2 = random.choice(pelattavat_kentät_lista_2)
sijainti_nimi = []
p = Pelaaja(sijainti_icao1, 5)
v = Vihollinen(sijainti_icao2, 5)
#
liikkeet = 4
kierrokset = 1
ympäristöpisteet = 30

pelikoordinaatit = p.koordinaatit(sijainti_icao1)
p.sijainnin_nimi(sijainti_icao1)

print()


peli_alkaa()

while kierrokset < 2:
    peliluuppi1()
    p.sijainnin_nimi(sijainti_icao1)
    v.vihollinen_liikkuu()

    kierrokset = kierrokset + 1

while p.kivet < 50 and v.kivet < 50 and ympäristöpisteet > 0:


    print("\n1. Lennä seuraavalle kentälle")
    print("2. Jää kentälle (säästät ympäristöä, saat +3 ympäristöpistettä)")
    valinta = input("Valintasi: ")

    if valinta == '1':
        ympäristöpisteet -= 1
        kenttäluettelo()
        sijainti_icao1 = p.seuraava_kohde()
        p.kivet = peliluuppi2(p.kivet)
    elif valinta == '2':
        print("Päätit jäädä paikalleen. Ympäristö kiittää sinua.")
        ympäristöpisteet += 3
    else:
        print("Virheellinen valinta.")
        continue
    v.vihollinen_liikkuu()
    v.kivet += v.vihollisen_arpa()
    if sijainti_icao1 in pelattavat_kentät_lista_2:
        pelattavat_kentät_lista_2.remove(sijainti_icao1)
    ympäristöpisteet -= 1

    print(f"\nYmpäristöpisteet: {ympäristöpisteet}")
    print(f"Pisteesi: {p.kivet}\nVastustaja: {v.kivet}")


print("\n--- PELI PÄÄTTYY ---")

if ympäristöpisteet <= 0:
    print("")
    print("Ympäristöpisteet loppuivat! Nyt maailmaa kohtaa ilmastokatastrofi!")
    quit()
elif p.kivet >= 50:
    print("")
    print("Sait kasaan 50 adakiittipistettä!")
elif v.kivet >= 50:
    print("")
    print("Vastustajasi saavutti 50 pistettä!")

print(f"\nLopulliset pisteet: {pelaajan_nimi}: {p.kivet}, Vastustaja: {v.kivet}")
print("Nyt siirrytään loppukohtaamiseen, jossa nopanheitot ratkaisevat kaiken!\n")

pelaajan_heitoista = heita_noppaa(p.kivet, ympäristöpisteet)
vastustajan_heitoista = heita_noppaa(v.kivet, 0)

print(f"{pelaajan_nimi} heitti yhteensä {pelaajan_heitoista} pistettä.")
print(f"Vastustaja heitti yhteensä {vastustajan_heitoista} pistettä.")

if pelaajan_heitoista > vastustajan_heitoista:
    print("\nOnneksi olkoon, voitit pelin!!")
elif pelaajan_heitoista < vastustajan_heitoista:
    print("\nHävisit pelin. Vastustajasi oli tällä kertaa vahvempi.")
else:
    print("\nTasapeli!!")

pisteet = loppu()

def hae_id_koodi():
    sql = f"select id from peli where nimi = ('{pelaajan_nimi}')"
    # print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if tulos:
        for rivi in tulos:
            koodi = rivi[0]

    return koodi
highscore_id = hae_id_koodi()

def id_tauluun(id):
    sql = f"insert into highscore (id) values ('{id}')"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return
id_tauluun(highscore_id)

def pisteet_tauluun(nimi, p):
    sql = f"update highscore set pisteet = '{p}' where id = (select id from peli where nimi = '{nimi}')"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return
pisteet_tauluun(pelaajan_nimi, pisteet)

print(f"Sait {pisteet} pistettä!")

def highscore():
    sql = f"select peli.nimi, highscore.pisteet from peli, highscore where highscore.id = peli.id group by peli.nimi order by highscore.pisteet desc, pisteet asc limit 10"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if tulos:
        for rivi in tulos:
            print(f'Pelaaja: {rivi[0]} Pisteet: {rivi[1]}')
    return

print()
highscore()