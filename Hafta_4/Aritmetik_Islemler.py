import numpy as np

dizi_1 = np.array([0,1,2,3,4,5,6,7,8,9])
dizi_2 = np.array([10,11,12,13,14,15,16,17,18,19])

dizi_1 = dizi_1.reshape(5,2)
dizi_2 = dizi_2.reshape(5,2)
print(dizi_1)
print(dizi_2)

# İki Dizi Toplamı
dizi_3 = dizi_1+dizi_2
print(dizi_3)
# İki Dizi Farkı
dizi_3 = dizi_1-dizi_2
print(dizi_3)
# İki Dizi Çarpımı
dizi_3 = dizi_1*dizi_2
print(dizi_3)
# İki Dizi Bölüm
dizi_4 = dizi_1/dizi_2
print(dizi_4)
# Dizinin Her Elemanına Sabit Ekleme
dizi_3 = dizi_3 + 5
print(dizi_3)
# Dizinin Her Elemanına Sabit Çarpma
dizi_3 = dizi_3 * 5
print(dizi_3)
# Dizinin Her Elemanına Sabit Çıkarma
dizi_3 = dizi_3 - 5
print(dizi_3)
# Dizinin Her Elemanına Sabit Bölme
dizi_3 = dizi_3 / 5
print(dizi_3)
