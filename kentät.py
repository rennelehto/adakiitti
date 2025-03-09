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
    tulos = random.randint(len(seuraavat_kentät - 1))
    return tulos