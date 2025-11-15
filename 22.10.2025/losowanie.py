import random;

def losujDoLotto():
    tablica = [];
    for _ in range(0,6):
        wylosowana = random.randint(1,49);
        czyIstnieje = bool(False);
        if(wylosowana in tablica):
            while czyIstnieje:
             wylosowana = random.randint(1,49);
             if (wylosowana in tablica == False): czyIstnieje = False;
        tablica.append(wylosowana);
    print(tablica);
            
losujDoLotto();