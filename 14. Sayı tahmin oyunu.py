import random

rastgele = random.randint(1,100)

tahmin_str = input("Lütfen tahmininizi giriniz (1-100 arası): ")
tahmin = int(tahmin_str)

while tahmin != rastgele:
    if tahmin < rastgele:
        print("Daha yüksek bir sayı tahmin et!")

    else:
        print("Daha düşük bir sayı tahmin et!")

    tahmin_str = input("Tekrar deneyin!")
    tahmin = int(tahmin_str)

print(f"Tebrikler! Sayıyı doğru tahmin ettin: {rastgele}")
