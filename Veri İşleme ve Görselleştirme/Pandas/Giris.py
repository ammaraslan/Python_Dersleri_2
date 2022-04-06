import pandas as pd

print(pd.__version__)

dosya = pd.read_csv("dosyalar/train.csv")
# print(dosya)
# print(dosya.head)

# print(dosya.tail(5))
# print(dosya.shape)
# print(dosya.size)
# print(dosya.dtypes)
# print(dosya.isnull().sum())
# print(dosya.Name.head())
# print(dosya.Ticket.head())

# print(dosya.rename(columns={"Name":"Isim","PassengerId":"NUMARA","Survived":"Hayatta Kaldı mı"}))
# print(int(dosya.shape[0])-int(dosya.Survived.sum()))

# iloc metodunda satır ve sütun indeksleri girilerek işlem yapılır. Bu komutların ilk parametresi satırı ikinci parametresi sütunu ifade eder.

print(dosya.iloc[2, [1, 3, 5, 2]].head())
print(dosya.Name.head())

dosya = dosya.dropna(axis=1, how="all").shape
