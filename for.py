numbers =[1,2,3,4,5]
for num in numbers:
    print('MERHABALAR')

names=['sezen','sude','kadir']
for name in names:
    print(f"My name is {name}")

'''
name=input("İsim giriniz: ")
yaz=''
for n in name:
    yaz+=f'{n} '
print(yaz)
'''

tuple=[(1,2),(1,3),(3,5),(5,7)]
for a,b in tuple:
    print(f"{a} sayısı ile {b} sayısı")

d={'k1':1,'k2':2,'k3':3}
for item,fiyat in d.items():
    print(f"{item} --> {fiyat} TL")
