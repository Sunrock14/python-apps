# Kullanıcı girdiği iki sayının büyük olanını ekrana yazdıran program
# 03.10.2017, ders uygulaması

a = eval(input("İlk sayıyı giriniz : "))
b = eval(input("Diger sayıyı giriniz : "))

if a>b:
    print(a," sayısı daha büyüktür")

if b>a:
    print(b," sayısı daha büyüktür")

if a==b:
    print("Her iki sayı eşittir")

