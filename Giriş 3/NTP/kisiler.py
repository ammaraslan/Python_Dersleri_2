class Kisiler:
    def __init__(self,ad,soyad,tc,vize,final):
        self.isim =ad
        self.soyisim =soyad
        self.tc =tc
        self.vize =vize
        self.final =final

    def notHesapla(self):
        self.gno=self.vize*0.4+self.final*0.6
        return self.gno

# bir = kisiler("Ammar","Aslan",223,50,80)
# bir.notHesapla()
# print(bir.gno)