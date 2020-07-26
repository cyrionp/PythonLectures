#inheritance (Kalıtım): Miras alma

#Person => name, lastname, age, eat(), run(), drink()
#Student(Person), Teacher(Person) (Bu sayede Person'a ait tüm özellikler Student ve Teacher için geçerli olacak ama değişiklikler, Person'a etki etmeyecek

#Animal => Dog(Animal), Cat(Animal)

class Person():
    def __init__(self,fname,lname):
        self.firstName=fname
        self.lastName=lname
        print("Person Created")

    def who_am_i(self):
        print("I'm a person")

    def eat(self):
        print("I'm eating")

class Student(Person):
    def __init__(self, fname,lname,number):
        Person.__init__(self,fname,lname) #Bu satırı yazarsak Person içindeki init metodu EZİLMEMİŞ olur
        self.studentNumber=number
        print("Student Created")

    #override
    def who_am_i(self):
        print("I'm a student")

    def sayHello(self):
        print("Hello! I'm a student")

class Teacher(Person):
    def __init__(self,fname,lname,branch):
        super().__init__(fname,lname)
        self.branch=branch

    def who_am_i(self):
        print(f"I'm a {self.branch} teacher")

p1=Person("Ali","Yılmaz")
s1=Student("Çınar","Turan",1256) #Person içindeki print çekilmiş oldu
t1=Teacher("Serkan","Yılmaz","Math")

print(p1.firstName+" "+p1.lastName)
print(s1.firstName+" "+s1.lastName+" "+str(s1.studentNumber))

p1.who_am_i()
s1.who_am_i()
t1.who_am_i()

p1.eat()
s1.eat()

#p1.sayHello() sayHello, Person'a ait olmadığı için çalışmaz
s1.sayHello()
