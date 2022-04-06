"""##Dictionary( Sözlük )

`ORNEK = {KEY:VALUE}`

Key ve value şeklinde değer alan listelerdir. Aynı key bilgisiyle birden fazla eleman olamaz. Süslü parantez kullanılır {}

72 --> BATMAN

liste yapısına göre tasarlanırsa iki ayrı liste tanımlayıp indexler üzerinden gezinmeler yapılması gerekmektedir.

sehirler = ["batman","istanbul"]

plakalar = [72,34]

sehirler[plakalar.index(72)]

Sıralar uyması gerekiyor bu yüzden karmaşaya sebep olabilir"""

sehirler = {72:"Batman",56:"siirt"}
print(sehirler[72])
print(sehirler[56])
