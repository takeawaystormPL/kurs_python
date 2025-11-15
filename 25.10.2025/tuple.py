cars = ("opel","bmw","fiat") #wartosci są niezmienne
print(cars);
tuple2 = (5) #to nie jest krotka
print(type(tuple));
print(tuple);
tuple2 = (5,) #to jest krotka
print(type(tuple2));
print(tuple);
def div(a,b):
    return a//b,a%b;
iloraz,reszta = div(17,5);
print(iloraz,reszta);
print(type(div(17,5)));
 #słownik z krotkami jako kluczami
location = {
    (50.040617553266806, 21.999495809144776):"Rzeszów - pomnik",
    (50.04217212318415, 22.002430360845235):"Rzeszów - dworzec autobusowuy",
    (50.0427989204364, 22.006990513807796):"Rzeszów - dworzec kolejowy"
}
print(location[(50.04217212318415, 22.002430360845235)])
for coords in location:
    print(f"Szerokość: {coords[0]}, Długość: {coords[1]} -> {location[coords]}")