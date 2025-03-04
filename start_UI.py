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
print(" ")
print("Ole hyvä ja valitse lentokenttä josta haluat aloittaa pelin seuraavasta listasta. ")




pelattavat_kentät=["Helsinki-Vantaa airport", "JFK international airport", "LAX international airport", "Arlanda airport","London Heathrow airport"]



numero = 1
for kenttä in pelattavat_kentät:
    print(f"{numero}. {kenttä}.")
    numero = numero + 1

alkupiste = int(input(": "))
#if alkupiste in pelattavat_kentät:





