"""
camalCase
PascalCase
snake_case
kebab-case
"""
"""
Mod    ve Açıklama
r:    Mevcut dosyayı okumak için açar, yoksa hata verir
w:    Dosya yoksa oluşturur, varsa içeriği silerek sıfır dosya açar
a:    Dosya yoksa oluşturur, varsa dosyanın sonunda imleçten başlayarak ekleme yapar
r+:    Dosyayı hem okuma, hem yazma(w) modunda açar
"""

# dosya = open("ornek.txt","r")
# oku = dosya.read(5)
# # print(oku)
# sayirNumarasi = 1
# for i in open("Dosyalar/ornek.txt"):
#     print(sayirNumarasi, ".", i)
#     sayirNumarasi += 1

"""Dosyayı Diziye Aktarma

dosya = open("Dosyalar\ornek.txt","r").readlines()
print(dosya[3])
"""

# dosya = open("Dosyalar\okisiler.txt","w")
# dosya.write("Ali Kemal\n")
# dosya.write("Amamr ASLAN")
# dosya.close()


# Öğrenci adında bir dosya oluşturup içerisinde aşağıdaki formatta veriler kullanıcıdan alınıp eklenmesi istenmektedir. Bu bilgiler boşlukla ayrılacak ve her öğrenci için alt satıra inilecektir.
#
# Öğrenci Numarası
# Öğrenci Adı
# Vize Notu
# Final Notu
# Genel Not Ortalaması
# Genel Not Ortalamasını Vize0,4 + Final0,6 olarak yazan python kodunu yazınız.
# dosya = open("Dosyalar/ogrenciler.txt", "r+")
# ogrNo = input("Lütfen Okul Numaranızı Giriniz")
# ogrAdi = input("Lütfen Adınızı Giriniz")
# ogrSoyadi = input("Lütfen Soyadı Giriniz")
# ogrVize = input("Lütfen Vizenizi Giriniz")
# ogrFinal = input("Lütfen Finalinizi Giriniz")
# ogrGNO = int(ogrVize) * 0.4 + int(ogrVize) * 0.6
# dosya.writelines([ogrNo, " ", ogrAdi, " ", ogrSoyadi, " ", ogrVize, " ", ogrFinal, " ", str(ogrGNO)])
# dosya.close()

for satırlar in open("Dosyalar\ogrenciler.txt"):
    degerler = satırlar.split(" ")
    print(degerler)
