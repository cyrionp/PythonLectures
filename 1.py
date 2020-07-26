a={"brand":"ford", "year":"1994", "model":"mustang"}
x=a["brand"]
print(x)
y=a.get("year")
print(y)
#a["model"]=fiesta#
b=1j
print(type(b))

tirnak='ali\'nin' #This is called "escape" and it can be used like this
print(tirnak)
escape="this contains \\ character"
print(escape)
tab="this\tstring"
print(tab)
altsatiragec= "this is a \nstring"
print(altsatiragec)
vstr="this\vstring"
print(vstr)
print(r"This \n string")
print("""This
string
contains
character""")

m=300
n=m #Hafızada gereksiz yer kaplayan şeyleri "Garbage Collector" yok sayar
m=400
print(m)
print(n)
k=300
l=k
print(id(k)) #variable id sini göstermek için kullandık
print(id(l)) #id lerin aynı olduğunu gördük
t=300
u=300
print(id(t))
print(id(u))

print=1
toplam=print+2
#print(toplam)

