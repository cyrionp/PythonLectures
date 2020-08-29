def enKucukBulma(x):
    kucuk=x[0]
    for sayi in x:
        if int(sayi)<int(kucuk): kucuk=int(sayi)
    return int(kucuk)

girilenListe=[1,2,3,4,5,6,4,23,67,21,-500,23,451,67]
print(enKucukBulma(girilenListe))
