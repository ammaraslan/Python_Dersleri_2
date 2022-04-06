"""
Pythonda 4 farklı liste tipi vardır. Bunlar; List, Tuple, Set ve Dictionary veri tipleridir.

*  List, elemanları sıralanabilir, güncellenebilir ayrıca her bir eleman liste içerisinde birden fazla tekrarlanabilir.

*  Tuple, elemanları sıralanabilir ancak güncellenemez ve her bir eleman liste içerisinde birden fazla tekrarlanabilir.

*  Set, elemanları sıralanamaz ve indekslenemez ayrıca her bir eleman liste içerisinde sadece bir tane olabilir.

*  Dictionary, key ve value şeklinde değer alırlar. Aynı key bilgisiyle birden fazla eleman olamaz.
"""
"""
liste = ["Ali","Kemal","Ceylan","ammar aslan"]
print(liste)
print(liste[2])
print(len(liste))

for i in liste:
    print(i)

liste2 = "ammaraslan"
print(liste2)
liste2 = list(liste2)
print(liste2)
print(liste[0::2])
"""
"""
liste = ["Ali","Kemal","ceylan","ammar aslan"]

liste.append("4")
print(liste)
liste.insert(2,"5")
print(liste)
liste.pop(1)
print(liste)
liste.remove("4")
print(liste)
liste.sort()
print(liste)

"""

"""dizi = list(range(0, 100, 2))
print(dizi)
dizi2 = [];
for i in range(0, 100, 2):
    dizi2.append(i)
print(dizi2)

dizi3 = [i for i in range(0,100,2) if i<10]

print(dizi3)
"""
# 1- "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
degerler = "Bmw, Mercedes, Opel, Mazda";
araclar = degerler.split(", ")
print(araclar)
# 2- Liste Kaç elemanlıdır ?
print(len(araclar))
# 3- Listenin ilk ve son elemanı nedir ?
print(araclar[0], araclar[-1])
# 4- Mazda değerini Toyota ile değiştirin.
araclar[-1] = "Toyota"
print(araclar)

# 5- Mercedes listenin bir elemanı mıdır ?

durum = "Mercedes" in araclar
print(durum)

#  Listenin son 2 elemanı yerine "Totoya" ve "Renault" değerlerini ekleyin.

araclar[-2:] = "Toyota","Ranault"

print(araclar)

# 9 Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
araclar.append("audi")
araclar.append("Nşssan")
print(araclar)


print(araclar[::-1])

