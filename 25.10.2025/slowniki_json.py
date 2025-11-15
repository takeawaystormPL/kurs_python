import os
import json
os.system('cls' if os.name == 'nt' else 'clear')

data ={
    "Piotr": 18,
    "Jan": 19,
    "Paweł": 19,
    "Anna": 20,
    "Hanna": 21
}


text_json = json.dumps(data,indent=4,ensure_ascii=False);
#with open("data.json","w",encoding="utf-8") as file:
    #json.dump(data,file,indent =4,ensure_ascii=False);
text_json = json.dumps(data, indent=4, ensure_ascii=False)
print(text_json)

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False) 
    # indent=4 ładnie formatuje plik dając 4 spacje wcięcia
    #ensure_ascii=False pozwala na zapis polskich znaków,  
# wczytywanie
with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)  # wczytuje dane z pliku i zamienia je na słownik Pythona
    print(data)