# Bir dik üçgenin dik kenarları girildiğinde hipotenüsü hesaplayan program
# 03.10.2017, ders uygulaması

import math  # Matematik kütüphanesi (modülü)

# Bilgi girişi
a = eval(input("a kenarının uzunluğunu giriniz :"))
b = eval(input("b kenarının uzunluğunu giriniz :"))

# İşlem
c=(a*a)+(b*b)
hipotenus = math.sqrt(c)

# Sonucu ekrana yazdırma
print("Dik kenarları ",a," ve ",b," olan dik üçgenin hipotenüsü : ",hipotenus)











