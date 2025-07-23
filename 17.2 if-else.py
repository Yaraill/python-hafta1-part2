hava = input("Lütfen hava durumunu giriniz (güneşli, yağmurlu, karlı): ").lower()

if hava == "güneşli":
    print("Bugün dışarıda yürüyüş yapabilirsiniz.")

elif hava == "yağmurlu":
    print("Bugün evde kitap okuyabilirsiniz.")

elif hava == "karlı":
    print("Bugün kar topu oynayabilirsiniz.")

else:
    print("Lütfen geçerli bir hava durumu giriniz: güneşli, yağmurlu veya karlı.")
