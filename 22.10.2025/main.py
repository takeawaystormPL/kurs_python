import math;
lista = [-705, 318, -460, -822, 139, 877, -91, 446, -639, -123, 52, 684, -955, 401, 785, -128, -671, 239, -
319, 530, -215, 791, -444, -945, 283, -511, 693, 319, -132, -779, 429, 686, -38, 45, 906, -382, 621, -
995, 274, 179,-551, -698, 848, -767, 264, -64, 309, -838, 957, -418, 214, 654, -572, -186, 344, 812, -
974, -346, 124, -33, 707, -670, 861, 559, -829, -27, 978, 11, -901, -222, 100, -366, 495, 737, -988, -
516, 187, -813, 660, 263, -150, -645, 933, 892, -560, -320, 358, 494, -447, 649, -177, -30, 581, -741,
162, 420, -857, -531, 799, -276];
def wyswietlParzyste(lista:list[int]):
    for i in range(0,len(lista)):
        if(lista[i]%2 == 0): 
            print(lista[i]);
def wyswietlLiczbeElementowParzystych(lista:list[int]):
    liczba = int(0);
    for el in lista:
        if(el % 2 == 0):
            liczba+=1;
    print(liczba)
def wyswietlSumeElementowDodatnich(lista:list[int]):
    suma = int(0);
    for el in lista:
        if(el > 0):
            liczba+=el;
    print(suma);
def wyswietlNajwiekszyUjemnyElement(lista:list[int]):
    najmniejszy = int(0);
    for el in lista:
        if(el < najmniejszy):
            najmniejszy=el;
    print(najmniejszy);
def sprawdzPesel():
    #Tak więc początek numeru PESEL osoby urodzonej 10 lutego 1899 roku będzie wyglądał tak: 998210... a osoby urodzonej 10 lutego 1999 roku tak: 990210...
    #Teraz została nam jeszcze sprawa obliczania sumy kontrolnej. Każdą pozycję numeru ewidencyjnego mnoży się przez odpowiednią wagę, są to kolejno: 1 3 7 9 1 3 7 9 1 3. Następnie utworzone iloczyny dodaje się i wynik dzieli się modulo 10. Wynik ten należy odjąć od 10 i znów podzielić przez modulo 10 (to zabezpieczenie gdybyśmy w poprzednim kroku otrzymali 10).
    pesel = "08241508954";
    if(len(pesel) != 11):
        print("Nieprawidlowy pesel");
        exit();
    wagi = list[int]([1,3,7,9,1,3,7,9,1,3]);
    suma_kontrolna = int(0);
    for i in range(0,(len(pesel)-1)):
        suma_kontrolna += int(pesel[i])*wagi[i];
    suma_kontrolna = 10-(suma_kontrolna%10);
    if suma_kontrolna == 10:
        suma_kontrolna%=10;
    if(int(pesel[10]) != suma_kontrolna):
        print("Nieprawidlowy pesel")
        exit();
    print("Prawidlowy pesel")
    if(int(pesel[9]) % 2 == 0):
        print("Jestes kobieta")
    else:
        print("Jestes mezczyzna");
        
sprawdzPesel()
def sitoErastotelesa():
#for i := 2, 3, 4, ..., nie większe niż n:{\displaystyle {\sqrt {n}}{:}}
  #if A[i] = true:
    #for j := i*i, i*(i+1), i*(i+2), ..., nie większe niż n :
      #A[j] := false
#Wyjście: wartości i takie, że A[i] zawiera wartość true.
 n = 100;
 tablica = [True]*n;
 tablica[0] = False;
 tablica[1] = False;
 for i in range(2,math.floor(math.sqrt(n))):
     if(tablica[i] == True):
         for j in range(i*2,n,i):
             tablica[j] = False;
 for i in range(0,len(tablica)):
     if(tablica[i] == True): print(i);
sitoErastotelesa();