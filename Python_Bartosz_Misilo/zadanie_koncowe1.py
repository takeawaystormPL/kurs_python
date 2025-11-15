with open("imiona.txt","r",encoding="utf-8") as plik:
    zawartosc = plik.read().split("\n")
    for imie in zawartosc:
        if(imie[0] == 'A' or imie[0] == 'a'):
            print(imie)

    