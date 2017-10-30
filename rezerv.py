# Kömür rezerv sorusu
# 31.10.2017, ders uygulaması

rezerv=2000
isci=50
ton=0.8
gun=0

while rezerv>0:
    gun=gun+1
    rezerv = rezerv - (isci*ton)
    print(gun,". gün sonunda kalan kömür miktarı = ",rezerv)
    if gun%7==0:  # gün=7,14,21... ise
        ton=ton+0.1

print("bu rezerv toplam ",gun," sonunda tükenir")

        
