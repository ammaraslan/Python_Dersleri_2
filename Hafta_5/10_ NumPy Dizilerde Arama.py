import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4, 1, 1])

x = np.where(arr%2 == 0)
print(x)
arr = np.array([1, 3, 5, 7, 9])

x = np.searchsorted(arr, 4)

print(x)