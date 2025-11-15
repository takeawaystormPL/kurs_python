zarobki=int(0);
e = float(input("Podaj przekątną 1:"));
f = float(input("Podaj przekątną 2:"));
if e<=0 or f<=0:
    print("Przekątne muszą być większe od 0")
    exit
else:
    p = (e*f)/2;
    print(f"Pole rombu:{p:.2f}")
#zadanie 2
staz = int(input("Podaj staż: "));
if staz<=5:
    zarobki = 1500+(120*staz)
else:
    zarobki=2300+(100*staz);
print(f"zarobki:{zarobki}");
#zadanie 3
dochod = float(input("Podaj dochód:"));
if(dochod <= 5000):
    print("Wysokość podatku:0zł");
elif(dochod <= 60000):
    print(f"Wysokość podatku:{((dochod*0.16)-800):.2f}zł")
else:
    print(f"Wysokość podatku:{(8800+0.3*(dochod-60000)):.2f}")