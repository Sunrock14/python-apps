# listelere döngü ile eleman eklenmesi


# listeye 0-9 arası sayıların eklenmesi
sayilar=[]
for i in range(10):
    sayilar.append(i)
print(sayilar)

# listeye 100-200 arasındaki çift sayıların eklenmesi
cift_sayilar=[]
for j in range(0,50):
    cift_sayilar.append(100+(j*2))
print(cift_sayilar)

# listeye kullanıcının girdiği 10 adet sayının eklenmesi
girilen_sayilar=[]
for i in range(10):
    print(i+1, ". sayıyı giriniz : ",end="")
    a=eval(input(""))
    girilen_sayilar.append(a)
print("Girilen sayilar = ",girilen_sayilar)














