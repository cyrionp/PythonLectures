#ÜRÜNLER BÖLÜMÜ
import random
kategoriler={
             'Telefon':{
                  'Tuşlu':
                      {'Nokia C1':100,'Nokia C2':200,'Nokia C3':450,'Nokia A10':350,'Nokia A20':600},
                  'Akılı':
                      {'iPhone 7':3000,'Samsung Galaxy S8':5500,'Huawei Mate X':32000,'iPhone 11':6500,'Xiaomi Mi 10':4900},
                  'Telsiz':
                      {'Huawei':100,'Model 2':200,'Model 3':300,'Model 4':400,'Model 5':500}},
             'Bilgisayar':{
                  'Masaüstü':
                      {'Acer Aspire 15':4000,'Casper Nirvana 200':6000,'Lenovo Thinkpad 12':9900,'HP NB122i7':15000,'Apple Mac Pro':42000},
                  'Dizüstü':
                      {'Apple MacBook Air':12000,'Acer Swift 3':5500,'Casper S500':4300,'Lenovo Legion 17':23000,'HP Omen 20':20000},
                  'Tablet':
                      {'iPad Pro':15000,'Samsung Tab 5':3320,'iPad Air':1900,'Casper eTab4':400,'Huawei TabTab11':3900}},
             'Kulaklık':{
                  'Bluetooth':
                      {'QCY T2C':200,'Airpods Pro':2000,'Samsung Earbuds':850,'JBL Pro TWS':3000,'Sony SNY20BT':1400},
                  'Kulaküstü':
                      {'QCY E3':100,'Philips Term 844':290,'Samsung AKG212':450,'JBL Pro Sync':1500,'Sony SNY22':900},
                  'Kulakiçi':
                      {'QCY I4T':90,'Beats Shine 2':300,'AKG A8484':250,'JBL Sense Lite':70,'Sony 1664R':200}},
             'Aksesuarlar':{
                  'Kılıf':
                      {'Silikon 2. Kalite':20,'Silikon 1. Kalite':30,'Sert Plastik':40,'Spigen Armor':70, 'Spigen Army':120},
                  'Kırılmaz cam':
                      {'Model 1':20,'Model 2':30,'Model 3':40,'Model 4':70, 'Model 5':120},
                  'Şarj aleti':
                      {'Zamzunk 5 Watt':20,'ChargerChina 10 Watt':30,'Huawei 18 Watt':40,'Samsung 27 Watt':70, 'Apple 5 Watt':120}},
             'Televizyon':{
                  'Akıllı':
                      {'Acer FAW4664':4000,'Philips PHL123':6000,'Samsung AAA313AV':9900,'LG L1F35G00D':15000,'Sony 50NY20':42000},
                  '4K':
                      {'Acer FAW4444':2000,'Philips PHL423':3500,'Samsung AAA414AK-T':3000,'LG LIF34L1V3':2600,'Sony Bravia Pro 894':4200},
                  'Normal':
                      {'Acer FA12':400,'ViewSonic Sonic Lite':600,'Arçelik Ultram 2':900,'LG SAL43-22':1500,'Sony Bravia Lite 874':2000}}}
#MARKET BÖLÜMÜ
sepet={}
tutar=0
print("TorosMarkt Teknoloji Mağazasına Hoşgeldiniz!")
print("-------------------------------------------------------------------")
alisveris=int(input("Alışveriş için 1, çıkmak için 0 giriniz: "))
if alisveris!=1:
    print("-------------------------------------------------------------------")
    print("Alışveriş yapabilmek için programı yeniden çalıştırın")
    print("**************************************")
else:
    while True:
        a=1
        b=1
        c=1
        d=1
        e=1
        print("-------------------------------------------------------------------")
        for kat in kategoriler.keys():
            print(str(a)+"->",kat)
            a+=1
        print("-------------------------------------------------------------------")
        secilenKategori=int(input("Lütfen Kategori Seçiniz: "))-1
        print("-------------------------------------------------------------------")
        if secilenKategori<0 or secilenKategori>4:
            print("Yanlış seçim yaptınız.")
        else:
            secilenKategori=[*kategoriler][secilenKategori]
            altKategori=kategoriler[secilenKategori]
            for secKat in altKategori.keys():
                print(str(b)+"->",secKat)
                b+=1
            print("-------------------------------------------------------------------")
            secilenAltKategori=int(input("Lütfen Alt Kategori Seçiniz: "))-1
            if secilenAltKategori<0 or secilenAltKategori>2:
                print("Yanlış seçim yaptınız.")
            else:
                print("-------------------------------------------------------------------")
                secilenAltKategori=[*altKategori][secilenAltKategori]
                altAltKategori=altKategori[secilenAltKategori]
                for secAltKat in altAltKategori.keys():
                    print(str(c)+"->",secAltKat,"->",altAltKategori[secAltKat],"TL")
                    c+=1
                print("-------------------------------------------------------------------")
                secilenUrun=int(input("Lütfen Ürün Seçiniz: "))-1
                if secilenUrun<0 or secilenUrun>4:
                    print("Yanlış seçim yaptınız.")
                else:
                    print("-------------------------------------------------------------------")
                    secilenUrunum=[*altAltKategori][secilenUrun]
                    secilenUrunFiyat=altAltKategori[secilenUrunum]
                    sepet.update( {secilenUrunum : secilenUrunFiyat} )
                    tutar+=secilenUrunFiyat
                    print("Sepetinizdeki ürünlerin toplam fiyatı: ",tutar,"TL")
                    print("-------------------------------------------------------------------")
                    devam=input("Alışverişe devam etmek için 1, sepetinize gitmek için 0 girin: ")
                    if int(devam)!=1:
                        break
#KULLANICI BİLGİLERİ
kullaniciInfo={}
if alisveris==1:
    print("-------------------------------------------------------------------")
    print("********** SEPETİNİZDEKİLER **********")
    print(" ")
    for sepettekiler in sepet:
        print(str(d)+"->",sepettekiler+" ->",str(sepet[sepettekiler])+(" TL"))
        d+=1
    print("-------------------------------------------------------------------")
    print("Toplam tutar: ",tutar,"TL")
    odemeYontemleri=('Kapıda Ödeme','Kredi Kartıyla Ödeme','Hediye Kartı')
    print("-------------------------------------------------------------------")
    for yontem in odemeYontemleri:
        print(str(e)+"->",yontem)
        e+=1
    print("-------------------------------------------------------------------")
    def robotKontrol():
        while True:
            kontrol=random.randint(1000, 9999)
            print("-------------------------------------------------------------------")
            print("Robot Kontrol: ",kontrol)
            print("-------------------------------------------------------------------")
            girisKontrol=int(input("Ekrandaki Sayıyı Giriniz: "))
            print("-------------------------------------------------------------------")
            if girisKontrol!=kontrol:
                print("Hatalı Kod Girdiniz. Tekrar Deneyin.")
            else:
                print("Kontrol Başarılı.")
                break
    def bilgiYazdir():
        f=1
        print("-------------------------------------------------------------------")
        print("*********KULLANICI BİLGİLERİ**********")
        for info in kullaniciInfo.keys():
            print(info+":",kullaniciInfo[info])
            f+=1
        print("-------------------------------------------------------------------")
    def bilgiAlma():
        ad=input("Adınızı girin: ")
        kullaniciInfo.update({'Ad':ad})
        soyad=input("Soyadınızı girin: ")
        kullaniciInfo.update({'Soyad':soyad})
        telefon=input("Telefon numaranızı girin: ")
        kullaniciInfo.update({'Telefon':telefon})
        eposta=input("Eposta adresinizi girin: ")
        kullaniciInfo.update({'Eposta':eposta})
        adres=input("Adresinizi girin: ")
        kullaniciInfo.update({'Adres':adres})

    print("-------------------------------------------------------------------")
    while True:
        odemeYontemi=int(input("Ödeme Yöntemi Seçiniz: "))
        if odemeYontemi==1:
            bilgiAlma()
            robotKontrol()
            bilgiYazdir()
            break
        elif odemeYontemi==2:
            bilgiAlma()
            print("-------------------------------------------------------------------")
            kredi=input("Kredi Kart Numarası: ")
            sonk=input("Kart Son Kullanma (AA/YY) Tarihi: ")
            cvv=input("Kredi Kartı CVV: ")
            robotKontrol()
            telkod=input("Telefonunuza Gelen Kodu Girin: ")
            bilgiYazdir()
            break
        elif odemeYontemi==3:
            bilgiAlma()
            input("Hediye Kartı Seri No Girin: ")
            robotKontrol()
            bilgiYazdir()
            break
        else:
            print("Hatalı seçim yaptınız.")
    print("Ödemeniz tamamlanmıştır.")
print("Yine bekleriz :)")
input("")#Program doğrudan kapanmasın diye yazdım
