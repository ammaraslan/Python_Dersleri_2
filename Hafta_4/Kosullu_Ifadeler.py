import numpy as np

dizi = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
kontrol = dizi > 5
print(dizi[kontrol])
dizi_1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
kontrol2 = dizi_1<=5
print(dizi_1[kontrol2])