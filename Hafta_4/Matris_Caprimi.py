import numpy as np

dizi = np.array([0,1,2,3,4,5,6,7,8,9])
dizi1=dizi.reshape(5,2)
dizi2=dizi.reshape(2,5)
print(np.dot(dizi1,dizi2))