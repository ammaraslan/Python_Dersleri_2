import pandas as pd
from xlrd import *
import pymssql

df = pd.read_csv("dosyalar/ulkeler.csv")
# print(df)

df = pd.read_json("dosyalar/ulkeler.json",encoding="utf-8")
# print(df)

dfx = pd.read_excel("dosyalar/ulkeler.xls")
# print(dfx)

db = pd.read_excel("dosyalar/ulkeler.xls")

# db
server = 'DESKTOP-Aslan'
database = 'AsmaKat'
