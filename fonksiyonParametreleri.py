'''
def changeName(n):
    n="Sude"

name="Sezen"
print(name)
changeName(name)
print(name)

def change(n):
    n[0]='adana'

sehirler=['ankara','izmir']
print(sehirler)
change(sehirler)
print(sehirler)

n=sehirler
n[0]='antep'
print(n)

def add(*params):
    sum=0
    for n in params:
        sum+=n
    return sum

print(add(10,20,30))
print(add(10,20))
print(add(10,20,50,89,416,479))
'''

def displayUser(**args): #dictionary gelecekse çift yıldız koyuyoruz
    for key,value in args.items():
        print('{} is {}'.format(key,value))

displayUser(name='Çınar',age=2,city='istanbul')
displayUser(name='Ada',age=12,city='kocaeli',phone='123213')
displayUser(name='Yiğit',age=14,city='ankara',phone='123213',email='yigit@gmail.com')

def myFunc(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

myFunc(10,20,30,40,50,key1='value1',key2='value2')
