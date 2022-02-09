""" Klavyeden veri Giriş İnput kullanılır. İnput değer olarak str döner. Eğer metinsel
 işlem değilde hesaplama yapılacaksa o zaman tip dönüşümü uygulanmalıdır.
"""

# sayi1 = input("Lütfen Bir Sayı Giriniz!")

# print(sayi1,"'in veri tipi -->",type(sayi1))


sayi_1 = input("Sayi 1 Giriniz")
sayi_2 = input("Sayi 2 Giriniz")

toplam = int(sayi_1) + int(sayi_2)

print("Toplam", toplam)
