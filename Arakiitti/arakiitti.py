
def nopanheitto():
    return random.randint(1, 6)  # Heittää nopan (1-6)

#pelaajan päätökset, jotka vaikuttavat pisteisiin:
def pelaajan_toiminta(matkustaako, ympäristöpisteet, vastustajan_siirrot):
    if matkustaako:
        ympäristöpisteet.append(-1)  #matkustaminen vähentää yhden pisteen
        vastustajan_siirrot += 1
    else:
        ympäristöpisteet.append(3)  # Jos ei matkusta, saa kolme pistettä

    return ympäristöpisteet, vastustajan_siirrot

#vastustajan liike
def vastustajan_liike(ympäristöpisteet, vastustajan_siirrot):
    for i in range(vastustajan_siirrot):
        ympäristöpisteet.append(-1)  # Vastustaja liikkuu joka vuorolla -1 piste
    return ympäristöpisteet

#rennen kivien arpominen: pelaajan kivet lisätään listaan
    kivet_yhteensä.append(kivet)

#pelin loppupisteet
def laske_loppupisteet(kivet_yhteensä, ympäristöpisteet):
    return sum(kivet_yhteensä) + sum(ympäristöpisteet)

#noppaa heitetään pelaajan loppupisteiden määrän verran:
def heitä_nopat(loppupisteet):
    return sum(nopanheitto() for i in range(loppupisteet))

def pelaa(matkustuspäätökset):
    kivet_yhteensä = []
    ympäristöpisteet = [20]  # Pelaajalla aluksi 20 ympäristöpistettä
    vastustajan_siirrot = 0

    for matkustaako in matkustuspäätökset:
        ympäristöpisteet, vastustajan_siirrot = pelaajan_toiminta(matkustaako, ympäristöpisteet, vastustajan_siirrot)
        ympäristöpisteet = vastustajan_liike(ympäristöpisteet, vastustajan_siirrot)
        kivet_yhteensä = kivet(kivet_yhteensä)  #Rennen koodiin

    loppupisteet = laske_loppupisteet(kivet_yhteensä, ympäristöpisteet)
    print(f'Kerätyt kivet: {kivet_yhteensä}')
    print(f'Kerätyt ympäristöpisteet: {sum(ympäristöpisteet)}')
    print(f'Pelin loppupisteet: {loppupisteet}')

    yhteispisteet = heitä_nopat(loppupisteet)  # Heitetään nopat loppupisteiden mukaan
    print(f'Yhteispisteesi: {yhteispisteet}')
