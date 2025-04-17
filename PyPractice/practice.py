""" DATA TYPES """

_String = "Hello World!"
_Integer =  1
_Float = 1.1523324
_Boolean = True # or False

""" COLLECTIVE DATA TYPES """

_List = [1, 2, 3, 4] # can be ordered, changeable and indexed - used in most cases
_Tuple = (1, 2, 3, 4) # can be ordered, unchangeable and indexed
_Set = {1, 2, 3, 4,} # unordered, unchangeable*, and unindexed
_Dictionary = {"Key1": "Value1", "Key2": "Value2"} # can be ordered, changeable and indexed - used in most cases, if you need a key-value pair

""" Variables """

# variablename = "data stored in it"
# other_variable = input("please enter your name")


""" functions """

def Adding(a, b):
    
    result = a + b

    return result

""" Loops """

for i in range(20):

    print(i)

print("\n-- for loop finished --\n")

x = 0

while x < 20:

    print(x)

    x = x + 1

print("\n-- while loop finished --\n")

""" Importing """

import os
import colorama

""" Classes """

class Car:

    def __init__(self, make = "", model = "", colour = "", rpm = 0, year = 0000, mileage = 000000):
        self._make = make
        self._model = model
        self._colour = colour
        self._rpm = rpm
        self._year = year
        self._mileage = mileage

    def GetMileage(self):
    
        return self._mileage
        
A = 7
B = 0
C = -3

vector = A + (3 * B) - C

print(vector)