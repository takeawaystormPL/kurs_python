import pandas as pd;
import datetime as dt;
data = {
    'Imię':['Jan','Anna','Marek','Stefan','Kasia','Ola','Tomek','Zofia','Piotr'],
    'Nazwisko':['Kowalski','Nowak','Wiśniewski','Wójcik','Kowalczyk','Kamińska','dsdsds','dsdsda','dsadsah'],
    'Pensja':[7000,8500,6000,7200,9000,7500,6800,8000,9500],
    'Miasto':['Rzeszów','Mielec','Tarnów','Kraków','Warszawa','Rzeszów','Wrocław','Szczecin','Gdańsk']
}
df = pd.DataFrame(data);
years = [1995,1988,2000,1975,1992,1985,1998,1990,1982];
df['Rok'] = years;
age = [];
df['Wiek'] = dt.datetime.now().year - df['Rok']
df.to_csv('wyniki.csv',index=False,encoding = 'utf-8-sig',sep=';');
df.to_csv('wyniki2.csv',index=True);
print(df);
