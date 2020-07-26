satis = {
             'Telefon':{
                  'Tuşlu':
                      {'C1':100,'C2':200,'C3':450,'A10':350,'A20':600},
                  'Akılı':
                      {'iPhone 7':3000,'Samsung Galaxy S8':5500,'Huawei Mate X':32000,'iPhone 11':6500,'Xiaomi Mi 10':4900},
                  'telsiz':
                      {'Model 1':100,'Model 2':200,'Model 3':300,'Model 4':400,'Model 5':500}},
             'bilgisayar':{
                  'masaüstü':
                      {'Acer':4000,'Casper':6000,'Lenovo':9900,'HP':15000,'Apple':42000},
                  'dizüstü':
                      {'Apple MacBook Air':12000,'Acer Swift 3':5500,'Casper S500':4300,'Lenovo Legion 17':23000,'HP Omen 20':20000},
                  'tablet':
                      {'iPad Pro':15000,'Samsung Tab 5':3320,'iPad Air':1900,'Casper':400,'Huawei':3900}},
             'kulaklık':{
                  'bluetooth':
                      {'QCY':200,'Airpods Pro':2000,'Samsung Earbuds':850,'JBL':3000,'Sony':1400},
                  'kulaküstü':
                      {'QCY':100,'Philips':290,'Samsung':450,'JBL':1500,'Sony':900},
                  'kulakiçi':
                      {'QCY':90,'Beats':300,'AKG':250,'JBL':70,'Sony':200}},
             'aksesuarlar':{
                  'kılıf':
                      {'Model 1':20,'Model 2':30,'Model 3':40,'Model 4':70, 'Model 5':120},
                  'kırılmaz cam':
                      {'Model 1':20,'Model 2':30,'Model 3':40,'Model 4':70, 'Model 5':120},
                  'şarj aleti':
                      {'Model 1':20,'Model 2':30,'Model 3':40,'Model 4':70, 'Model 5':120}},
             'televizyon':{
                  'akıllı':
                      {'Acer':4000,'Philips':6000,'Samsung':9900,'LG':15000,'Sony':42000},
                  '4k':
                      {'Acer':2000,'Philips':3500,'Samsung':3000,'LG':2600,'Sony':4200},
                  'normal':
                      {'Acer':400,'ViewSonic':600,'Arçelik':900,'LG':1500,'Sony':2000}}}
kategori=[]
altKategori=[]
urun=[]
a=1
b=1
c=1
d=1
e=1
f=1
# initializing search key string
for key in satis.keys():
  kategori.append(key)
for kat in kategori:
    print(str(a)+"->",kat)
    a+=1
secilenKategori=input("Kategori seçiniz: ")
indexSecilenKategori=int(secilenKategori)-1
print(str(indexSecilenKategori))
for key2 in satis['indexSecilenKategori'].keys():
    altKategori.append(key2)
for kat2 in altKategori:
    print(str(b)+"->",kat2)
    b+=1
