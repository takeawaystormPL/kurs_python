import matplotlib.pyplot as plt;
from scipy import stats
import numpy as np;
def myfunc(x):
    return result.slope*x+result.intercept;

numberOfStorks = [6,6,10,12,10,6,5,5,11,9,9,7,8];
numberOfBirthts = [12,14,19,24,21,12,10,11,20,18,19,15,15];
plt.title('Zależność ilości urodzeń od ilości bocianów');
plt.xlabel('Ilość bocianów');
plt.ylabel('Ilość urodzeń');
plt.scatter(numberOfStorks,numberOfBirthts);

result = stats.linregress(numberOfStorks,numberOfBirthts);
print(f"slope = {result.slope},intercept = {result.intercept}");
mymodel = np.array(list(map(myfunc,numberOfStorks)));
plt.plot(numberOfStorks,mymodel);
print(f"Funkcja liniowa y={result.slope:.2f} + {result.intercept:.2f}")

n = int(input("Wpisz ilość bocianów:"));
print(f"Przy {n} bocianach powinno być mniej więcej {int(myfunc(n))} dzieci");
plt.show();
