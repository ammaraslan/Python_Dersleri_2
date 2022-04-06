import numpy as np
#axis = 1 : satırı alır
#axis = 0 : sütunları alır
dizi_1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
dizi_2 = dizi_1.reshape(5, 2)
dizi_3 = dizi_1.reshape(5, 2)
print(dizi_2)

print("--------------")

birlesmis_dizi = np.concatenate([dizi_2, dizi_3], axis=0, dtype=int)
birlesmis_dizi2 = np.concatenate([dizi_2, dizi_3], axis=1, dtype=int)
print(birlesmis_dizi)

print("--------------")
print(birlesmis_dizi2)
