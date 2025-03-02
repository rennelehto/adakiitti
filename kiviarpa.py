import random

def kenttäarpa(kiviä):
    if kivet >0:
        tulos = random.randint(0, 1)
    return tulos

def kiviarpa(määrä):
    määrä = random.randint(1,6)
    return määrä

kivet = 5
kerätyt_kivet=0

tulos = kenttäarpa(kivet)
if tulos == 1:
    kivet = kivet - 1
    kerätyt_kivet = kerätyt_kivet + kiviarpa(kerätyt_kivet)

if kivet > 1:
    print(f'Pelissä on vielä  {kivet} kiveä.')
if kivet == 1:
    print(f'Pelissä on vielä {kivet} kivi.')
if kivet == 0:
    print('Lol.')

print(f'Kivien kerätty arvo: {kerätyt_kivet}.')
