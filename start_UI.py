import mysql.connector
import random

#Näihin listoihin tulee kenttien "Ident" -tunnukset.

#Euroopassa on 118 suurta kenttää.

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

#Pohjois-Amerikassa on 112 suurta kenttää.
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

yhteys = mysql.connector.connect(
       # host='127.0.0.1',
      #  port=3306,
        database='flight_game',
        user='root',
        password='gr0ups',
        autocommit=True)

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
    valitut_kentätEU.append(lista_kentistäEU[random.randint(0, 117)])
    määräEU=määräEU+1

valitut_kentätAF=[]
määräAF = 0
while määräAF < 15:
    valitut_kentätAF.append(lista_kentistäAF[random.randint(0, 44)])
    määräAF=määräAF+1

valitut_kentätAS=[]
määräAS = 0
while määräAS < 15:
    valitut_kentätAS.append(lista_kentistäAS[random.randint(0, 136)])
    määräAS=määräAS+1

valitut_kentätOC=[]
määräOC = 0
while määräOC < 15:
    valitut_kentätOC.append(lista_kentistäOC[random.randint(0, 16)])
    määräOC=määräOC+1

valitut_kentätNA=[]
määräNA = 0
while määräNA < 15:
    valitut_kentätNA.append(lista_kentistäNA[random.randint(0, 107)])
    määräNA=määräNA+1

valitut_kentätSA=[]
määräSA = 0
while määräSA < 15:
    valitut_kentätSA.append(lista_kentistäNA[random.randint(0, 21)])
    määräSA=määräSA+1

#print(valitut_kentätEU)
#print(f' Euroopan kenttiä listassa {len(valitut_kentätEU)} kpl.')
#print(f' Afrikan kenttiä listassa {len(valitut_kentätAF)} kpl.')
#print(f' Aasian kenttiä listassa {len(valitut_kentätAS)} kpl.')
#print(f' Oseanian kenttiä listassa {len(valitut_kentätOC)} kpl.')
#print(f' Pohjois-Amerikan kenttiä listassa {len(valitut_kentätNA)} kpl.')
#print(f' Etelä-Amerikan kenttiä listassa {len(valitut_kentätSA)} kpl.')

#Tässä valitut kentät yhdistyy yhdeksi listaksi kenttiä, joille pelaajalla on pääsy.
pelattavat_kentät=[]
pelattavat_kentät.extend(valitut_kentätEU)
pelattavat_kentät.extend(valitut_kentätAF)
pelattavat_kentät.extend(valitut_kentätAS)
pelattavat_kentät.extend(valitut_kentätOC)
pelattavat_kentät.extend(valitut_kentätNA)
pelattavat_kentät.extend(valitut_kentätSA)
print()
#print(f'✈ Pelattavia kenttiä {len(pelattavat_kentät)} kpl. ✈')
print()

#Tästä eteenpäin kokeilua
def kenttähaku():
    sql = f'SELECT airport.name, country.name FROM airport, country WHERE airport.iso_country = country.iso_country and ident = "{pelattavat_kentät[random.randint(0, 89)]}"'
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print('Airport name: ' + rivi[0] + '.')
            print('Location: ' + rivi[1] + '.')
    return

kenttähaku()
print()

pelaajan_nimi = input("Ole hyvä ja syötä nimesi: ")
def pelaajat(nimi):
    sql = f"insert into peli (nimi) value {pelaajan_nimi}"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return pelaajan_nimi


def peli_alkaa():
    print(" ")
    print("                                                                                         Adakite--Adakiitti")
    print(" ")
    print("Tehtäväsi on pelastaa maailma ilkeältä velholta, joka pyrkii keräämään maagisia kiviä joilla hän haluaa aiheuttaa ilmastokatastrofin.")

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
    mantere = int(input(                # mantereen valinta
                "\n1. Eurooppa "
                "\n2. Aasia"
                "\n3. Oseania "
                "\n4. Afrikka "
                "\n5. Etelä-Amerikka"
                "\n6. Pohjois-Amerikka "
                "\n: "))




    #pelattavat_kentät=["Helsinki-Vantaa airport", "JFK international airport", "LAX international airport", "Arlanda airport","London Heathrow airport"]



    numero = 1
    while mantere in range (0,7):
        if mantere == 1:
            print("")
            print("Euroopan kentät: ")
            print(" ")
            for kenttä in valitut_kentätEU:
                print(f"{numero}. {kenttä}.")
                numero = numero + 1
            break
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

#pelaajat(pelaajan_nimi)
peli_alkaa()
alkupiste = int(input(": "))
#if alkupiste in pelattavat_kentät:





