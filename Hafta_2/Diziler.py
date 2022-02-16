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