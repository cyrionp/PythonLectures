#def square(num): return num**2
square=lambda num:num**2
numbers=[1,3,5,9]

print(list(map(square,numbers)))
print(square(3))

#for item in map(square,numbers):
#    print(item)

def checkEven(num): return num%2==0
print(list(filter(lambda num: num%2==0,numbers)))
