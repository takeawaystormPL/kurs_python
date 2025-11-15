#zapis
plik = open("dane.txt","w",encoding="utf-8");
plik.write("Pierwsza linia \n");
plik.write("Druga linia \n");
plik.close();
#drugi sposób zapisu
with open("dane.txt","w",encoding="utf-8") as plik3:
    plik3.write("Pierwsza linia \n");
    plik3.write("Druga linia \n");
#odczyt
plik2 = open("dane.txt","r");
zawartosc = plik2.read();
print(zawartosc);
plik2.close();