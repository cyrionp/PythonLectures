'''
ogrenciler={'120':{
                'ad':'Ali',
                'soyad':'Yılmaz',
                'telefon':'532 000 00 01'
            },
            '125':{
                'ad':'Can',
                'soyad':'Korkmaz',
                'telefon':'532 000 00 02'
            },
            '128':{
                'ad':'Volkan',
                'soyad':'Yükselen',
                'telefon':'532 000 00 03'
            }
            }
'''
ogrenciler={}
for i in range(3):
    numero=input("Öğrenci Numarası Giriniz: ")
    ad=input("Öğrenci Adını Giriniz: ")
    soyad=input("Öğrenci Soyadını Giriniz: ")
    telefon=input("Öğrenci Telefon Numarasını Giriniz: ")
    ogrenciler.update({
        numero:{
            'Ad':ad,
            'Soyad':soyad,
            'Telefon':telefon
        }
    })
    print('----------')
req=input('Öğrenci Numarasıyla Bilgi Alın: ')
for bilgi in ogrenciler[req]:
    print(f"Öğrenci Adı {bilgi}")
