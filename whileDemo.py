#1
#sayilar=[1,3,5,7,9,12,19,21]
# i=0
# #len(sayilar) LISTENIN UZUNLUGUNU ALIYOR
# while (i<len(sayilar)):
#     print(sayilar[i])
#     i+=1

#2
# baslangic=int(input("Başlangıç değeri giriniz: "))
# bitis=int(input("Bitiş değeri giriniz: "))
# while baslangic<=bitis:
#     if baslangic%2==1:
#         print(baslangic)
#     baslangic+=1

#3
# i=100
# while i>=1:
#     print(i)
#     i-=1

#4
# sayilar=[]
# i=0
# while i<5:
#     sayi=int(input("Sayı giriniz: "))
#     sayilar.append(sayi)
#     i+=1
# a=0
# while a<len(sayilar):
#     print(sayilar[a])
#     a+=1

#5
urunSayisi=int(input("Ürün sayısını giriniz: "))
urunListesi=[]
i=0
while i<urunSayisi:
    urunAdi=input("Ürün adını giriniz: ")
    urunFiyati=int(input("Ürün fiyatını giriniz: "))
    urunListesi.append({'name':urunAdi,'price':urunFiyati})
    i+=1
for urun in urunListesi:
    print(f"{urun['name']} --> {urun['price']} TL")
