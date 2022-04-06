# Karekter Dizileri
"""Kurum = "BATMAN ÜNİVERSİTESİ"
print(Kurum)
print(Kurum[0:2])
print(Kurum[2:])
print(Kurum[2:-3])"""

"""print(len(Kurum))

j=0
for i in Kurum:
    j=j+1
print(j)

k_dizim = "Semih ASLAN"

print(k_dizim[0:5])
print(k_dizim[6:])
print(k_dizim[::])
print(k_dizim[::2])
print(k_dizim[::3])
print(*reversed(k_dizim))
print(k_dizim[::-1])

deger = "BATMAN ÜNİVERSİTESİ"
print(deger.upper())
print(deger.lower())
print(deger.count("A"))
print(deger.title())
yenideger = deger.replace("BATMAN", "SİİRT")
print(yenideger)
"""

# Split Komutu

Kurum = "BATMAN, ANKARA, Adana, İzmir, Siirt, Antalya"

arr = Kurum.split(", ")

for i in arr:
    print(i.upper())


# Strip Komutu
isim = "****AMMAR****"
print(isim.strip("*"))
