import numpy as np;

arr = np.random.randint(0,100,size=10);
i_positive = np.where(arr < 5);
print(arr[i_positive]);
i_even = np.where(arr%2 == 0);
print(arr[i_even]);
i_min = np.argmin(arr);
print(arr[i_min]);