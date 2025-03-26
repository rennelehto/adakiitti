import random

#Tein nyt niin että kentällä ei ole valmiina kiveä, vaan kentälle saavuttaessa arvotaan onko se siellä.
#Ei vaikuta pelimekaniikkaan, mut selkeyttää koodia imo ku ei tarvii tehä kentistä sanakirjaa.



#Eli kun saapuu kentälle, arvotaan ensin löytyykö kivi.
def kenttäarpa(kivet):
    if kivet >0:
        tulos = random.randint(0, 6)
    return tulos

#Jos on, arvotaan toisella funktiolla sen "arvo", tässä 1-6 (voi muuttaa vielä).
#"Iso" kivi on kaksi kertaa pientä arvokkaampi, eli nopan tulos kerrotaan kahdella.

def kiviarpa(määrä):
    määrä = random.randint(1,6)
    return määrä

#Pääkoodi

kivet = 6
kerätyt_kivet=0

tulos = kenttäarpa(kivet)

if tulos == 6:
    kivet = kivet - 1
    kerätyt_kivet = kerätyt_kivet + (kiviarpa(kerätyt_kivet) * 2)
    print('Löysit suuren kiven!')

if tulos in range(1, 6):
    kivet = kivet - 1
    kerätyt_kivet = kerätyt_kivet + kiviarpa(kerätyt_kivet)
    print('Löysit kiven!')

if tulos == 0:
    print('Kentällä ei ole kiveä.')



#Koodin testaus
if kivet > 1:
    print(f'Pelissä on vielä  {kivet} kiveä.')
if kivet == 1:
    print(f'Pelissä on vielä {kivet} kivi.')
if kivet == 0:
    print('Lol.')

print(f'Kivien kerätty arvo: {kerätyt_kivet}.')
