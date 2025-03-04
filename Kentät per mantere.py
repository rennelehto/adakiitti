import mysql.connector
import random

#Näihin listoihin tulee kenttien "Ident" -tunnukset.

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

yhteys = mysql.connector.connect(
      #  host='127.0.0.1',
      #  port=3306,
        database='flight_game',
        user='python',
        password='1232',
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
    maa=lista_kentistäAF[random.randint(0, 44)]
    if maa not in lista_kentistäAF:
        valitut_kentätAF.append(lista_kentistäAF[random.randint(0, 44)])
        määräAF=määräAF+1

valitut_kentätAS=[]
määräAS = 0
while määräAS < 15:
    maa = lista_kentistäAS[random.randint(0, 44)]
    if maa not in lista_kentistäAS:
        valitut_kentätAS.append(lista_kentistäAS[random.randint(0, 44)])
        määräAS = määräAS + 1

valitut_kentätOC=[]
määräOC = 0
while määräOC < 15:
    maa = lista_kentistäOC[random.randint(0, 44)]
    if maa not in lista_kentistäOC:
        valitut_kentätOC.append(lista_kentistäOC[random.randint(0, 44)])
        määräOC = määräOC + 1

valitut_kentätNA=[]
määräNA = 0
while määräNA < 15:
    maa = lista_kentistäNA[random.randint(0, 44)]
    if maa not in lista_kentistäNA:
        valitut_kentätNA.append(lista_kentistäNA[random.randint(0, 44)])
        määräNA = määräNA + 1

valitut_kentätSA=[]
määräSA = 0
while määräSA < 15:
    maa = lista_kentistäSA[random.randint(0, 44)]
    if maa not in lista_kentistäSA:
        valitut_kentätSA.append(lista_kentistäSA[random.randint(0, 44)])
        määräSA = määräSA + 1

#print(valitut_kentätEU)
print(f'{'✈':6} Euroopan kenttiä listassa {len(valitut_kentätEU)} kpl.')
print(f'{'✈':6} Afrikan kenttiä listassa {len(valitut_kentätAF)} kpl.')
print(f'{'✈':6} Aasian kenttiä listassa {len(valitut_kentätAS)} kpl.')
print(f'{'✈':6} Oseanian kenttiä listassa {len(valitut_kentätOC)} kpl.')
print(f'{'✈':6} Pohjois-Amerikan kenttiä listassa {len(valitut_kentätNA)} kpl.')
print(f'{'✈':6} Etelä-Amerikan kenttiä listassa {len(valitut_kentätSA)} kpl.')

#Tässä valitut kentät yhdistyy yhdeksi listaksi kenttiä, joille pelaajalla on pääsy.
pelattavat_kentät=[]
pelattavat_kentät.extend(valitut_kentätEU)
pelattavat_kentät.extend(valitut_kentätAF)
pelattavat_kentät.extend(valitut_kentätAS)
pelattavat_kentät.extend(valitut_kentätOC)
pelattavat_kentät.extend(valitut_kentätNA)
pelattavat_kentät.extend(valitut_kentätSA)
print()
print(f'{'✈ ':6}✈      ✈      ✈ {'✈':>6}')
print(f'✈ Pelattavia kenttiä {len(pelattavat_kentät)} kpl. ✈')
print(f'{'✈ ':6}✈      ✈      ✈ {'✈':>6}')
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
print(f'{'✈':6} Bon voyage! {'✈':>6}')

