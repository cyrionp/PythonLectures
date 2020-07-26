urunler={'Kitap':{'roman':{'huzursuzluk':20, 'tutunamayanlar':30, 'devir':30, 'serenad':25, 'aşk':25},
                      'şiir':{'sevda':17, 'gönül':22, 'hayat':20, 'ölüm':20, 'çiçek':10},
                      'çizgiroman':{'flash':35, 'wonderwoman':42, 'superman':35, 'spiderman':40, 'ricky':27},
                      'hikaye':{'monti':10, 'yaramaz':12, 'ayıcık':17, 'kartanesi':20, 'pati':18}},
             'Kulaklık':{'kulakiçi':{'x':100, 'y':150, 'z':250, 'w':125, 'a':110},
                         'kulaküstü':{'a1':100, 'a2':120, 'a3':130, 'a4':140, 'a5':150},
                         'bluetooth':{'b1':100, 'b2':110, 'b3':120, 'b4':130, 'b5':170},
                         'spor':{'jbl':200, 'sony':190, 'samsung':210, 'beats':400, 'jabra':100}},
             'OyuncakVeHobi':{'peluş':{'ayı':50, 'kedi':60, 'köpek':70, 'baykuş':80, 'pony':90},
                           'lego':{'l1':200, 'l2':210, 'l3':220, 'l4':250, 'l5':290},
                           'puzzle':{'puz1':130, 'puz2':140, 'puz3':150, 'puz4':170, 'puz5':160},
                           'bebekler':{'barbie':100, 'cindy':150, 'bratz':200, 'witch':250, 'pony':300},
                            'oyunlar':{'monopoly':100, 'tabu':150, 'jenga':200, 'uno':250, 'scrable':300}},
             'Müzik':{'yerlialbüm' :{'sıla':20, 'ceylanertem':20, 'cem':18, 'oğuzhan':16, 'sertap':22},
                      'yabancıalbüm' :{'bruno':20, 'rihanna':27, 'nicky':19, 'jlo':24, 'beyonce':30},
                      'rap' :{'patron':20, 'ati':25, 'ceza':27, 'ezhel':30, 'fero':20},
                      'karaoke' :{'karao1':10, 'karao2':11, 'karao3':12, 'karao4':13, 'karao5':14},
                      'rock' :{'şebnemferah':11, 'haykocepkin':13, 'cemkaraca':11, 'Queen':16, 'Evanescence':19}},
             'Film':{'korku' :{'dabbe1':20, 'testere':23, 'o':25, 'siccin':27, 'arınmagecesi':29},
                     'dram' :{'limonatalar':13, 'hokkabaz':13, 'esaretinbedeli':16, 'suveateş':14, 'cebimdekiyabancı':18},
                     'belgesel' :{'atombombası':23, 'naziler':25, '2dünyasavaşı':25, '13korkusu':16, 'yaratıcıbeyin':19},
                     'romantik' :{'romantikkomedi1':24, 'romatikkomedi2':21, 'herşeyaşktan':23, 'notebook':26, 'delibal':28}}}

Sepet=[]
kategoriler = ["Kitap","Kulaklik","OyuncakVeHobi","Müzik","Film"]
odenecekucretkdvli=0
odenecekucret=0
durum=True
print("Kültür ve Eğlence Dünyası S&S e hoşgeldiniz.")
alisveris=int(input("Alışveriş yapmak için 1 i, istemiyorsanız 0 giriniz: "))
if alisveris!=1:
    print('Hoşçakalın :(')
else:
    while durum==True:
        i = 1
        k=1
        l=1
        for kategori in urunler:
            print(str(i) + "-" + kategori)
            i=i+1
        kategori_sec = int(input("Lütfen Bir Kategori Seçiniz : "))-1  #inputu inte cevirdim
        kategori_sec = [*urunler][kategori_sec]
        alt_dict = urunler[kategori_sec]
        for katS in urunler[kategori_sec].keys():
            print(str(k)+"-"+katS)
            k=k+1
        a_kategori=int(input("Alt kategori seçiniz: "))-1
        a_kategori = [*alt_dict][a_kategori]
        enalt_dict = alt_dict[a_kategori]
        for akatS in urunler[kategori_sec][a_kategori].keys():
            print(str(l)+"-"+akatS)
            l=l+1
        secilen_urun=int(input("Ürün Seçiniz:"))-1
        sonurun = [*enalt_dict][secilen_urun]

        secilen_urun_ucret=urunler[kategori_sec][a_kategori][sonurun]
        Sepet.append(sonurun)
        odenecekucret=odenecekucret+secilen_urun_ucret
        devamdurumu = int(input("Alışverişe Devam Etmek İçin 1 i - Sepete Gitmek İçin 2 yi seçiniz :"))
        if devamdurumu != 1:
            break
m=1
print(" ")
print("SEPETİM")
print(" ")
if alisveris==1:
    for sepetcik in Sepet:
        print(str(m)+"-",sepetcik)
        m=m+1
    odenecekucretkdvli=odenecekucret*118/100
    odenecek_kdv=odenecekucret*18/100
    print(" ")
    print("Ödenecek KDV'siz tutar: ",odenecekucret)
    print("Ödeyeceğiniz KDV tutarı: ",odenecek_kdv)
    print("Ödenecek ücret toplamı: ",odenecekucretkdvli)
    print(" ")
    odemesecenekleri={'KrediKartı', 'KapıdaOdeme'}
    n=1
    print("Toplam Ücret : " + str(odenecekucretkdvli))
    print(" ")

    print("Bilgilerinizi Giriniz")
    input("Adres :")
    input("E-posta : ")
    print("ÖDEME SEÇENEKLERİ")
    print("1-Kredi Kartı")
    print("2-Kapıda ödeme")
    odeme_secenegi = int(input("Ödeme Seçeneği : "))
    if odeme_secenegi ==1:
        print(" ")
        input("Kredi Kartı Numarası : ")
        input("Kredi Kartı Sahibi : ")
        input("Kredi Kartı CVV : ")

bitir=input(print("Bizi tercih ettiğiniz için teşekkür ederiz"))
