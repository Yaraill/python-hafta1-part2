gun = input("Lütfen gün giriniz (Pazartesi, Salı, Çarşamba, Perşembe, Cuma, Cumartesi, Pazar): ").lower()
yas = int(input("Lütfen yaşınızı giriniz: "))

if gun == "çarşamba":
    print("Bugün sinemada Halk günü! Tüm Biletler 100TL.")

elif gun == "cuma":
    if yas < 18:
        print("Bugün sinemada Çocuk Bileti 100TL.")
    else:
        print("Bugün sinemada Yetişkin Bileti 150TL.")

elif gun == "cumartesi" or gun == "pazar":
    if yas < 18:
        print("Bugün sinemada Çocuk Bileti 120TL.")
    else:
        print("Bugün sinemada Yetişkin Bileti 200TL.")
    
else:
    if yas < 18:
        print("Bugün sinemada Çocuk Bileti 80TL.")
    else:
        print("Bugün sinemada Yetişkin Bileti 120TL.")
