# # creating a function
# def hypotenus_calculator(side_a, side_b):
#     hypotenus = (side_a **2 + side_b **2) ** (1/2)
#     return(round(hypotenus, 3))

# print ('The hypotenus of the triangle is: ',hypotenus_calculator(6,6), 'cm')


# def distance(x1, x2, y1, y2):
#     d_a = pow(y1 - x1, 2)
#     d_b = pow(y2 - x2, 2)
#     dsquare = d_a + d_b
#     distance_a = dsquare**(1/2)
#     print(distance_a)
#     return distance

# distance(3,2,4,5)
# print("After thae function")


# def factorial(n):
#     space = ' ' * (4*n)
#     print(space, 'factorial', n)
#     if n == 0:
#         print(space, 'returning 1')
#         return 1
#     else:
#         recurse = factorial(n-1)
#         result = n* recurse
#         print(space, 'returning', result)
#         return result
# factorial(7)
    
   
   
   
   

   
    




# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# def print_fibonacci(n):


# def hypot(side_a, side_b):
#     side_c = round((pow(side_a, 2) + pow(side_b, 2))**(1/2), 3)
#     print(side_c)
#     return side_c
# hypot(3, 8)    

# lambda function             lambda argument: expression
# square = lambda x: x**2

# print(square(5))

# *name, helps you to create a function of unknown values of the paramenters.
# import math
# def add_numbers(*numbers):
#     result = math.sumprod(numbers)
#     return result

# add_numbers(3,5,6,8,7,2,3)

