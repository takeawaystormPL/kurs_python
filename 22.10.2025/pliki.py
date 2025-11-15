import random;
import math;
import datetime;
imiona = [];
nazwiska = [];
with open("imiona.txt","r",encoding="utf-8") as plik:
    imiona = plik.read().split();
print(imiona);
print(nazwiska);
with open("nazwiska.txt","r",encoding="utf-8") as plik2:
    nazwiska = plik2.read().split();
with open("osoby.txt","w",encoding="utf-8") as plik3:
 for i in range(1,1001):
    indeks1 = random.randint(0,len(imiona)-1);
    indeks2 = random.randint(0,len(nazwiska)-1);
    wiek = random.randint(1960,2010);
    plik3.write(f"{i}. {imiona[indeks1]} {nazwiska[indeks2]} {wiek} \n");
    
with open("osoby.txt","r",encoding="utf-8") as plik4:
    data = datetime.datetime.now();
    zawartosc = plik4.read().split();
    print(zawartosc);
    lacznyWiek = int(0);
    ileWiekow = int(0);
    for i in range(3,len(zawartosc),4):
        wiek = int(data.year) - int(zawartosc[i]);
        lacznyWiek += wiek;
        ileWiekow += 1;
    print(math.ceil(lacznyWiek/ileWiekow));    
        
