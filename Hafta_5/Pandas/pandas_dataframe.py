import kis as kis
import pandas as pd

# s1 = pd.Series([3, 2, 4, 5])
# s2 = pd.Series([0, 2, 4, 5])
#
# data = dict(elma=s1, portakal=s2)
# df = pd.DataFrame(data)
# print(df)

df = pd.DataFrame()
print(df)

df = pd.DataFrame([1, 2, 3, 4])
print(df)

df = pd.DataFrame([["Ali", 60], ["ahmet", 50]])
print(df)

isimler = ["Ali", 60], ["ahmet", 50], ["ela", 20]
df = pd.DataFrame(isimler, columns=["isim", "Not"])
print(df)

isimler = [["Ali", 60], ["ahmet", 50], ["ela", 20], ["murad", 90]]
df = pd.DataFrame(isimler, columns=["isim", "Not"], index=[1, 2, 3, 4])
print(df)
isimler = [["Ali", 60], ["ahmet", 50], ["ela", 20], ["murad", 90]]
df = pd.DataFrame(isimler, columns=["isim", "Not"], index=[1, 2, 3, 4])
print(df)

sozluk = {"isim": ["Ahmet", "Veli", "Cınar"],
          "Notları": [50, 60, 70]
          }
numaralari = [5454,2121,8451]
kisiler = pd.DataFrame(sozluk,index=numaralari)
print(kisiler)

