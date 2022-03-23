import numpy as np
import pandas as pd

# data

numbers = [20, 30, 40, 50]
metin = ["a", "b", "c", "d"]
skaler = 5

pandas_series = pd.Series(numbers)
metinler = pd.Series(metin)
skalerler = pd.Series(skaler)

print(pandas_series)
print(metinler)
print(skalerler)

# indexleme
metin = ["a", "b", "c", "d"]
index = [1, 2, 3, 4]
serilerim = pd.Series(metin, index)

print(serilerim)

# sözlük ile oluşturma

sozluk = {
    'a': "ammar",
    'b': "Ali",
    'c': "DAli",
    'd': "Tuba",
}

serim = pd.Series(sozluk)
print(serim)

# Elemana Erişim

print(serim[-1])
print(serim[::])
print(serim[:1])
print(serim['a'])
print(serim['d'])
print(serim[['a', 'c']])

# işlemler
print(serim.ndim)
print(serim.shape)
print(serim.dtype)
print(serim.sum())
print(serim.max())
print(serim.min())
print(serim + serim)
print(serim * 3)

sozluk = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
}

serim = pd.Series(sozluk)
print(serim)
print(np.sqrt(serim))

# filtreleme

sonuc = serim > 2
print(sonuc)
print(serim[sonuc])
