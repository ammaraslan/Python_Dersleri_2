"""
listeye benzer ama bazı farklılıkları bulunmaktadır.
Parantez kullanılır ()

Parantezli tanımlanabilir örn  a = (1,"ammar",3)

parantezsizde tanımlanabilir örn  a = 1,"ammar",3

Öge çağırma listedeki gibidir.

Tuplelerin elemanı değişmez

Sadece count ve index metotları vardır. Liste gibi değildir

Demetler birleşebilir. t+t2

"""
tuplem = (1,2,"ammar")
print(tuplem.index(2))
print(tuplem.count("ammar"))