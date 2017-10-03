# Kullanıcı girdiği iki sayının büyük olanını ekrana yazdıran program
# 03.10.2017, ders uygulaması

a = eval(input("İlk sayıyı giriniz : "))
b = eval(input("Diger sayıyı giriniz : "))

if a>b:
    print(a," sayısı daha büyüktür")
elif b>a:
    print(b," sayısı daha büyüktür")
else:
    print("Her iki sayı eşittir")

