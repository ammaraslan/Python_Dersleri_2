import numpy as np

np_dizi = np.array([0,1,2,3,4,5,6])
np_dizi2 = np.array([[0,1,2]])
np_dizi3 = np.array([[0,1,2],[3,4,5]])


print(np_dizi)
print("------")

print(np_dizi2)
print("------")

print(np_dizi3)
print("------")

# .ndim →numpy array nesnesinin boyutunu döndürür.

print(np_dizi.ndim)
print(np_dizi2.ndim)
print(np_dizi3.ndim)


# - Dizinin satır ve sütun sayısını bulmak: .shape
# .shape →Numpy array nesnesinin kaç satır ve sütundan oluştuğunu gösteren bir tupple nesnesi döndürür.
print("------SHAPE--------")
print(np_dizi.shape)
print(np_dizi2.shape)
print(np_dizi3.shape)

