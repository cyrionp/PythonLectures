#1 Ekranda "Merhaba Dünya" yazdır
#2 Kullanıcı adını al, "Merhaba, kullanıcı adı" yazdır
#3 Girilen 2 sayıyı topla yazdır
#4 Girilen 2 sayının ortalamasını al yazdır
#5 Girilen vize-final not ortalamasını yazdır (%40-%60)
#6 Girilen 3 yazılı notunun ortalamasını yazdır
#7 Yazılı ortalaması girilen öğrencinin sınıf geçme durumu
#8 Girilen sayının tek mi çift mi olduğunu yazdır
#9 Girilen sayının + - 0 olduğunu bul yazdır
#10 Yaşı girilen kişinin ehliyet alıp alamayacağını yazdır

'''
#1))

print("Merhaba Dünya")

#2))
isim=input("Kullanıcı adını giriniz: ")
print(f"Merhaba, {isim}")

#3))
sayi1=int(input("İlk sayıyı giriniz: "))
sayi2=int(input("İkinci sayıyı giriniz: "))
print(f"Girdiğiniz sayıların toplamı: {sayi1+sayi2}")

#4))
sayi1=int(input("İlk sayıyı giriniz: "))
sayi2=int(input("İkinci sayıyı giriniz: "))
ort=(sayi1+sayi2)/2
print(f"Girdiğiniz iki sayının ortalaması: {ort}")

#5))
vize=int(input("Vize notunu giriniz: "))
final=int(input("Final notunu giriniz: "))
ort=(vize*0.4)+(final*0.6)
print(f"Ortalamanız: {ort}")
if ort>=60:
    print("Geçtiniz")
else:
    print("Kaldınız")

#6))
yazili1=int(input("1. yazılı notu giriniz: "))
yazili2=int(input("2. yazılı notu giriniz: "))
yazili3=int(input("3. yazılı notu giriniz: "))
ort=(yazili1+yazili2+yazili3)/3
print(f"Ortalamanız: {ort}")

#7))
ort=float(input("Ortalamayı giriniz: "))
if ort>=60:
    print("Geçtiniz.")
else:
    print("Kaldınız.")

#8))
sayi=int(input("Sayı giriniz: "))
if sayi%2==0:
    print(f"{sayi}, çift bir sayıdır")
else:
    print(f"{sayi}, tek bir sayıdır")

#9))
sayi=int(input("Sayı giriniz: "))
if sayi>0:
    print(f"{sayi}, pozitiftir")
elif sayi<0:
    print(f"{sayi}, negatiftir")
else:
    print("Girdiğiniz sayı 0'dır")

#10))
yas=int(input("Yaşınızı giriniz: "))
if yas>=18:
    print("Ehliyet alabilirsiniz")
else:
    print("Ehliyet alamazsınız")
'''

#1 1-100 arasındaki sayıları alt alta yazdır
#2 1-100 arasındaki çift sayıları alt alta yazdır
#3 1-100 arasındaki tek sayıları alt alta yazdır
#4 1-100 arasındaki 3'e ve 5'e tam bölünen sayıları yazdır
#5 1'den girilen sayıya kadar yazdır
#6 Kenarları girilen dd alanı ve çevresini yazdır
#7 Girilen metnin harflerini alt alta yazdır
#8 Girilen iki sayı arasındaki tüm sayıların toplamı
#9 Girilen sayının asal mı değil mi olduğunu yazdır
#10 1'den girilen sayıya kadar olan tüm tek ve çift toplamı

'''
#1))
for x in range(1,101):
    print(x)

#2))
for x in range(1,101):
    if x%2==0:
        print(x)

#3))
for x in range(1,101):
    if x%2!=0:
        print(x)

#4))
for x in range(1,101):
    if x%3==0 and x%5==0:
        print(x)

#5))
bitis=int(input("Bitiş sayısını giriniz: "))
for x in range(1,bitis+1):
    print(x)

#6))
kenar1=int(input("Dikdörtgenin bir kenarını giriniz: "))
kenar2=int(input("Dikdörtgenin diğer kenarını giriniz: "))
cevre=kenar1*2+kenar2*2
alan=kenar1*kenar2
print(f"Dikdörtgenin çevresi: {cevre} ve alanı: {alan}'dır.")

#7))
metin=input("Metin giriniz: ")
for harf in metin:
    print(harf)

#8))
sayi1=int(input("İlk sayıyı giriniz: "))
sayi2=int(input("İkinci sayıyı giriniz: "))
toplam=0
for x in range(sayi1,sayi2+1):
    toplam+=x
print(f"Girdiğiniz sayılar arasındaki sayıların toplamı: {toplam}")

#9))
sayi=int(input("Sayı giriniz: "))
sayac=0
for x in range(2,sayi):
    if sayi%x==0:
        sayac+=1
        break
if sayac!=0:
    print(f"{sayi}, asal değildir.")
else:
    print(f"{sayi}, asaldır.")

#10))
sayi=int(input("Sayı giriniz: "))
tekToplam=0
ciftToplam=0
for x in range(1,sayi+1):
    if x%2!=0:
        tekToplam+=x
    else:
        ciftToplam+=x
print(f"Tek sayıların toplamı: {tekToplam}")
print(f"Çift sayıların toplamı: {ciftToplam}")
'''

#Tümünü fonksiyon kullanarak yap
#1 Maaşı ve zam oranı girilen işçinin zamlı maaşını yaz
#2 Fonk kullan yarıçapı girilen daire alanı yaz
#3 Fonk kullan genişliği ve yüksekliği verilen alanı yaz
#4 random ile sayı tahmin oyunu yap (hak yok)
#5 verilen tarihin, o yılıncı kaçıncı günü olduğunu yaz
#6 bir liste içinde 5'in katları olan sayıları yaz
#7 Fonk string içinde istenen karakterden kaç tane old yaz
#8 Fonk girilen 2 sayı arasındaki çift sayıların ort bul
#9 Veri tabanından kayıt oku
#10 tkinter form kullan

'''
#1))
def zam(sayi):
    zamliMaas=sayi+sayi*(zamOrani/100)
    zamMiktari=sayi*(zamOrani/100)
    print(f"Yapılan zam miktarı {zamMiktari} TL, zamlı maaşınız ise {zamliMaas} TL")
maas=float(input("Maaşınızı yazın: "))
zamOrani=float(input("Zam oranınızı yazın: "))
zam(maas)

#2))
def daireAlani(sayi):
    pi=3.14
    alan=pi*sayi*sayi
    print(f"Dairenin alanı {alan}")
yaricap=float(input("Yarıçapı girin: "))
daireAlani(yaricap)

#3))
def Alan(gen,yuk):
    alanimiz=gen*yuk
    print(f"Alan: {alanimiz}")
genislik=float(input("Genişliği girin: "))
yukseklik=float(input("Yüksekliği girin: "))
Alan(genislik,yukseklik)

#4))
import random
def tahmin():
    sefer=0
    uretilen=random.randint(1, 101)
    while True:
        sayi=int(input("1-100 arası tahmininizi yazın: "))
        if sayi!=uretilen:
            sefer+=1
            if sayi<uretilen:
                print("Yukarı")
            else:
                print("Aşağı")
        else:
            print("Tahmininiz doğru!")
            break
    print(f"Tam {sefer}. seferde doğru cevabı buldunuz.")
tahmin()
'''
