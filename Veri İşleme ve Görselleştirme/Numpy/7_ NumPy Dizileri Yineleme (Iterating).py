# Yineleme (Iterating), öğeleri tek tek gözden geçirmek anlamına gelir.
import numpy as np

arr = np.array([1, 2, 3])
print("1 boyut")
for x in arr:
    print(x)
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("2 boyut")
for x in arr:
    for y in x:
        print(y)
print("# Nditer() Kullanarak Dizileri Yineleme")
# Nditer() Kullanarak Dizileri Yineleme
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for i in np.nditer(arr):
    print(i)
"""
op_dtypes argümanını kullanarak yineleme sırasında öğelerin veri
türünü değiştirmek için beklenen veri türünü iletebiliriz.
NumPy, in-place veri türünü (öğenin dizide olduğu yerde) 
değiştirmez, bu nedenle bu eylemi gerçekleştirmek için başka bir alana ihtiyaç duyar, 
bu fazladan boşluğa tampon adı verilir ve onu nditer() içinde etkinleştirmek için 
flags=['buffered'] 
parametresini kullanabiliriz.
"""

arr = np.array([3, 2, 3])
for i in np.nditer(arr,flags=["buffered"],op_dtypes=["S"]):
    print(i)