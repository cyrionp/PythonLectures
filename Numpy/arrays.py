import numpy as np

#result=np.array([1,3,5,7,9])
#result=np.arange(1,10)
#result=np.arange(10,100,3) #Between 10 and 100 (include 10, except 100) increase by 3
#result=np.zeros(10) #float values
#result=np.ones(10) #float values
#result=np.linspace(0,100,5) #Divide numbers between 0 and 100 by equal parts
#result=np.linspace(0,5,5)
#result=np.random.randint(0,10) #Generate a random number between 0 and 10 (include 0, except 10)
#result=np.random.randint(20) #From 0 to 19
#result=np.random.randint(1,10,3) #Generate numbers between 1-9 and select 3 of them
#result=np.random.rand(5) #Generate numbers between 0-1 and select 5 of them
#result=np.random.randn(5) #Allow negative numbers to be selected

#np_array=np.arange(50)
#np_multi=np_array.reshape(5,10)
#print(np_multi.sum(axis=1))

rnd_numbers=np.random.randint(1,100,10)
print(rnd_numbers)
#result=rnd_numbers.max()
#result=rnd_numbers.min()
#result=rnd_numbers.mean() #Average number
#result=rnd_numbers.argmax() #Max number's index
result=rnd_numbers.argmin() #Min number's index

print(result)
