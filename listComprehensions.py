numbers=[]
for x in range(10):
    numbers.append(x)
print(numbers)

numbers2=[x for x in range(10)]
print(numbers2)

for x in range(10):
    print(x**2)
numbers=[a**2 for a in range(10)]
print(numbers)

numbers=[x*x for x in range(10) if x%3==0 and x!=0]
print(numbers)

myString='Hello'
myList=[]

for harf in myString:
    myList.append(harf)
print(myList)

myList=[harf for harf in myString]
print(myList)

years=[1983,1999,2008,1956,1986]
ages=[2020-year for year in years]
print(ages)

results=[x if x%2==0 else 'TEK' for x in range(1,10)]
print(results)

result=[]
for x in range(3):
    for y in range(3):
        result.append((x,y))
print(result)

numbers=[(x,y,z) for x in range(3) for y in range(3) for z in range(3)]
print(numbers)
