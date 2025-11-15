import math;
def avg(list):
    return sum(list)/len(list)
def weightedAvg(list:list[list[int]]):
    if(len(list[0]) != len(list[1])):
        exit();
    suma = int(0);
    for i in range(0,len(list[0])):
        suma += list[0][i] * list[1][i];
    return suma / sum(list[1]); 
def variance(list:list[int]):
    srednia = avg(list);
    wariancja_suma = int(0);
    for i in range (0,len(list)):
        wariancja_suma += (srednia-list[i])**2;
    return wariancja_suma/len(list);
def stddev(list:list[int]):
    return math.sqrt(variance(list));
def median(list:list[int]):
    list.sort();
    if(((len(list))/2 - 1)%2 !=0):
        return list[len(list)//2-1]; 
    else:
        return (list[len(list)//2-1] + list[len(list)//2])/2;
def mode(lista:list[int]):
    ileRazy = {};
    for el in lista:
        ileRazy[el] = ileRazy.get(el,0)+1;
    najwiekszyKlucz = max(ileRazy,key=lambda k:ileRazy[k]);
    ileRazyNajwiekszaWartosc = int(1);
    for key,value in ileRazy.items():
        if(key != najwiekszyKlucz):
            if(value == ileRazy[najwiekszyKlucz]):ileRazyNajwiekszaWartosc += 1;
    if(ileRazyNajwiekszaWartosc == len(ileRazy)):return "Brak nominanty";
    else:
        keys = list(ileRazy.keys());
        keys.sort();
        dominanty = list();
        for key in keys:
            if(ileRazy[key] == ileRazy[najwiekszyKlucz]):
                keys.remove(key);
        return dominanty;