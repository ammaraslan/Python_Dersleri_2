import numpy as np

arr = np.array([1.1,2.3,4.8],dtype="f")
print(arr.dtype)
print(arr)

# Dönüştürme
yeniarr = arr.astype('i')
print(yeniarr.dtype)
print(yeniarr)

#
dizi = np.array([-1,0,2,3])
booldizi = dizi.astype("bool")
print(booldizi)