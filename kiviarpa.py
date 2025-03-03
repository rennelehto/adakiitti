import random

#Tein nyt niin että kentällä ei ole valmiina kiveä, vaan kentälle saavuttaessa arvotaan onko se siellä.
#Ei vaikuta pelimekaniikkaan, mut selkeyttää koodia imo ku ei tarvii tehä kentistä vielä sanakirjaa.



#Eli kun saapuu kentälle, arvotaan ensin löytyykö kivi.
def kenttäarpa(kiviä):
    if kivet >0:
        tulos = random.randint(0, 1)
    return tulos

#Jos on, arvotaan toisella funktiolla sen "arvo", tässä 1-6 (voi muuttaa vielä).
def kiviarpa(määrä):
    määrä = random.randint(1,6)
    return määrä

kivet = 5
kerätyt_kivet=0

#Pääkoodi
tulos = kenttäarpa(kivet)
if tulos == 1:
    kivet = kivet - 1
    kerätyt_kivet = kerätyt_kivet + kiviarpa(kerätyt_kivet)

#Koodin testaus
if kivet > 1:
    print(f'Pelissä on vielä  {kivet} kiveä.')
if kivet == 1:
    print(f'Pelissä on vielä {kivet} kivi.')
if kivet == 0:
    print('Lol.')

print(f'Kivien kerätty arvo: {kerätyt_kivet}.')
