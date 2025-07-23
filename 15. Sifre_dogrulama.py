sifre = "123456"
email = "hyasirpost@gmail.com"
username = "yarail"

username_dogrulama = input("Lütfen kullanıcı adınızı ya da mailinizi giriniz: ")
sifre_dogrulama = input("Lütfen şifrenizi giriniz: ")

sonuc = sifre_dogrulama == sifre and (username_dogrulama == email or username_dogrulama == username)

if sifre != sifre_dogrulama:
    print("Şifreniz yanlış!")

elif username_dogrulama != email and username_dogrulama != username:
    print("Kullanıcı adınız ya da mailiniz yanlış!")

else:
    print("Giriş başarılı!")

