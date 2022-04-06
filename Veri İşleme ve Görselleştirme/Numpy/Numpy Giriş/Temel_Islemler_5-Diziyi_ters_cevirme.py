import numpy as np

dizi_1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
dizi_1 = dizi_1.reshape(5, 2)
print(dizi_1[::-1])
print("---------")
print(dizi_1[::2])
print("---------")
print(dizi_1[0, 1])
