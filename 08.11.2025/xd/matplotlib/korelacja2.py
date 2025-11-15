import matplotlib.pyplot as plt;
import numpy as np;
from scipy import stats;

def myfunc(x):
    return result.slope*x+result.intercept
plt.title("Zależność pensji od poziomu doświadczenia pracownika");
plt.xlabel("Lata doswiadczenia");
plt.ylabel("Pensja");

x = [1,2,3,4,5,6,7,8,9,10];
y = [4000,4500,5000,5500,6000,6500,7000,7500,8000,8100];

plt.scatter(x,y);
result = stats.linregress(x,y);
mymodel = np.array(list(map(myfunc,x)));
z = list(map(myfunc,x));

iloscLatDoswiadczenia = int(input("Podaj ilość lat doświadczenia:"));
print(f"Przy {iloscLatDoswiadczenia} latach doświadzenia powinieneś zarabiać:{myfunc(iloscLatDoswiadczenia)}");
plt.plot(x,z)
plt.show();