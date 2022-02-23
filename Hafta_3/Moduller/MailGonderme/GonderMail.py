
# Google Güvenli erişim kapatılması gerekmektedir. Aşağıdaki linlten kapatabilirsiniz.
# https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4PvBJSlJA155OqwhiSPaFe9OzLSvMoZn2clBmlUTOf42XxQIr4mcMx3iOM2eBINvLw8vk1fzhVvCIGgvrNStlCZoGkPxg
def mailGonder(eposta,sifre,kime,mesaj):
    import smtplib
    sunucu = smtplib.SMTP("smtp.gmail.com", 587)
    sunucu.ehlo()
    sunucu.starttls()
    sunucu.login(eposta, sifre)
    to = [kime]
    mesaj = mesaj
    try:
        sunucu.sendmail(eposta, to, mesaj)
        print("Mail Gönderme Başarılı")
    except:
        print("Hata Aldık")
    sunucu.quit()


