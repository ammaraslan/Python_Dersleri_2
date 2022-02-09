# 1-) isim, soyisim, ve doğum tarihi bilgilerini girip ekrana “Merhaba Ammar ASLAN yaşınız 40 Hoş Geldiniz”
# şeklinde çıktı veren python kodunu yazınız.

import datetime as dt

bugununTarihi = dt.datetime.now().year

isim = "Ammar"
soyisim = "Aslan"
dogumTarihi = 1980
yas = bugununTarihi - dogumTarihi
print("Merhaba", isim, soyisim,"Yaşınız:", yas,"Hoş Geldiniz.")
