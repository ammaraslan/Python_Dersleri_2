import numpy as np

arr = np.array([0, 1, 2, 3, 4])
filtre_arr = [True,False,False,True,False]
print(arr[filtre_arr])

ciftler = arr %2 ==0
print(arr[ciftler])

buyukler = arr< 2
print(arr[buyukler])