import random
def rastgeleSayi():
    puan=0
    for i in range(5):
        print("-------------------------------------------------------------------")
        kalanHak=int(input("Kaç hak olsun?: "))-1
        while True:
            uretilenSayi=random.randint(1, 10)
            print("-------------------------------------------------------------------")
            tahmin=int(input("Tahmininiz: "))
            print("-------------------------------------------------------------------")
            if kalanHak==0:
                print(f"Hakkınız doldu, sayı {uretilenSayi} idi.")
                print("-------------------------------------------------------------------")
                break
            else:
                if tahmin!=uretilenSayi:
                    kalanHak-=1
                    print(f"Yanlış tahmin. Kalan hak: {kalanHak+1}")
                    if tahmin<uretilenSayi:
                        print("Arttırın :)")
                    elif tahmin>uretilenSayi:
                        print("Azaltın :)")
                else:
                    print("Tahmin doğru, Tebrikler!")
                    print("-------------------------------------------------------------------")
                    puan+=20
                    break
    print(f"Puanınız: {puan}")

rastgeleSayi()
