class Calisan:
    zamOrani=1.8
    counter=0

    def __init__(self,isim,soyisim,maas):
        self.isim=isim
        self.soyisim=soyisim
        self.maas=maas
        self.email=isim+soyisim+"@asd.com"

        Calisan.counter+=1

    def giveNameSurname(self):
        return self.isim+" "+self.soyisim

    def zamYap(self):
        self.maas+=self.maas*self.zamOrani

calisan1=Calisan("Ali","Veli",100)
print(f"İlk maaş: {calisan1.maas}")
calisan1.zamYap()
print(f"Yeni maaş: {calisan1.maas}")

calisan2=Calisan("Ayşe","Hatice",200)
print(Calisan.counter)
