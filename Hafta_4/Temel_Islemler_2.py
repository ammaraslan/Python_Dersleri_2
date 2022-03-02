
# -Dizinin satır ve sütun sayısını değiştirmek : .reshape()
import numpy as np
"""
Numpy array’i yeniden şekillendirmek istediğimizde yani (satır ve sütun) sayısını değiştirmek istediğimizde
 reshape() metodunu kullanabiliriz. numpy_array isimli değişkenimizi yeniden şekillendirelim:
 Tek boyutlu bir diziyi birden fazla boyuta taşıyabilirsin
"""
numpy_dizisi = np.array([0,1,2,3,4,5,6,7,8,9])
print(numpy_dizisi.ndim)
print(numpy_dizisi.shape)
print(numpy_dizisi.reshape(1,10))
print(numpy_dizisi.reshape(10,1))
yeni_dizi = numpy_dizisi.reshape(5,2)
print(numpy_dizisi.reshape(5,2))
print(numpy_dizisi.reshape(2,5))
print(yeni_dizi.ndim)
print(yeni_dizi.shape)