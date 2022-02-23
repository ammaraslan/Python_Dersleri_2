# # sehirler = {}
# # sehirler[72] = "BATMAN";
# # print(sehirler[72])
#
# sehirler = {72:"BATMAN",56:"Siirt",34:"İstanbul"}
# # for sehir in sehirler:
# #     print(sehir)
# # for sehir in sehirler:
# #     print(sehirler[sehir])
#
# sehirler[6] = "Ankara"
# sehirler[72] = "Batman"
#
# sehirler.pop(56)
#
# for sehir in sehirler:
#     print(sehirler[sehir])

Ogrenciler = {
    15: {
        "Adı":"Ammar",
        "Soyadı":"ASLAN",
        "Yas":17
    }
    ,16: {
        "Adı":"Abdullah",
        "Soyadı":"Manap"
    }
}
# print(Ogrenciler[15]["Adı"])
# print(Ogrenciler[15]["Soyadı"])
# print(Ogrenciler[15]["Yas"])

for ogrenci in Ogrenciler:
    print(Ogrenciler[ogrenci]["Adı"])