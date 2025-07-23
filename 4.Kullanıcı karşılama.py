ad = input("Adınızı yazınız: ")
soyad = input("Soyadınızı yazınız: ")
title = input("Ünvanınızı yazınız: ")

def kullanici_karsila(kisi_adi, kisi_soyadı, kisi_title):
    print(f"Hoş geldin, {kisi_adi} {kisi_soyadı}!\n{kisi_title}")

kullanici_karsila(ad, soyad, title)