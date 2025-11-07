# import math
# import random
# import string

# print(random.randint(3, 7))
# print(math.factorial(3))
# print(math.log2(128))
# print(string.ascii_letters)


# you can import libraries with specific methods you want. 
#you can still can a method from the library and you dont import the whole library e.g
from math import sqrt
from string import ascii_uppercase

print(sqrt(9))  #then you can call the method as a variable
print(ascii_uppercase)


# iporting the whole module into a file may be tiresome but you can import classes, functions or variables specifically
# like they are created with in 