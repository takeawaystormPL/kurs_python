def find(rok1:int,rok2:int,nazwaPliku:str):
 if(rok1 > rok2):
     rok1,rok2 = rok2,rok1
 with open(nazwaPliku,"r",encoding="utf-8-sig") as plik:
    zawartosc = plik.read().split("\n")
    for line in zawartosc[:len(zawartosc)-1]:
        dane = line.split(" ")
        if(int(dane[3]) >= rok1 and int(dane[3]) <= rok2):
            print(f"{dane[1]} {dane[2]}")
find(1999,2003,"osoby.txt")
    