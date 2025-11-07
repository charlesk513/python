 
# functions and methods

# functions
# print('a value') this function prints the value
# input('bring back the value') allows the user to type inside the data provided


# methods -> functions of datatypes
# print('value'.upper())
# print('VALUE'.lower())
# print('value'.replace('e','3'))

# for and a while loop
# exercise_list = [1,2,3,4,5]
# exercise_counter = 0
# for x in exercise_list:
#     if x == 2:
#         print('The value is 2')
#     else:
#         print('The value is not 2')
#     while exercise_counter <= 5:
#         print('Last item')
#         exercise_counter += 1


# pythagoras theorem
# side_a = int(input('The width of the triangle is: '))
# side_b = int(input('The length of the triangle is: '))
# hypotenuse = (pow(side_a, 2) + pow(side_b, 2)) ** (1/2) 
# print('The hypotenuse is:', hypotenuse, 'cm')
# print('The hypotenuse is:', round(hypotenuse,2), 'cm')

# simpler method to solve pytagorus theorem
# def pythagorus_calculator(side_a, side_b):
#     hypotenuse = (side_a**2 + side_b**2)**(1/2)
#     return hypotenuse

# print('The hypotenuse of the triangle is: ', round(pythagorus_calculator(6,6), 4), 'cm')


# single line if statements
# user_age = 10
# user_status = "adult" if user_age >= 18 else "Child"
# print(user_status)

# def shouter(function_string, repitition_amount):
#     counter = 0
#     while counter <= repitition_amount:
#         print(counter)
#     counter += 1
#     return(counter)
#     if 
# print (shouter("charles", 10))

# def shouter(exerciseString, repititionNumber):
#     print(exerciseString.upper())
#     counter = 0
#     while counter < repititionNumber:
#         print(counter, exerciseString)
#         counter += 1
#         if counter == repititionNumber:
#             print('You are too loud')

# shouter('charles', 10)

# f strings (they help to concatenate the strings to form one line)
# university_name = 'Mbarara (MUST)'
# start_year = 1987
# statement = f'the university called {university_name} has lived from {start_year}'
# print(statement)

# list comprehension (it helps to generate the list in python)
# list_comprehension = []
# for i in range (0,31,1):
#     list_comprehension.append(i)
# print(list_comprehension)

# list_comprehension = [i for i in range (0,11,1)] #this is the summary, i before customises the 'for'
# print(list_comprehension)




