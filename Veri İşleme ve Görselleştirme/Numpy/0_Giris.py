import numpy as np

print(np.__version__)
# 0-D Diziler
dizi = np.array(4)
print(dizi.dtype)
print(dizi.ndim)
print(dizi.shape)
# 1-D Diziler
dizi = np.array([1, 2, 3])
print(dizi.dtype)
print(dizi.ndim)
print(dizi.shape)
# 2-D Diziler
dizi = np.array([[1, 2, 3], [2, 5, 8]] ,dtype=int)
print(dizi.dtype)
print(dizi.ndim)
print(dizi.shape)
print(dizi)
# 3-D Diziler
dizi = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(dizi.dtype)
print(dizi.ndim)
print(dizi.shape)
print(dizi)

dizi = np.array([1,2,3],ndmin=5)
print(dizi.dtype)
print(dizi.ndim)
print(dizi.shape)
print(dizi)