# imie = input("Podaj imię: ");
# nazwisko = input("Podaj nazwisko: ");
# print("Witaj:"+imie+nazwisko);
# print(f"Witaj {imie} {nazwisko}");
x = int(input("Podaj x="));
y = float(input("Podaj y="));
z = x+y;
#Błędne
# print(x + " + "+y+" = "+z )
#Poprawne
print(str(x) + " + " +str(y)+" = " + str(z));
print("%d + %.1f = %.2f"%(x,y,z))
print(f"{x}+{y}={z}");
print(f"{x}+{y:.1f}={z:.1f}");
#instrukcje warunkowe
if y==0:
    print("Nie dzielimy przez zero!")
else:
    result=x/y
    print(f"{x}/{y}={x/y}")
