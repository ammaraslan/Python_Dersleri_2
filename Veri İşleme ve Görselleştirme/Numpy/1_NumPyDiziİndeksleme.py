import numpy as np

# Dizi Öğelerine Erişim
arr = np.array([1, 2, 3])
print(arr[0], arr[2])
print("2 Boyutlu Dizilere Erişim")
# 2 Boyutlu Dizilere Erişim
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
print(arr[0][1])
print(arr[0, 1])
print("3 Boyutlu Dizilere Erişim")
# 3 Boyutlu Dizilere Erişim
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])

print("NEgatif İndexleme")

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

print(arr[1, -2])