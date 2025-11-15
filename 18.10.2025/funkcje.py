def avg(x,y):
    return x/y;
def silnia(x):
    if(x == 1 or x == -1):return x;
    if(x < -1):return x*silnia(x+1);
    else:return x*silnia(x-1)
def silnia2():
    n = int(input("Podaj ilosc:"));
    k = int(input("Podaj drugą ilość:"));
    if(n<k): n,k = k,n
    return silnia(n) / (silnia(k) * silnia(n-k))

def avgLista(list:list[int]):
    if(len(list) <= 0):return "Lista jest pusta";
    suma = int(0);
    rozmiar = len(list);
    for liczba in list:
        suma += liczba;
    return suma/rozmiar;
def fibonacci(n):
    if(n <= 2):return 1;
    return fibonacci(n-1) + fibonacci(n-2);
def fibonacci2(n):
    suma = 0;
    s1 = 1;
    s2 = 1;
    for i in range (n-2):
        suma = s1 + s2;
        s1=s2;
        s2=suma;
    return suma;
#funkcja o zmiennej liczbie parametrów
def avg(a,b, *inne): #* to dodatkowe parametry
    suma=a+b
    n=2
    for liczba in inne:
        suma+=liczba
    n+=len(inne)
    return suma/n        
print(silnia(5));
print(silnia2());
print(avgLista([1,2,3,4,5]));
print(fibonacci2(8));
