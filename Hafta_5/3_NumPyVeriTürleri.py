
# NumPy’de Veri Türleri
# i – integer
# b – boolean
# u – unsigned integer
# f – float
# c – complex float
# m – timedelta
# M – datetime
# O – object
# S – string
# U – unicode string
# V – fixed chunk of memory for other type ( void )
import numpy as np

dizi = np.array(['a',1,2,3],dtype='S')
print(dizi.dtype)
print(dizi)

dizi = np.array(['a',1,2,3],dtype='i')
print(dizi.dtype)
print(dizi)

