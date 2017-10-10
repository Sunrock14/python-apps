# Çevrim yapıları : for döngüsü
# 10.10.2017, ders uygulaması

# 0'dan 49'a kadar olan sayilarin kareleri
for i in range(50):
    print(i," sayisinin karesi = ",i*i)


toplam=0
# 20 ile 45 arası sayıların toplamı
for j in range(20,45):
    toplam=toplam+j
    #print("Ara Toplam =",toplam)

print("20+21+22+...+43+44=",toplam)


print("0-100 arası 3'e bölünebilen sayılar:")
# 0 ile 100 arasında 3'e kalansız bölünebilen sayıların
# yanyana yazdırılması
for i in range(3,100,3):
    if i<99:
        print(i,end='-')
    else:
        print(i)

print("100'den geriye sayma :")
# 100'den geri sayma
for i in range(100,0,-1):
    print(i,end=' ')



    




