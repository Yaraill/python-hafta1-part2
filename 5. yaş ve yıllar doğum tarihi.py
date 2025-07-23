import datetime

current_year = datetime.datetime.now().year

yas_str = input("Lütfen yaşınızı girin: ")
kullanici_yasi = int(yas_str)

dogum_yili = current_year - kullanici_yasi

print(f"Doğum yılınız {dogum_yili} yılıdır.")