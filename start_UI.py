import random

print(" ")
print("                                                                                         Adakite--Adakiitti")
print("Tehtäväsi on pelastaa maailma ilkeältä velholta, joka pyrkii keräämään maagisia kiviä joilla hän haluaa aiheuttaa ilmastokatastrofin.")
Pelin_aloitus = int(input(                          #Vastaus valinta
                "\n1. Asia selvä. "
                "\n2. Okei. "
                "\n3. En halua. "
                "\n: "))
while int(Pelin_aloitus) == 1 or 2 or 3:
    if Pelin_aloitus == 1:
        print("--------------------------------------------------")
        print("Asia selvä.")
        print("--------------------------------------------------")
        break
    if Pelin_aloitus == 2 :
        print("--------------------------------------------------")
        print("Okei.")
        print("--------------------------------------------------")
        break
    if Pelin_aloitus == 3:
        print("--------------------------------------------------")
        print("Valitettavasti et saa jatkaa.")
        print("--------------------------------------------------")
        quit()
    if Pelin_aloitus != 1 or 2 or 3:
        print("--------------------------------------------------")
        print("Error,please try again")
        print("--------------------------------------------------")
        Pelin_aloitus = int(input(  # Vastaus valinta
            "\n1. Asia selvä. "
            "\n2. Okei. "
            "\n3. En halua. "
            "\n: "))

print("Onnea matkaan, ja käytä voimiasi hyvään.")
print("--------------------------------------------------")
print("Ole hyvä ja valitse lentokenttä josta haluat aloittaa pelin seuraavasta listasta. ")




pelattavat_kentät=["Helsinki-Vantaa airport", "JFK international airport", "LAX international airport", "Arlanda airport","London Heathrow airport"]
pelattavat_kentät2 = ["Helsinki-Vantaa airport", "JFK international airport", "LAX international airport", "Arlanda airport","London Heathrow airport"]
kenttä1 = []
kenttä2 = []
kenttä3 = []
kenttä4 = []
kenttä5 = []

for n in range(1):
    choice = random.choice(pelattavat_kentät2)  # Pick a random element
    kenttä1.append(choice)
    pelattavat_kentät2.remove(choice)

    choice = random.choice(pelattavat_kentät2)  # Pick a random element
    kenttä2.append(choice)
    pelattavat_kentät2.remove(choice)

    choice = random.choice(pelattavat_kentät2)  # Pick a random element
    kenttä3.append(choice)
    pelattavat_kentät2.remove(choice)

    choice = random.choice(pelattavat_kentät2)  # Pick a random element
    kenttä4.append(choice)
    pelattavat_kentät2.remove(choice)

    choice = random.choice(pelattavat_kentät2)  # Pick a random element
    kenttä5.append(choice)
    pelattavat_kentät2.remove(choice)


Alkupiste = int(input(
                f"\n1. {kenttä1}"
                f"\n2. {kenttä2}"
                f"\n3. {kenttä3}"
                f"\n4. {kenttä4}"
                f"\n5. {kenttä5}"
                "\n: "))






