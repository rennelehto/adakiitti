import random
def siirtyy(kohde):
    sql = f"update peli set location = (select ident from airport where name = {kohde}) where nimi = 'Pelaaja';"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return

def sijainti():
    sql = f"select name from airport where ident in (select from nimi where nimi = 'Pelaaja');"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    print(f"Sijaintisi on {tulos}.")
    return

def vihollisvalinta():
    tulos = seuraavat_kentät[random.randint(0, (len(seuraavat_kentät) - 1))]
    return tulos

def vih_sijainnin_nimi(sijainti_icao):
    sql = f"SELECT name FROM airport WHERE ident = '{sijainti_icao}'"
        # print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
       for rivi in tulos:
           vih_sijainti_nimi.append(rivi[0])
    return tulos

while kivet != 0:
    peliluuppi()
    kivet, kerätyt_kivet = kiviarpa(kivet, kerätyt_kivet)
    #kivet_pelissä(kivet, kerätyt_kivet)
    sijainti_icao = seuraava_kohde()
    #print(sijainti_icao)
    pelaajan_sijainnin_nimi(sijainti_icao)
    #print(sijainti_nimi[0])
    pelattavat_kentät.remove(sijainti_icao)
    vih_sijainti_icao = vihollisvalinta()
    #print(vih_sijainti_icao)
    vih_sijainnin_nimi(vih_sijainti_icao)
    #print(vih_sijainti_nimi[0])
    pelattavat_kentät.remove(vih_sijainti_icao)