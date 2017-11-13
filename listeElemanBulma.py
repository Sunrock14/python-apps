# İki listenin en büyük elemanlarının toplamının bulunması
# 07.11.2017, ders uygulaması

import random

def enBuyukEleman(liste):
    eb=liste[0]
    for i in range(len(liste)):
        if liste[i]>eb:
            eb=liste[i]
    print("bu listenin en büyük elemanı = ",eb)
    return eb


# n: eleman sayisi, a: rastgele sayi alt sinir, b: rastgele sayi üst sınır
def yeniListeOlustur(n,a,b):
    x=[]
    for i in range(n):
        r = random.randint(a,b)
        x.append(r)
    print("Oluşan Liste : ",x)
    return x


# ANA PROGRAM

a = yeniListeOlustur(15,100,199)
eb_a = enBuyukEleman(a)

b = yeniListeOlustur(8,200,299)
eb_b = enBuyukEleman(b)

c = yeniListeOlustur(10,300,399)
eb_c = enBuyukEleman(c)

toplam = eb_a + eb_b + eb_c

print("bu üç elemanin toplami = ",toplam)






        
    










