#sayı 2 eğer sıfır verilirse sistem çöker veya metin girilirse sistem çöker
# sayi1 = int(input("Sayı biri giriniz!"))
# sayi2 = int(input("Sayı ikiyi giriniz!"))
# print(sayi1/sayi2)

try:
  sayi1 = int(input("Sayı biri giriniz!"))
  sayi2 = int(input("Sayı iki giriniz!"))
  print(sayi1/sayi2)
except (ZeroDivisionError):
  print("Sayı sıfıra bölünemez tekrar deneyiniz")
except (ValueError):
  print("Veri Tipiniz Hatalıdır")
finally:
  print("Ne yaparsan yap ben burdayım")