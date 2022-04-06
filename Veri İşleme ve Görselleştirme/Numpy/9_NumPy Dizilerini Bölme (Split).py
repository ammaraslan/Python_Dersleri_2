import numpy as np


arr = np.array([1, 2, 3, 4, 5, 6])

isim = "ammar aslan batman siirt"
dizi = isim.split(" ")
print(dizi)

arr = np.array_split(arr,4)
print(arr)
