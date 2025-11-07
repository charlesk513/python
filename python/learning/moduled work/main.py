# import support


# first_class = support.FirstClass()

# first_class.my_func()
# first_class.hypot(3, 8)



# importing the whole module into a file may be tiresome but you can import classes, functions or variables specifically
# like they are created with in this document

from support import FirstClass

FirstClass.my_func('self')
firstClass = FirstClass()
firstClass.hypot(5, 6)


# # we can still import everything from a module and we dont need to repeat writing the module in our main file
# from support import *