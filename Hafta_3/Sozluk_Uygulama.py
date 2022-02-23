sozluk={}
i=0
while i<3:
  ogr_no=input("öğrenci numarası :")
  adi=input("adınız :")
  soyadi=input("soyadınız :")
  tc=input("t.c kimlik numarası :")
  sozluk.setdefault(ogr_no,{"adi":adi,"soyadi":soyadi,"tc":tc})
  i=i+1
print(sozluk)