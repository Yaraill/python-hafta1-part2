premium = input("Premium üyeliğiniz var mı? (Evet/Hayır): ").lower()

if premium == "evet":
    premium = True

else:
    premium = False

sepet = int(input("Sepet tutarını giriniz: "))

if sepet >= 500 or premium == True:
    print("Kargo ücretsiz!")

elif sepet >= 250:
    print("Kargo ücreti 20TL")

else:
    print("Kargo ücreti 40TL")