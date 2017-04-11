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
import fibo
import datetime as dateLibrary
from fibo import fib2
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
# A method on an instance passes the instance as the 1st arguement to the method
# Instance have their own data or state called instance attributes
# Variables defined in a class are available to all instances

class Joe(object):
    def callme(self):
        print('calling callMe method with instance: ')

thisJoe = Joe()
thisJoe.callme()

print;print
