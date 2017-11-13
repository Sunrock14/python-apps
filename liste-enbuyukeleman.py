# Bir listenin en büyük elemanının bulunması
# 07.11.2017, ders uygulaması

import random

a=[]   # Boş liste
for i in range(10):
    r = random.randint(10,99)  # sayıların 2 rakamlı olması istendiği için
    a.append(r)

print(a)

eb=a[0]  # Listenin ilk elemanını en büyük kabul et
for i in range(1,10):   #Listenin geri kalanı için
    if a[i]>eb:
        eb=a[i]

print("Bu listenin en büyük elemanı = ",eb)


        
    










