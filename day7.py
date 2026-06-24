# Functions
# pre defined functions:

# print() , input() , len()

# user defined functions:

# statements

# windsurf: , explain , generate docstring
def addition():
    a = 10
    b = 20
    print("Addition", a + b)

    # addition()
    # addition()
    # addition()
    # addition()
    # print(addition())
    # print(addition())
    # print(addition())
    # print(addition())

    # functions with parameter

    # windsurf: , explain , generate docstring

    def add(a,b):
        return a+b
    
    # print (add(10,20))
    # print (add(40,50))

    # functions with default parameters
    # print(add(10))

     # windsurf: , explain , generate docstring

def sum (a=0,b=0):
    print(a)
    print(b)
    return a+b

print (sum(10,20))
print (sum(20,50))
print (sum(10))
print (sum(a=100,b=200))

# inbuilt modules 

import math
print(math.pi)
print(math.sqrt(28))
print(math.pow(3,5))

import math as m

print(math.pi)
print(math.sqrt(28))
print(math.pow(3,5))

from math import pi, sqrt, pow
print(pi)
print(sqrt(34))

import random as r
print(r.randint(1,100))
print(r.random())

import  calendar as c
print (c.calendar(3001))


    


    


    


