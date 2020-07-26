sayilar=[1,3,5,7,9,12,19,21]
#1
print("--------------")
for key in sayilar:
    if key%3==0:
        print(key)

#2
print("--------------")
sayilarToplami=0
for sayi in sayilar:
    sayilarToplami+=sayi
print(f"Sayıların toplamı: {sayilarToplami}")

#3
print("--------------")
for sayi in sayilar:
    if sayi%2!=0:
        print(sayi**2)
        print('|')

#4
print("--------------")
sehirler=['kocaeli','istanbul','ankara','izmir','rize']
for sehir in sehirler:
    harfSayisi=0
    for harf in sehir:
        harfSayisi+=1
    if harfSayisi<=5:
        print(sehir)

#5
print("--------------")
urunler=[
    {'name':'S6','price':'3000'},
    {'name':'S7','price':'4000'},
    {'name':'S8','price':'5000'},
    {'name':'S9','price':'6000'},
    {'name':'S10','price':'7000'}
]
toplamFiyat=0
for urun in urunler:
    toplamFiyat+=int(urun['price'])
print(f"Toplam fiyat: {toplamFiyat}")

#6
print("--------------")
for urun in urunler:
    if int(urun['price'])<=5000:
        print(urun['name'])
