#przyklad 1
try:
    x = int(input("Podaj liczbę: "))
    result = 10 / x
    print("Wynik:", result)
except ZeroDivisionError:
    print("Serio? Dzielenie przez zero? Co Ty zrobisz??!!!")
except ValueError:
    print("To nie liczba, tylko jakaś literka albo inny znaczek. Spróbuj jeszcze raz.");
#przyklad 2
try:
    with open("tajne_dane.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("Pliku nie ma. Może po prostu go sobie wyobraź?")
#przykład 3
try:
    numbers = [1, 2, 3, 4, 5]
    print(numbers[7])
except IndexError:
    print(f"Lista nie jest z gumy, indeksy kończą się na {len(numbers) -1}.");
#przykład 4
class ToMuchCoffeeError(Exception):
    pass

try:
    kawa = int(input("Ile filiżanek kawy dzisiaj wypiłeś? "))
    if kawa > 5:
        raise ToMuchCoffeeError("To już nie kofeina, to doping!") #rzucenie własnego wyjątku
    print("Spokojnie, jeszcze żyjesz.")
except ToMuchCoffeeError as e:
    print("Uwaga:", e)
# przykład 5
try:
    nr = int(input("Podaj liczbę dodatnią: "))
    if nr < 0:
        raise ValueError("Miała być dodatnia! Nie toleruję minusów!!!!")
except ValueError as e:
    print("Błąd:", e)
else: #else należy do try, nie if
    print(f"Dobra robota, {nr} to fajna liczba.")
finally:
    print("Nieważne co się stało, i tak muszę to wykonać.")
# przykład 6
try:
    with open("dane_uzytkownika.txt", "r", encoding="utf-8") as f:
        zawartosc = f.read()
        print("Plik wczytany poprawnie.")
except FileNotFoundError:
    print("Brak pliku. Może ktoś go usunął, może nigdy nie istniał.")
except PermissionError:
    print("Brak dostępu. System nie ufa Tobie albo temu folderowi.")
else:
    print("Zawartość pliku:", zawartosc[:50], "...")
finally:
    print("Zamykam temat pliku.")
# przyklad 7
import requests
#pip install requests
country = input("Podaj nazwę kraju: ")
try:
    response = requests.get(f"http://universities.hipolabs.com/search?country=poland", timeout=3)
    # timeout=3 - czekaj maksymalnie 3 sekundy na odpowiedź od serwera, a potem rzuć wyjątek
    response.raise_for_status()  # jeśli status != 200, rzuca wyjątek
    data = response.json()
    print("Lista uniwersytetów:")
    for u in data:
        print(u['name'])
except requests.exceptions.Timeout:
    print("Serwer mówi: 'Poczekaj chwilę'... no i czekasz, czekasz, czekasz, ...")
except requests.exceptions.ConnectionError:
    print("Nie ma internetu, albo router znów się wygłupia.")
except requests.exceptions.HTTPError as e:
    print("Serwer odpowiedział błędem:", e)
else:
    print("Dane odebrane poprawnie.")
finally:
    print("Zakończono zapytanie do API.")

#Dodaj własny wyjątek, dla sytuacji, gdy wynik wyszukiwania będzie pusty pusty (zmienna data bedzie pustą listą )

#przykład 8
try:
    wiek = int(input("Podaj swój wiek: "))
    if not 0 < wiek < 120:
        raise ValueError("Nie wierzę, że masz tyle lat.")
except ValueError as e:
    print("Błąd:", e)
else:
    print("OK, przyjmuję ten wiek.")
finally:
    print("Walidacja zakończona.")
# przykład 9 
import sqlite3 # wbudowana w Pythona

try:
    conn = sqlite3.connect("baza.db")
    cursor = conn.cursor()
    #cursor to  pośrednik między kodem a bazą danych (jak kelner pośredniczy miedzy klientem,a kucharzem)
    # execute(sql, params) — wykonuje jedno zapytanie,
    # executemany(sql, list_of_params) — wiele zapytań na raz,
    # fetchone() — pobiera jeden rekord,
    # fetchall() — pobiera wszystkie rekordy,
    # fetchmany(n) — pobiera n rekordów.
    name = input("Podaj imie: ")
    cursor.execute("CREATE TABLE IF NOT EXISTS uzytkownicy (id INTEGER PRIMARY KEY, imie TEXT)")
    cursor.execute("INSERT INTO uzytkownicy (imie) VALUES (?)", (name,)) # można też [name,]
    # (name,) jest krotką (tuple), a nie zwykłym nawiasem wokół zmiennej
    # (name,) oznacza: wstaw name jako pierwszy (i jedyny) element krotki.
    # sqlite3 wymaga, żeby dane przekazywać jako sekwencję (tuple lub listę), nawet jeśli jest tylko jeden parametr.

    conn.commit()

    cursor.execute("SELECT * FROM uzytkownicy")
    for row in cursor.fetchall():
        print(row)
except sqlite3.OperationalError as e:
    print("Błąd SQL:", e)
except sqlite3.DatabaseError:
    print("Coś jest nie tak z bazą.")
else:
    print("Wszystko zapisane i odczytane bez błędów.")
finally:
    conn.close()
    print("Połączenie z bazą zamknięte.")

