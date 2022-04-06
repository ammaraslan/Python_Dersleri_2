class ogrenciler:
    yas=30
    cinsiyet = False
    isim  ="Ammar ASLAN"
    def ekranYaz(self):
        if self.cinsiyet:
            cinsiyet = "Kadın"
        else:
            cinsiyet = "Erkek"
        print("Merhaba",self.isim,"yaşınız",self.yas,"cinsiyetiniz", cinsiyet)

kisi = ogrenciler()
kisi.ekranYaz()