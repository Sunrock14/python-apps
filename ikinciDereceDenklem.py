# İkinci derece bir denklemin köklerini bulan program
# ax^2 + b^x + c  denklemindeki a,b,c parametrelerini
# kullanıcı girecek.
# Ders uygulaması, 05.10.2017

import math

# Giriş (a,b ve c katsayılarının kullanıcıdan alınması)
a = eval(input("a katsayısını giriniz : "))
b = eval(input("b katsayısını giriniz : "))
c = eval(input("c katsayısını giriniz : "))

# İşlem ve Sonuç
delta = (b*b)-(4*a*c)
if delta>0:
    kok_delta = math.sqrt(delta)
    x1 = (-b + kok_delta)/(2*a)
    x2 = (-b - kok_delta)/(2*a)
    print("Bu denklemin kökleri ",x1," ve ",x2," dir")
elif delta==0:
    x = -b/(2*a)
    print("Bu denklemin çift katlı kökü olup bu kök ",x," dir")
else:
    print("Bu denklemin R sisteminde kökü yoktur")








    
