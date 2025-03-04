print("")
print("                                                                                         Adakite--Adakiitti")
print("Tehtäväsi on pelastaa maailma ilkeältä velholta, joka pyrkii keräämään maagisia kiviä joilla hän haluaa aiheuttaa ilmastokatastrofin.")
Pelin_aloitus = int(input(
                "\n1. Asia selvä. "
                "\n2. Okei. "
                "\n3. En halua. "
                "\n: "))
while int(Pelin_aloitus in range(1,4)):
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
    else:
        print("--------------------------------------------------")
        print("Error,please try again")
        print("--------------------------------------------------")
        break
print("Onnea matkaan, ja käytä voimiasi hyvään.")
print("--------------------------------------------------")
print(" Ole hyvä ja valitse lentokenttä josta haluat aloittaa pelin seuraavasta listasta. ")
Alkupiste = int(input(
                "\n1. Kenttä 1 "
                "\n2. Kenttä 2 "
                "\n3. Kenttä 2 "
                "\n3. Kenttä 2 "
                "\n3. Kenttä 2 "
                "\n3. Kenttä 2 "
                "\n3. Kenttä 2 "
                "\n3. Kenttä 2 "
                "\n3. Kenttä 2 "
                "\n3. Kenttä 2 "
                "\n3. Kenttä 2 "
                "\n: "))





