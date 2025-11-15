#sortowanie
import os;
os.system("cls" if os.name == "nt" else "clear");
data = {
    "Piotr": 18,
    "Jan": 19,
    "Paweł": 40,
    "Anna": 20,
    "Zbigniew": 34,
    "Hanna": 21
}

sorted_name = dict(sorted(data.items())) # bez argumentu sortuje po kluczach, dict() zamienia z powrotem na słownik
print(sorted_name)

sorted_age = dict(sorted(data.items(), key=lambda item: item[1])) # sortuje po wartościach
print(sorted_age)   

# odwrócenie kolejności
sorted_age_desc = dict(sorted(data.items(), key=lambda item: item[1], reverse=True)) # sortuje po wartościach
print(sorted_age_desc)