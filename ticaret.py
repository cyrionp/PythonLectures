kategoriler= {
    'elektronik':{
                 'telefon':{'iphone xr':6000,'samsung galaxy a10':1400, 'iphone 8':5000,'redmi 6a':1300,'galaxy a50':2800},
                 'bilgisayar':{'lenovo':4000,'msı':6000,'hp':3500,'casper':3000,'macair':8000},
                 'televizyon':{'vestel':2000,'lg':3500,'arcelik':2200,'beko':1750,'samsung':5000},
                 'beyaz eşya':{'buzdolabı':5000,'fırın':1500,'camasir makinesi':3000,'bulasik makinesi':2500,'mikro dalga':1000}
                 },
    'otomotiv':{
                'aksesuar':{'paspas':150,'silecek':10,'motor yağı':200, 'lastik':1000, 'akü':350},
                'yedek parça':{'far':1000,'buji':150,'balata':400,'filtre seti':75, 'seyahat ürünleri0':250},
                'lastik-jant':{'petlas':1000,'lassa':1200,'michelen':2000,'continental':2200,'good year':1750},
                'ses sistemleri':{'pioner':1000,'navitech':1500,'navigold':2000,'altech':750,'jameson':2500},
                'navigasyon':{'audiomax':1500,'roadstar':1200,'ava':1000,'necvox':1600,'hardward':550}
                },
    'spor-outdoor':{
               'fitnes-kondisyon':{'magnum kosu bandı':5500,'fox kosu bandı':2500,'runped bisiklet':2000,'sprit bisiklet':8000,'voit bisiklet':6000},
               'spor giyim':{'a1':1000,'b2':1200,'c1':1300,'d1':1400,'e1':1500},
               'outdoor-kamp':{'yağmurluk':1000,'mont':1200,'kamp çadırı':1300,'mat':1400,'ayakkabı':1500},
               'su sporları':{'kano':1000,'kano oturağı':1200,'dalış elbisesi':1300,'dalış seti':1400,'bodyboard':1500},
               'kış sporları':{'kar maskesi':1000,'kayak eldiveni':1200,'yüz maskesi':1300,'kayak pantalon':1400,'kayak ekipmanları':1500}
    },
    'evmalzemeleri':{
              'mobilya':{'gardrop aksesuarları':1000,'tv ünitesi':1200,'elbise dolabı':1300,'ayna':1400,'ayakkabılık':1500},
              'dekorasyon':{'kitaplık':1000,'avize':1200,'kanvas tablo':1300,'konsol dolap':1400,'sehpa':1500},
              'yapı market':{'klozet':1000,'lavobo':1200,'askılık':1300,'fayans m2':20,'çimento 1 torba':12},
              'kırtasiye':{'tükenmez kalem':1000,'a4 kağıt':1200,'foksiyonlu kalem':1300,'yapıştırıcı':1400,'defter':1500},
              'supermarket':{'Dergi':1000,'ekmek':1,'tavuk bonfile':20,'et 1 kg':55,'bisküvi':1500}
    },
    'giyim':{
             'erkek giyim':{'ayakkabı':1000,'gömlek':1200,'t shirt':1300,'kemer':1400,'kol düğmesi':1500},
             'kadın giyim':{'elbise':1000,'şort':1200,'etek':1300,'kadın ayakkabı':1400,'çanta':1500},
             'çocuk giyim':{'uyku tulumu':1000,'çocuk çorap':1200,'çocuk ayakkabısı':1300,'çocuk zıbın':1400,'çocuk şapka':1500},
             'gözlükler':{'ray ban':1000,'calvin klein':1200,'lacoste':1300,'heritage':1400,'marc jacops':1500},
    }
}
sepetim=[]
tutar=0
durum=True
print('MD E-Ticaret Sitesine Hoşgeldiniz..!')
programgiris=int(input("Alışveriş yapmak için (1), çıkış yapmak için (0) giriniz: "))
while durum:
    if programgiris!=1:
        break
    else:
        print(kategoriler.keys())
        kategorisec=input('Bir kategori seçiniz: ')
        print(kategoriler[kategorisec].keys())
        kategorialtmenusec=input('Bir alt kategori seçiniz:')
        print(kategoriler[kategorisec][kategorialtmenusec].keys())
        secilenurunler=input('Bir ürün seçiniz...')
        secilenurunfiyat=kategoriler[kategorisec][kategorialtmenusec][secilenurunler]
        sepetim.append(secilenurunler)
        tutar=tutar+secilenurunfiyat
        devametmek=int(input("Siparişiniz alındı.. Alışverişe devam etmek isterseniz (1) basınız', istemiyorsanız (2) basınız..."))
        if devametmek!=1:
            break
if programgiris==1:
    print("Sepetinizdeki Ürünler:", sepetim)
    print("Ürünlerin Toplam Tutarı:",tutar)
    print("Lütfen müşteri bilgilerini giriniz:")
    musteriadi=input("Ad: ")
    musterisoyad=input("Soyad giriniz: ")
    musteritelefon=input("Telefon: ")
    musterimail=input("E-Posta: ")
    musteriadres=input("Adres:")
    print("Müşteri Bilgileri: ", musteriadi, musterisoyad, "mail mail adresi: " ,musterimail, "musteri telefonu: ",musteritelefon, "musteri adresi: " ,musteriadres)
    print("Sepetteki Ürünler: ", sepetim)
    print("Ödenecek Toplam Tutar: ",tutar)
    print("Ödeme Yöntemi Seçiniz: ")
    print("1 - Kapıda ödeme")
    print("2- Kredi Kartı")
    odeme_tercih = int(input("Ödeme Tercihi : "))
    if odeme_tercih!=1:
        print("*******")
        input("Kartı No : ")
        input("Son Kullanma Tarihi : ")
        input("CVV : ")
    print("Siparişiniz alınmıştır. Alışveriş yaptığınız için teşekkür ederiz.")
print("Alışveriş yapmak için lütfen yeniden çalıştırınız")
