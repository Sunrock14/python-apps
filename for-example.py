# Rakamları toplamı 13 olan tüm 3 basamaklı sayıların
# ortalamasını bulan program
# 10.10.2017, ders uygulaması

toplam = 0
sayac = 0

for sayi in range(100,1000):
    yuzler = sayi//100   # 100'e bölümündeki tamsayı kısmı
    onlar = (sayi-(yuzler*100))//10
    birler = sayi%10  # sayinin mod 10'u
    bas_top = yuzler+onlar+birler
    if bas_top==13:  # sayinin basamak toplami 13 ise
        print(sayi,end=" ")
        toplam=toplam+sayi
        sayac=sayac+1

ortalama=toplam/sayac
print("İstenen toplam =",toplam)
print("Sayı adedi =",sayac)
print("İstenen ortalama = ",ortalama)
        

