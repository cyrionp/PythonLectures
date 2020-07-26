#class
class Person:
    pass
    #class attributes
    address="no information"

    #constructor (yapıcı metod)
    def __init__(self,name,year):
        #object attributes
        self.name=name
        self.year=year

    #instance methods
    def intro(self):
        print("Hello There. I am "+self.name)

    def calculateAge(self):
        return 2020-self.year

#object (instance)
p1=Person("kadir",1998)
p2=Person("ali",2005)

#updating
p1.name="Ahmet"
p2.address="kocaeli"

'''
p1.intro()
p2.intro()
print(f"Adım: {p1.name} yaşım: {p1.calculateAge()}")
print(f"Adım: {p2.name} yaşım: {p2.calculateAge()}")
'''

class Circle:
    #class object attribute
    pi=3.14

    def __init__(self,yaricap=1):
        self.yaricap=yaricap

    #methods
    def cevre_hesapla(self):
        return 2*self.pi*self.yaricap

    def alan_hesapla(self):
        return self.pi*(self.yaricap**2)

c1=Circle() #yaricap default olarak 1 ayarlanmıştı
c2=Circle(5)

print(f"c1:\n Alan= {c1.alan_hesapla()} \nÇevre= {c1.cevre_hesapla()}")
print(f"c2:\n Alan= {c2.alan_hesapla()} \nÇevre= {c2.cevre_hesapla()}")
