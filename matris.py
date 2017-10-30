# Matris formunda ekran çıktıları
# 31.10.2017, ders uygulaması

n = eval(input("Bir sayı giriniz : "))

for i in range(n):   # satır döngüsü
    for j in range(n): # sütun döngüsü
        print(i+1, end=" ")
    print()  # bir alt satıra geçmek için        
    
print("Ucgen yildiz matrisi-1")

for i in range(n):
    for j in range(n-i):
        print("*", end=" ")
    print()

print("Ucgen yildiz matrisi-2")

for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()

print("Ucgen * + matrisi")

for i in range(n):
    for j in range(i+1):
        if i%2==0:   # i çift sayı ise
            print("*", end=" ")
        else:
            print("+", end=" ")
    print()

# 2011 vize sorusu
for i in range(n):

    print(i+1,end=" ")

    if i%2==0:
        for j in range(n-2):
            print("X", end=" ")
    else:
        for j in range(n-2):
            print("Y", end=" ")
    
    print(i+1)






