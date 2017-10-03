# Vize1 (%20), Vize2 (%30) ve Final(%50) notları girildiğinde
# başarı durumunu hesaplayan program

# Giriş
v1 = eval(input("1. vize notunu giriniz : "))
v2 = eval(input("2. vize notunu giriniz : "))
f = eval(input("Final notunu giriniz : "))

# İşlem
basari = (v1*0.2)+(v2*0.3)+(f*0.5)

#Sonuç
print("Bu dersten başarı notunuz : ",basari)

if basari >= 85:
    n="A"
elif basari >= 70:
    n="B"
elif basari >= 55:
    n="C"
elif basari >= 40:
    n="D"
else:
    n="F"
    
print ("Harf Notu : ",n)
print("Program sonlandı.")










