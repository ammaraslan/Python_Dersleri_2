import numpy as np
# 1D dilimleme
arr = np.array([1,2,3,4,5,6,7,9], dtype=int)
print(arr[1:5])
print(arr[:5])
print(arr[5:])
print(arr[::-1])
print(arr[1:-5:])

print("2D dilimleme")
# 2D dilimleme
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 4, 5]], dtype=int)
print(arr)
print(arr[0:2,1:3])
