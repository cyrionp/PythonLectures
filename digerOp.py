# Identity Operator: is
x=y=[1,2,3]
z=[1,2,3]

print(x==y) #İçindeki değerleri kontrol
print(x==z)
print(x is y) #X aslında Y mi kontrol (referans olarak) TRUE
print(x is z) #x ve y'nin değerleri aynı ama eşitlenmedi FALSE

a=[1,2,3]
b=[2,4]
del a[2]
b[1]=1
b.reverse()
print(a==b)
print(a is b)
print(a is not b)

#Membership Operator: in
k=['apple','banana']
print('banana' in k)

def arat():
    n1=name.upper()
    n2=name.lower()
    if istenen in n1 or istenen in n2:
        print("İçindeee")
    else:
        print("MAfeles")

name=input("Kelime giriniz: ")
istenen=input("İstenen harfi giriniz: ")
arat()

