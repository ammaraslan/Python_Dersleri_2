import numpy as np
#Copy
dizi = np.array([1,2,3,4])
print(dizi)
dizicopyasi = dizi.copy()
dizicopyasi[0] = 1111
print(dizicopyasi)
print(dizi)
#View -->Görünüm (View), orijinal dizide yapılan değişikliklerden ETKİLENMELİDİR.
print("View----------")
dizi = np.array([1,2,3,4])
print(dizi)
dizicopyasi = dizi.view()
dizicopyasi[0] = 1111
print(dizicopyasi)
print(dizi)