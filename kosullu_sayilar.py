# Kullanıcı 0 girene dek (0 girmediği sürece), girmiş olduğu tüm sayıların
# bir listeye alınması ve toplamının bulunması

sayilar=[]
a=1   # en başta döngüye girebilmek için a 0'dan farklı olmalı
i=1   # girilen sayı adedi
while a!=0:     # a sayısı 0 olmadığı sürece
    print(i,". sayıyı giriniz (bitirmek için 0) : ",end="")
    a=eval(input(""))
    if a!=0:
        sayilar.append(a)
        i=i+1
    else:
        print("0 sayısını girdiniz. İşlem sonlanıyor!")

print(sayilar)

# sayilar listesinin toplamının bulunması
toplam=0
for i in range(len(sayilar)):
    toplam=toplam+sayilar[i]


print("Listedeki sayıların toplamı = ",toplam)










