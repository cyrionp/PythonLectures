'''
def my_decorator(func):
    def wrapper(name):
        print("Fonksiyondan önceki işlemler")
        func(name)
        print("Fonksiyondan sonraki işlemler")
    return wrapper

def sayHello():
    print("hello")

def sayGreeting():
    print("greeting")

@my_decorator
def sayHello(name):
    print(f"hello {name}")

sayHello("Ali")
'''

import math
import time

def calculate_time(func):
    def inner(*args,**kwargs):
        start=time.time()
        time.sleep(1)
        func(*args,**kwargs)
        finish=time.time()
        print(f"Fonksiyon {func.__name__} {str(finish-start)} saniye sürdü")
    return inner

@calculate_time
def usalma(a,b):
    print(math.pow(a,b))

@calculate_time
def faktoriyel(num):
    print(math.factorial(num))

@calculate_time
def toplama(a,b):
    print(a+b)

@calculate_time
def cikarma(a,b):
    print(a-b)

@calculate_time
def carpma(a,b):
    print(a*b)

@calculate_time
def bolme(a,b):
    print(a/b)

usalma(2,3)
faktoriyel(4)
