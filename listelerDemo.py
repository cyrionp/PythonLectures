#1
sezen=['Bmw','Mercedes','Opel','Mazda']
print(sezen)

#2
print(len(sezen))

#3
print(sezen[0],'ve',sezen[-1])

#4
#sezenReplace=sezen
#sezenReplace[-1]='Toyota'
#print(sezenReplace)

#5
isEleman='Mercedes' in sezen
print("Mercedes, sezen'in elemanı mıdır?",isEleman)

#6
print(sezen[-2])

#7
#print(sezen[:3])

#8
#sezenReplace2=sezen
#sezenReplace2[-2:]=['Totoya','Renault']
#print(sezenReplace2)

#9
#sezenAdd=sezen
#sezenAdd+=['Audi','Nissan']
#print(sezenAdd)

#10
#sezenDel=sezen
#del sezenDel[-1]
#print(sezenDel)

#11
print(f"{sezen[::-1]}") #Tersten yazdırmak için

#12
studentA=['Yiğit','Bilgi',2010,[70,60,70]]
studentB=['Sena','Turan',1999,[80,80,70]]
studentC=['Ahmet','Turan',1998,[80,70,90]]
students=studentA+studentB+studentC
print(students)

#13
#Yiğit'in doğum yılı 2010'dur. Not ortalaması 66.6'dır.
print(f"{studentA[0]} {studentA[1]}'nin yaşı {2020-studentA[2]}'dur. Not ortalaması {(studentA[3][0]+studentA[3][1]+studentA[3][2])/3}'dır.")
