import numpy as np

#numbers=np.array([0,5,10,15,20,25,50,75])

#result=numbers[5]
#result=numbers[-1] #Last number
#result=numbers[:3] #First 3 numbers. Equals to numbers[0:3]
#result=numbers[3:] #Print the array except first 3 numbers
#result=numbers[::] #Print the exact array
#result=numbers[::-1] #Print the REVERSED array
#result=numbers[::-2] #Two's steps

numbers2=np.array([[0,5,10],[15,20,25],[50,75,85]])
#result=numbers2[0] #Select 0th indexed line
#result=numbers2[2] #Select 2nd indexed line
#result=numbers2[0,2] #Select 0th line's 2nd item
#result=numbers2[2,1] #Select 2nd line's 1st item
#result=numbers2[:,2] #Select each lines 2nd items. We use cama(,) to select each lines
#result=numbers2[:,0:2] #Select each lines first 2 items
#result=numbers2[-1,:] #Select last line's all items
#result=numbers2[:2,:2]
#print(result)

arr1=np.arange(0,10)
#arr2=arr1 #Copying with reference (address)
arr2=arr1.copy() #Copying WITHOUT reference
arr2[0]=20 #This will change both of arrays on copying with reference

print(arr1)
print(arr2)
