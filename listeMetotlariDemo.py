names=['Ali','Yağmur','Hakan','Deniz']
years=[1998,2000,1998,1987]

#1
#names.append('Cenk')
#print(names)

#2
#names.insert(0,'Sena')
#print(names)

#3
#names.remove('Deniz')
#print(names)

#4
print(names.index('Deniz'))

#5
isFound= 'Ali' in names
print(isFound)

#6
#names.reverse()
#print(names)
#years.reverse()
#print(years)

#7
#names.sort()
#print(names)
#years.sort()
#print(years)

#8
#years.sort()
#years.reverse()
#print(years)

#9
str="Chevrolet,Dacia"
listStr=str.split(',')
print(listStr)

#10
kucuk=min(years)
buyuk=max(years)
print(f"Years dizisinin en büyük elemanı {buyuk}, en küçük elemanı ise {kucuk}")


#11
print(years.count(1998))

#12
years.clear()
print(years)

#13
marka=[]
for i in range(3):
    marka.append(input("Marka giriniz: "))
print('MARKALAR'.center(26,'*'))
for sezen in marka:
    print(sezen.center(26,'-'))
