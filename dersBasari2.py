# Vize1 (%20), Vize2 (%30) ve Final(%50) notları girildiğinde

# Giriş
v1 = eval(input("1. vize notunu giriniz : "))
v2 = eval(input("2. vize notunu giriniz : "))
f = eval(input("Final notunu giriniz : "))

# İşlem
basari = (v1*0.2)+(v2*0.3)+(f*0.5)

#Sonuç
print("Bu dersten başarı notunuz : ",basari)

if basari>=50:    # eğer başarı notu 50'den büyük eşitse
    print("TEBRİKLER ! GEÇTİNİZ !")  # bu mesajı yazdır

if basari<50:
    print("MALESEF BAŞARILI OLAMADINIZ :(")  

print("Program sonlandı.")










