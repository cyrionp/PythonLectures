import numpy as np

numbers1=np.random.randint(10,100,6)
numbers2=np.random.randint(10,100,6)

print(numbers1)
print(numbers2)

#result=numbers1+numbers2 # This will add the same indexes
#result=numbers1-numbers2 # This will substract the same indexes
#result=numbers1*numbers2 # This will multiply the same indexes
#result=numbers1/numbers2 # This will divide the same indexes
#result=numbers1+10

#result=np.sin(numbers1) #Take the sinus
#result=np.cos(numbers1) #Take the cosinus
#result=np.sqrt(numbers1) #Take the squared (karekök)
#result=np.log(numbers1) #Take the logarithms

mnumbers1=numbers1.reshape(2,3)
mnumbers2=numbers2.reshape(2,3)

#result=np.vstack((mnumbers1,mnumbers2)) #Do the matrices a single matrix (VERTICAL)
#result=np.hstack((mnumbers1,mnumbers2)) #Do the matrices a single matrix (HORIZONTAL)

#result=numbers1>=50 #Check if each items bigger than 50
result=numbers1%2==0 #Check if each items are even
print("NO") if False in result else print("YES") #Check if all items are even

print(numbers1[result]) #Check if which items are even

print(result)
