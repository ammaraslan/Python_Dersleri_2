"""
i = 0
while (i < 10):
    print(i)
    i = i + 1
"""
# Kullanıcıdan sonsuz veri alma

"""while(True):
    deger = int(input("Bir sayı giriniz"))
    if(deger<0 or deger>10):
        print("Aralık Deışında veri Girdiniz Döngü sonlandı")
        break
    print(deger)"""
# Faktöriyel Hesaplama, 5! =5*4*3*2*1
"""Faktoriyel = int(input("Hesaplamak istediğiniz Faktöriyel değerini giriniz: "))
FaktoriyelSonucu = 1
while (Faktoriyel>=1):
    FaktoriyelSonucu = FaktoriyelSonucu * Faktoriyel
    Faktoriyel=Faktoriyel-1
print(FaktoriyelSonucu)"""

import random as r
sayirasgele = r.randrange(0,10)
giris = int(input("Lütfen bir rakam giriniz"))
i=1
while(giris !=sayirasgele  ):
    print("Tekrar Dene ", "Deneme Sayın=", i)
    i+=1
    giris = int(input("Lütfen bir rakam giriniz"))

print("Tebrikler Buldunuz","Deneme Sayınız=",i)