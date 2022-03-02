# Genel kullanım : dizi[satır,sutun]
import numpy as np

dizi_1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(dizi_1)
# print(dizi_1.ndim)
# print(dizi_1.shape)
dizi_2 = dizi_1.reshape(5, 2)
print(dizi_2)
print("-------")
print(dizi_2[0])  # sıfırıncı satır verir
print(dizi_2[1])  # birinci satır verir
print(dizi_2[2:4])  # 2. ve 3. satırları --> row  verir
print(dizi_2[1][1])  # direk elemanı verir
print("-------")
print(dizi_2[:, 0])
print(dizi_2[:, 1])
print("-------")
print(dizi_2[0, :])
print(dizi_2[0:2, :])

# Not: dizi[:,:] → buradaki “:” kullanımı tüm satır ve sütunları seçmemizi sağlar.

print(dizi_2[3,1])
