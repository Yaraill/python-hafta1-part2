kenar = input("Lütfen kenar sayısını giriniz: ")

if kenar == "3":
    print("Üçgen")

elif kenar == "4":
    print("Dörtgen")

elif kenar == "5":
    print("Beşgen")

elif kenar == "6":
    print("Altıgen")

else:
    if kenar in ["0", "1", "2"]:
        print("Bu mümkün değil")
    else:
        print(f"Kenar sayısı: {kenar}gen")
