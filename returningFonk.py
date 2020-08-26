'''
def usalma(number):

    def inner(power):
        return number**power
    return inner

two=usalma(2)
three=usalma(3) #inner fonksiyonu
print(two(3))
print(three(4))


def yetkiSorgula(page):
    def inner(role):
        if role=="Admin":
            return f"{role} rolü {page} sayfasına ulaşabilir"
        else:
            return f"{role} rolü {page} sayfasına ulaşamaz"
    return inner

user1=yetkiSorgula("Product Edit")
print(user1("Admin"))
print(user1("User"))
'''

def islem(islem_adi):
    def toplam(*args):
        toplam=0
        for i in args:
            toplam+=i
        return toplam
    def carpma(*args):
        carpim=1
        for i in args:
            carpim*=i
        return carpim
    if islem_adi=="toplama":
        return toplam
    else:
        return carpma

toplama=islem("toplama")
print(toplama(1,3,5,6,7))

carpma=islem("carpma")
print(carpma(12,12))
