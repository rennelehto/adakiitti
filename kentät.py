def siirtyy(kohde):
    sql = f"update game set location = (select ident from airport where name = {kohde}) where screen_name = 'Pelaaja';"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return

def sijainti():
    sql = f"select name from airport where ident in (select from screen_name where screen_name = 'Pelaaja');"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    print(f"Sijaintisi on {tulos}.")
    return