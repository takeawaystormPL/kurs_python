import matplotlib.pyplot as plt;

import numpy as np

numberOfStorks = np.array([6,6,10,12,10,6,5,5,11,9,9,7,8]);
numberOfBirthts = np.array([12,14,19,24,21,12,10,11,20,18,19,15,15]);
plt.title('Zależność ilości urodzeń od ilości bocianów');
plt.xlabel('Ilość bocianów');
plt.ylabel('Ilość urodzeń');
plt.scatter(numberOfStorks,numberOfBirthts);
plt.show();