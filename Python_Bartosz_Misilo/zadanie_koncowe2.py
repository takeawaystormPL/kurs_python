with open("./liczby.txt","r",encoding="utf-8") as plik:
    zawartosc = plik.read().split('\n');
    for liczba in zawartosc:
        if(int(liczba)<100):
            print(liczba);
    
        
            