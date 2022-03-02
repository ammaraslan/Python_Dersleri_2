import numpy as np

dizi = np.array([0,1,2,3,4,5,6,7,8,9])
dizi = dizi.reshape(5,2)
print(dizi)

# Maksimum Bulma
print(dizi.max())
# Minimum Bulma
print(dizi.min())
# Toplam Bulma
print(dizi.sum())
# Sutun Toplamu Bulma
print(dizi.sum(axis = 0))
# Satır Toplamı Bulma
print(dizi.sum(axis = 1))

