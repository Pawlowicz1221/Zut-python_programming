print("Wisielec. Masz 8 prób. Powodzenia!")

ileProb = 8
ileRazy = 0
indeks = 0
slowoConst = slowo = "HANGMAN"
zgadywaneSlowo = list(slowo)
odgadnieteSlowo = list("_" * len(slowo))

while ileProb >= 0:
    if "_" not in odgadnieteSlowo:
        print("Wygrałeś!!!")
        break
    if ileProb == 0:
        print("Przegrałeś!!!")
        print("Słowo do odgadnięcia:",slowoConst)
        break
    print("Masz jeszcze",ileProb,"prób.")
    litera = input("Zgadnij literę: ")
    if litera.isalpha():
        litera=litera.upper()
        ileProb-=1
        ileRazy = zgadywaneSlowo.count(litera)
        while ileRazy >= 1:
            indeks = zgadywaneSlowo.index(litera)
            odgadnieteSlowo[indeks] = litera
            zgadywaneSlowo[indeks] = "_"
            ileRazy-=1
        else:
            print(''.join(odgadnieteSlowo))
    else:
        print("Podałeś zły znak.")
        


