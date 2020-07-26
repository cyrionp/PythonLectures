#1
'''
isim=input("İsim girin: ")
yas=int(input("Yaş girin: "))
egitim=input("Eğitim durumu girin\n(ilkokul, lise, üniversite): ")
ehliyetAlmaDurumu=yas>=18 and (egitim=='lise' or egitim=='üniversite')
if not ehliyetAlmaDurumu:
    if yas<18:
        print("18 yaşından küçükler ehliyet alamaz.")
    if egitim=='ilkokul':
        print("Ehliyet alabilmek için en az lise mezunu olmalısın.")
else:
    print(f"Tebrikler! Ehliyet alabilirsin, {isim}")
'''

#2
'''
yazili1=float(input("İlk yazılı notu: "))
yazili2=float(input("İkinci yazılı notu: "))
sozlu=float(input("Sözlü notu: "))
ortalama=(yazili1+yazili2+sozlu)/3
if ortalama<25 and ortalama>=0:
    print(f"Ortalamanız {ortalama} ve notunuz => 0")
elif ortalama<45 and ortalama>=25:
    print(f"Ortalamanız {ortalama} ve notunuz => 1")
elif ortalama<55 and ortalama>=45:
    print(f"Ortalamanız {ortalama} ve notunuz => 2")
elif ortalama<70 and ortalama>=55:
    print(f"Ortalamanız {ortalama} ve notunuz => 3")
elif ortalama<85 and ortalama>=70:
    print(f"Ortalamanız {ortalama} ve notunuz => 4")
elif ortalama<=100 and ortalama>=85:
    print(f"Ortalamanız {ortalama} ve notunuz => 5")
'''

#3
import datetime
tarih=input("Aracınız hangi tarihte trafiğe çıktı?\n(YY/AA/GG)\n")
tarih=tarih.split('/')
simdi=datetime.datetime.now()
trafigeCikis=datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
fark=simdi-trafigeCikis
print(f"{fark.days} gün olmuş")
if fark.days<=365:
    print("1. servis aralığı")
elif fark.days>365 and fark.days<=365*2:
    print("2. servis aralığı")
elif fark.days>365*2 and fark.days<=365*3:
    print("3. servis aralığı")
else:
    print("Hatalı tarih girdiniz.")
