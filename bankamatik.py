#Bankamatik Uygulaması

SadikHesap={
    'ad':'Sadık Turan',
    'hesapNo':'859595',
    'bakiye':3000,
    'ekHesap':2000
}
AliHesap={
    'ad':'Ali Turan',
    'hesapNo':'999595',
    'bakiye':2000,
    'ekHesap':1000
}

def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")

    if hesap['bakiye']>=miktar:
        print("Paranızı alabilirsiniz.")
    else:
        toplam=hesap["bakiye"]+hesap["ekHesap"]
        if toplam>=miktar:
            ekHesapKullanimi=input("Ek hesap kullanılsın mı? (e/h): ")
            if ekHesapKullanimi=="e":
                print("Paranızı alabilirsiniz")
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır.")
        else:
            print("Bakiye yetersiz")

print("1)Sadık 2)Ali")
kisi=int(input("Seçiminiz: "))
hesap=""
if kisi==1:
    hesap="SadikHesap"
elif kisi==2:
    hesap="AliHesap"
else:
    print("Yanlış seçim yaptınız")
miktar=int(input("Çekmek istediğiniz miktar: "))
paraCek(hesap,miktar)
