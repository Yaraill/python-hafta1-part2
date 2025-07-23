print("Döngü başlıyor...")

for sayi in range(1, 21):

    if sayi == 16:
        print(f"Sayı {sayi} oldu, döngü sonlandırılıyor (break)!")
        break 

    if sayi % 5 == 0:
        print(f"Sayı {sayi}, 5'in katı olduğu için atlanıyor (continue)...")
        continue 

    print(f"Sayı: {sayi}")

print("Döngü bitti.")