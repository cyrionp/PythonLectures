#Bir aracın yakıt tipine göre (benzin, dizel) belirtilen bir mesafede
#ne kadar yakıt masrafı olduğunu hesaplayan uygulamayı yapınız.

# 7.30 TL benzin, 6.65 TL dizel

secim=int(input("1) Benzin  2) Dizel : "))
tuketim=float(input("100 kmdeki ortalama yakıt tüketiminiz: "))/100
km=float(input("Kaç km? : "))
masraf=0
if secim==1:
    masraf=7.30*tuketim*km
elif secim==2:
    masraf=6.65*km
else:
    print("YANLIŞ GİRDİNİZ")

print("Yakıt masrafınız: "+str(masraf)+" TL")
