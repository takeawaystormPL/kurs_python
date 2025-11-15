procenty = int(input("Podaj procent"));
if procenty < 0:
    print("Liczba procentów nie może być mniejsza niż 0");
elif procenty > 95:
    print("Dostałeś ocenę celującą");
elif procenty > 90:
    print("Dostałeś ocenę bardzo dobrą")
elif procenty > 70:
    print("Dostałeś ocenę dobrą")
elif procenty > 50:
    print("Dostałeś ocenę dostateczną")
elif procenty>30:
    print ("Dostałeś ocenę dostateczną");
else :
    print("Dostałeś ocenę niedostateczną");
dzien_tygodnia = str(print("Podaj dzien tygodnia:"));
match dzien_tygodnia.lower():
    case "sobota"|"niedziela":
        print("Dzisiaj jest weekend")
    case _:
        print("Dzisiaj jest dzień roboczy")
