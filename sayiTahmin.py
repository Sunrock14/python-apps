# Sayı tahmin oyunu
# 26.10.2017, ders uygulaması

import random
s = random.randint(1,100)
t = eval(input("İlk tahmininiz nedir ? "))
tahmin_no=1

while t!=s:
    if s<t:
        print("Benim sayim daha küçük!")
    elif s>t:
        print("Benim sayim daha büyük!")
    tahmin_no = tahmin_no+1 
    print(tahmin_no,". tahmininiz ? ",end="")
    t = eval(input(""))

# Program döngüden çıktığı anda t=s dir
print("Tebrikler ! Ben de ",s," sayısını tutmuştum !")
print(tahmin_no,". tahminde buldunuz!")





             
