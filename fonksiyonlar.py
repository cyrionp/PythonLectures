'''
def sayHello(x):
    print('Hello '+x)
name=input("Your name: ")
sayHello(name)
'''
'''
def total(num1,num2):
    return num1+num2

sayi1=int(input("Sayı girin: "))
sayi2=int(input("Sayı girin: "))
print(f"{total(sayi1,sayi2)}")
'''
'''
def SezenSeniCokOzledik(sonGorulme):
    print(f"Tam {2020-sonGorulme} yıldır göremiyk :'(")
    print("SEZEN SENİ ÇOK ÖZLEDİK")

tarih=int(input("Sezen'i son gördüğünüz yıl: "))
SezenSeniCokOzledik(tarih)
'''
def yasHesapla(dogumYili):
    return 2020-dogumYili

def emeklilik(dogumYili,isim):
    '''
    DOCSTRING: Doğum yılınıza göre emekliliğinize kaç yıl kaldığını gösteren program
    INPUT: Doğum yılı
    OUTPUT: Hesaplanan yıl bilgisi
    '''
    yas=yasHesapla(dogumYili)
    emekli=65-yas
    print(f"Sayın {isim}\nYaşınız {yas} ve emekliliğinize {emekli} yıl kaldı")

ad=input("Adınız: ")
dgko=int(input("Doğum Yılınız: "))
emeklilik(dgko,ad)
