# Everything in Python is an object as in Ruby
# Remember, Modules are simply .py files meant to be imported
# Modules contain class defitions, sometimes only containing one class
# A module is a file containing Python definitions and statements.
# When importing a module leave  off the extentsion, like Below
# All classes begin with upercase letters in Python as in Ruby
# A class is a factory which contains the blueprint for an instance
# An instance is a constructed object of its class type
# Type indicates the class the instance belongs to
# An attribute is an object value, data or state
# A method is a callable  attribut that perfoms some function

# Think of an object as a unit of data with associated functionality
# An object's interface is made up of its public methods
# Methods can be viewed as buttons that operate the object
# Methods can change the objects state or data
# Implemenatatio or processing of data is private methods and apart of interface


# Below is the way to import from other modules
import math
import datetime as dateLibrary
from decimal import Decimal

# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a+b

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result


print(Decimal('3.5') + Decimal('3.5'))

print; print

# A simple class example

class Myclass(object):
    pass # pass indicates that their is no contents

this_obj = Myclass()

print(this_obj)

print;print

# Below is a new class that contains instance methods
# Instance Methods are variables defined in the class
# In the example below the instance is self meaning the object itself
# Self is the instance upon which an object is called
# A method on an instance passes the instance as the 1st arguement to the method
# Instance have their own data or state called instance attributes
# Variables defined in a class are available to all instances

class Joe(object):
    def callme(self):
        print('calling callMe method with instance: ')

thisJoe = Joe()
thisJoe.callme()

print;print

import random

class Michael(object):
    def generateNum(self):
        self.rand_val = random.randint(1,10)

doThis = Michael()
doThis.generateNum()
print(doThis.rand_val)

# Below is a new class with getter and setter methods
# Remember any instance method is designed to work on the instance implicitly
# Setter values take an arguement and setting it as an attribute in the instance
# Getter methods allow me to retrieve an instances state or attributes
# Hence, why self is passed to the gettter and setter methods first

class MyClass2(object):
    def set_val(self, val):
        self.value = val

    def get_val(self):
        return self.value

a = MyClass2()
b = MyClass2()

# I can set an instances attribute in the body of the code
a.value = 'hello'

# However, setting gateways using instance methods insures the integrty of state, aka encapsulation
# By requiring encapsulation I create safe storage of data in an instance
# Data should only be accessed through instance methods
# Data should be validated by passing through instance methods
# These mechnanism protect dat from external processes


a.set_val(10)
b.set_val(100)


print(a.get_val())
print(b.get_val())

# Below I utilize the __init__ inorder to construct new instances
# __init__ is a method that is automatically called when a new instance is constructed
# The self arguement is the first appearance of the instance
# __init__ allows me to initialize attributes and prep work before and instance is created


class MyNum(object):
    def __init__(self, value):
        print('calling __init__')
        self.val = value

    def increment(self):
        self.val = self.val + 1

dd = MyNum(5)
dd.increment()
dd.increment()

print(dd.val)


##### Class attributes vs Instance attributes #####
# The attribute look up order is first in the instance then in the class
# An instance has access to its attributes as well as the class's

class YourClass(object):
    classy = 10 # class variables

    def set_val(self):
        self.insty = 100 # insty is a instance attributes

dd = YourClass()
dd.set_val()

print(dd.classy)
print(dd.insty)
print
