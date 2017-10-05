# Kenar uzunlukları (a,b,c) girilen bir üçgenin
# eşkenar, ikizkenar veya çeşitkenar olduğunu bulan program
# 05.10.2017, ders uygulaması

# Giriş
a = eval(input("a kenar uzunluğunu giriniz : "))
b = eval(input("b kenar uzunluğunu giriniz : "))
c = eval(input("c kenar uzunluğunu giriniz : "))

# İşlem ve Sonuç
if a==b and a==c:  # Her 3 kenar da birbirine eşit ise
    print("Bu üçgen EŞKENAR üçgendir")
elif a==b or a==c or b==c:  #Bu 3 koşuldan herhangi biri doğruysa
    print("Bu üçgen İKİZKENAR üçgendir")
else:  # Geriye kalan tek durum: tüm kenarlar farklı
    print("Bu üçgen ÇEŞİTKENAR üçgendir")

        
        

