#1
'''
sayi=float(input('sayı: '))
result=(sayi>0) and (sayi<=100)
if result:
    print(f"{int(sayi)}, 0-100 arasındadır")
else:
    print(f"{int(sayi)}, 0-100 arasında değildir.")
'''

#2
'''
sayi=int(input('sayı: '))
ciftlik=sayi%2==0
pozitiflik=sayi>0
if ciftlik:
    if pozitiflik:
        print(f"{sayi}, çift ve pozitiftir.")
    else:
        print(f"{sayi}, çift ve negatiftir.")
else:
    if pozitiflik:
        print(f"{sayi}, tek ve pozitiftir.")
    else:
        print(f"{sayi}, tek ve negatiftir.")
'''

#4
a=int(input('a: '))
b=int(input('b: '))
c=int(input('c: '))
aBuyuk=a>b and a>c
bBuyuk=b>a and b>c
cBuyuk=c>a and c>b

kucukSayi=0
ortancaSayi=0
buyukSayi=0
if aBuyuk:
    buyukSayi='a'
    if b>c:
        ortancaSayi='b'
        kucukSayi='c'
    else:
        ortancaSayi='c'
        kucukSayi='b'
elif bBuyuk:
    buyukSayi='b'
    if a>c:
        ortancaSayi='a'
        kucukSayi='c'
    else:
        ortancaSayi='c'
        kucukSayi='a'
elif cBuyuk:
    buyukSayi='c'
    if a>b:
        ortancaSayi='a'
        kucukSayi='b'
    else:
        ortancaSayi='b'
        kucukSayi='c'
print(f"Sayıların sıralaması: {buyukSayi} > {ortancaSayi} > {kucukSayi}")
