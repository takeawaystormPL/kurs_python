suma = int(0);
lista=[1,-3,3,-34,-35,-36,7];
for i in range(len(lista)):
    print(lista[i],end=" -- ");
for element in lista:
    print(element,end=" ");
for element in lista:
    suma += element
print(f"Srednia:{suma/len(lista)}");
#wypełnianie tablicy
lista= [0]*100;
#listy dwuwymiarowe
lista2d = [[3,4],[2,3,4],[3]];
print(lista2d);
for el in lista2d:
    for el2 in el:
     print(el2);
    print();
sqr = [x*x for x in range(1,11)];
print(sqr);
numbers = [1,2,3,4,5,6];
sqr2 = [el*el for el in numbers];
sqrEven = [x*x for x in numbers if x%2==0];
print(sqrEven);