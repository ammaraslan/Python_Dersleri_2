"""Vize ve Final Notlarını Kullanıcıdan
Alıp Kişinin geçip geçmediğini söyleyen programı yazınız.
Kurallar 1: Final 60 'dan büyük eşit olacak
Kurallar 2: Genel ortalama 60 'dan büyük eşit olacak
"""
vize = int(input("Vize Notunu Giriniz"))
final = int(input("Final Notunuz Giriniz"))

gno = vize * 0.4 + final * 0.6
print("GNO:", gno)
print(gno >= 60 and final >= 60)
