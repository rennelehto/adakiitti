import random

def nopanheitto():
    return random.randint(1, 6)

#pelaajan päätökset, jotka vaikuttavat pisteisiin
def pelaajan_toiminta(matkustaako, ympäristöpisteet, vastustajan_siirrot):
    if matkustaako:
        ympäristöpisteet.append(-1)  #matkustaminen vähentää yhden pisteen
        vastustajan_siirrot += 1  # Vastustaja liikkuu joka vuorolla
    else:
        ympäristöpisteet.append(3)  #jos pelaaja ei matkusta, saa hän kolme pistettä
    return ympäristöpisteet, vastustajan_siirrot

#vastustajan liike
def vastustajan_liike(ympäristöpisteet, vastustajan_siirrot):
    for i in range(vastustajan_siirrot):
        ympäristöpisteet.append(-1)  #vastustaja liikkuu joka vuorolla -1 piste
    return ympäristöpisteet

#Arvotaan löytyykö kentältä kiveä
def kenttäarpa():
    return random.randint(0, 6)

#arvotaan kiven arvo
def kiviarpa():
    return random.randint(1, 6)

#laske loppupisteet
def laske_loppupisteet(ympäristöpisteet, kivet_yhteensä):
    return sum(kivet_yhteensä) + sum(ympäristöpisteet)

#heitetään noppaa
def heita_nopat(loppupisteet):
    return sum(nopanheitto() for i in range(loppupisteet))

def pelaa():
    pelaajan_kivet = []
    vastustajan_kivet = []
    ympäristöpisteet = [20]  #pelaajalla ja vastustajalla yhteiset ympäristöpisteet
    vastustajan_siirrot = 0

    while True:
        pelaajan_pisteet = laske_loppupisteet(ympäristöpisteet, pelaajan_kivet)
        vastustajan_pisteet = laske_loppupisteet(ympäristöpisteet, vastustajan_kivet)

        print(f"Pelaajan kivet: {pelaajan_kivet}")
        print(f"Vastustajan kivet: {vastustajan_kivet}")
        print(f"Pelaajan pisteet: {pelaajan_pisteet}")
        print(f"Vastustajan pisteet: {vastustajan_pisteet}")
        print(f"Ympäristöpisteet: {sum(ympäristöpisteet)}")

        #peli päättyy, jos jompikumpi on kerännyt 40 kiveä
        if len(pelaajan_kivet) >= 40 or len(vastustajan_kivet) >= 40:
            if len(vastustajan_kivet) >= 40 and len(pelaajan_kivet) < 40:
                print("Peli päättyy, vastustaja keräsi 40 kiveä!")
            elif len(pelaajan_kivet) >= 40 and len(vastustajan_kivet) < 40:
                print("Hienoa! Sait 40 kiveä talteen, ennen vastustajaa!")
            break

        #peli päättyy, jos ympäristöpisteet menevät nollaan eli loppuvat
        if sum(ympäristöpisteet) <= 0:
            print("Ympäristöpisteet ovat loppuneet. Peli päättyy.")
            break

        valinta = input("Matkustetaanko? (kyllä/ei): ").lower()
        if valinta not in ["kyllä", "ei"]:
            print("Virhe, valitse 'kyllä' tai 'ei'.")
            continue

        matkustaako = valinta == "kyllä"
        ympäristöpisteet, vastustajan_siirrot = pelaajan_toiminta(matkustaako, ympäristöpisteet, vastustajan_siirrot)
        ympäristöpisteet = vastustajan_liike(ympäristöpisteet, vastustajan_siirrot)

        tulos = kenttäarpa()
        if tulos == 6:
            kivi_arvo = kiviarpa() * 2
            pelaajan_kivet.append(kivi_arvo)
            print(f'Löysit suuren kiven! Kiven arvo on: {kivi_arvo}')
        elif tulos in range(1, 6):
            kivi_arvo = kiviarpa()
            pelaajan_kivet.append(kivi_arvo)
            print(f'Löysit kiven, arvo: {kivi_arvo}')
        else:
            print('Kentällä ei ole kiveä.')

        #vastustajan kivien etsintä (satunnaisesti löytää kiven)
        if kenttäarpa() > 0:
            kivi = kiviarpa()
            vastustajan_kivet.append(kivi)

        #päivitetään pelaajan ja vastustajan pisteet
        pelaajan_pisteet = laske_loppupisteet(ympäristöpisteet, pelaajan_kivet)
        vastustajan_pisteet = laske_loppupisteet(ympäristöpisteet, vastustajan_kivet)

    print(f"Sinun loppupisteet: {pelaajan_pisteet}")
    print(f"Velhon loppupisteet: {vastustajan_pisteet}")
    print(f"Ympäristöpisteet: {sum(ympäristöpisteet)}")

    #ilmoitetaan, että on loppupelin vuoro
    print("\nLoppupeli alkaa! Voittaja selviää nyt...")

    #siirrytään loppupeliin, jossa heitetään noppaa omien pisteiden verran
    pelaajan_heittopisteet = sum(pelaajan_kivet) + sum(ympäristöpisteet)
    vastustajan_heittopisteet = sum(vastustajan_kivet) + sum(ympäristöpisteet)

    print(f"Sinun heittopisteesi: {pelaajan_heittopisteet}")
    print(f"Velhon heittopisteet: {vastustajan_heittopisteet}")

    pelaajan_heittotulos = sum(nopanheitto() for i in range(pelaajan_heittopisteet))
    vastustajan_heittotulos = sum(nopanheitto() for i in range(vastustajan_heittopisteet))

    print(f"Sinun heittotulos: {pelaajan_heittotulos}")
    print(f"Velhon heittotulos: {vastustajan_heittotulos}")

    if pelaajan_heittotulos > vastustajan_heittotulos:
        print("Voitit loppupelissä!")
    elif pelaajan_heittotulos < vastustajan_heittotulos:
        print("Velho voitti loppupelissä!")
    else:
        print("Loppupeli päättyi tasapeliin!")

pelaa()
.....


