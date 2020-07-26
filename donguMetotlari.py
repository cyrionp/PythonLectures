#range ***********
# for item in range(50,100,10) :
#     print(item)
#
# print(list(range(50,100,10)))

#enumerate ******
# salamlama='Selam'
# for index,harf in enumerate(salamlama):
#     print(f"{index} -> {harf}")

#zip ************
list1=[1,2,3,4,5]
list2=['a','b','c','d','e']
list3=[100,200,300,400,500]
print(list(zip(list1,list2,list3)))

for sira,urun,fiyat in zip(list1,list2,list3):
    print(f"{sira} -> {urun} --> {fiyat} TL")
