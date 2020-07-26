#Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyon
#Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyon
#Gönderilen 2 sayı arasındaki tüm asal sayıları bulan ve yazdıran fonksiyon
#Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyon

'''
#1
def kelimeGoster(kelime,kez):
    print(kelime*kez)

kelime=input("Kelime giriniz: ")
kez=int(input("Kaç kez yazılsın?: "))
kelimeGoster(kelime,kez)

#2
def myFunc(*args):
    myList=[]
    for arg in args:
        myList.append(arg)
    print(myList)

myFunc(12,32,5324,1231,232,123,22)

#3
def asalSayiBulucu(ilk,son):
    for sayi in range(ilk,son+1):
        if sayi>1:
            for i in range(2,sayi):
                if sayi%i==0:
                    break
                else:
                    print(sayi)

sayi1=int(input("İlk sayıyı giriniz: "))
sayi2=int(input("İkinci sayıyı giriniz: "))
asalSayiBulucu(sayi1,sayi2)
'''
#4
def tamBolenBulucu(sayi):
    listTamBolenler=[]
    for i in range(1,sayi+1):
        if sayi%i==0:
            listTamBolenler.append(i)
    print(f"\n{sayi} sayısına ait tam bölenler: \n")
    for bolen in listTamBolenler:
        print(bolen)
    print(f"\n{sayi} sayısının toplam {len(listTamBolenler)} tane tam böleni vardır.")
    if len(listTamBolenler)==2:
        print("Girdiğiniz sayı asaldır.")

sayi=int(input("Sayı giriniz: "))
tamBolenBulucu(sayi)
