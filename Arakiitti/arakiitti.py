
kivet_yhteensä = []
#ympäristöpisteiden kertyminen listaan:
pisteet_yhteensä = []

#Pääkoodi (Rennen)
#tulos = kenttäarpa(kivet)
#f tulos == 1:
   #kivet = kivet - 1
    #kerätyt_kivet = kerätyt_kivet + kiviarpa(kerätyt_kivet)
    kivet_yhteensä.append(kivet)


#Pelin lopussa yhdistetään kerätyt kivet ja ympäristöpisteet
print(f'Kerätyt kivet: {kivet_yhteensä}')
print(f'Kerätyt ympäristöpisteet: {pisteet_yhteensä}')

#pelin loppupisteet
loppupisteet = sum(kivet_yhteensä) + sum(pisteet_yhteensä)
print(f'Pelin loppupisteet: {loppupisteet}')

#Loppupisteet arvotaan noppaa heittämällä (yksi nopanheitto per loppupiste)
nopan_silmälukujen_summa = 0
for i in range(loppupisteet):
    nopan_silmälukujen_summa += nopanheitto()

print(f'Yhteensä nopan heitoista saatujen silmälukujen summa: {nopan_silmälukujen_summa}')