#1
'''
a=int(input("Sayı gir birader: "))
if a<100 and a>0:
    print("Tabi ki de lann")
else:
    print("BAŞŞARAMADIK AAABİ")
'''
#2
'''
a=int(input("Kardeş sayı girer misin aq?: "))
if a>0 and a%2==0:
    print(f"Helal len\n{a}, hem pozitif hem de çift")
else:
    print("NEYİ BAŞŞŞŞARAMADIN??")
'''
#4
'''
a=int(input('İlk sayı: '))
b=int(input('İkinci sayı: '))
c=int(input('Üçüncü sayı: '))
buyukluk1=(a>b) and (a>c)
print(f"a, en büyük sayıdır: {buyukluk1}")
buyukluk2=(b>a) and (b>c)
print(f"b, en büyük sayıdır: {buyukluk2}")
buyukluk3=(c>a) and (c>b)
print(f"c, en büyük sayıdır: {buyukluk3}")
'''
#5
'''
vize1=float(input("Vize notu giriniSSS: "))
vize2=float(input("Vize notu giriniSSS: "))
final=float(input("Final notu giriniSSS: "))
ortalama=((vize1+vize2)/2)*0.6+final*0.4
print(ortalama)
if ortalama>=50 and final>=50 and final<70:
    print("GEÇTİN LAN HADİ YİNE İYİSİNSSS")
elif final>=70:
    print("FİNALİN İYİYMİŞ GEÇTİNSSSS")
else:
    print("BAŞŞŞŞŞŞŞARAMADINSS")
'''
#6
ad=input("Adınız: ")
kilo=float(input("Kilonuz: "))
boy=float(input("Boyunuz: "))
index=kilo/(boy**2)
print(index)
if index<18.5:
    print("ZAYIFSIN ZALIMSIN")
elif index<25 and index>=18.5:
    print("NORMALSİN")
elif index<30 and index>=25:
    print("FAZLA KİLOLARIN VAR TOMBİŞ")
elif index<35 and index>=30:
    print("AĞIR YAŞAMLAR ŞİMDİ NE YAPIYOR?")
else:
    print("hesaplayamadım len")
