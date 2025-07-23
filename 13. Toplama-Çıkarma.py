sayi1_str = input("Lütfen ilk sayıyı giriniz: ")
sayi2_str = input("Lütfen ikinci sayıyı giriniz: ")

sayi1 = int(sayi1_str)
sayi2 = int(sayi2_str)

def toplama(sayi1, sayi2):
    sonuc_t = sayi1 + sayi2
    return sonuc_t

def cıkarma(sayi1, sayi2):
    sonuc_c = sayi1 - sayi2
    return sonuc_c

toplama_sonucu = toplama(sayi1, sayi2)
cikarma_sonucu = cıkarma(sayi1, sayi2)

print(f"Toplama sonucu: {toplama_sonucu}")
print(f"Çıkarma sonucu: {cikarma_sonucu}")