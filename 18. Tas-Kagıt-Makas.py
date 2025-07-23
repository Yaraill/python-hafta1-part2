import random
print("--- Taş Kağıt Makas Oyunu ---")

bilgisayar_secim = random.choice(["taş", "kağıt", "makas"])

secim = input("Taş, Kağıt veya Makas seçin: ").lower()

if bilgisayar_secim == secim:
    print(f"Beraberlik! Bilgisayar da {bilgisayar_secim} seçti.")

elif (bilgisayar_secim == "taş" and secim == "makas") or  (bilgisayar_secim == "kağıt" and secim == "taş") or (bilgisayar_secim == "makas" and secim == "kağıt"):
    print(f"Kayıp! Bilgisayar {bilgisayar_secim} seçti.")

else:
    print(f"Kazandınız! Bilgisayar {bilgisayar_secim} seçti.")