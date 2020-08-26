def greeting(name):
    print("Hello ",name)

'''
print(greeting("Ali"))

sayHello=greeting
print(sayHello)
print(greeting)

del sayHello
print(greeting)
#print(sayHello)


#Encapsulation
def outer(num1):
    def inner_increment(num1):
        return num1+1
    num2=inner_increment(num1)
    print(num1,num2)

outer(10)
'''

def factorial(number):
    if not isinstance(number,int):
        raise TypeError("Number must be an integer")

    if not number>=0:
        raise ValueError("Number must be zero or positive")

    def inner_factorial(number):
        if number<=1: return 1
        return number*inner_factorial(number-1)
    return inner_factorial(number)

try: print(factorial(-2))
except Exception as ex: print(ex)
