# map functions in python help us change iterative items simply into any type of containers wanted

# # one iterative containers
# my_list = [1,2,3,4,5,6,7,8,9]

# def calc(n):
#     return n * n

# #the first parameter is the one for the map function then the second is for iterative ite container
# print(list(map(calc, my_list))) 
# print(set(map(calc, my_list)))
# print(tuple(map(calc, my_list)))

# # multiple iterative containers
# third = ['1','2','3']
# second = ['d', 'ue', 'ge']
# first = ['re', 'bl', 'oran']

# def concatenated(first, second, third):   #we can use maps to concatenate strings
#     return first + second + third

# #the first parameter is the one for the map function then the rest are for iterative ite container
# print(list(map(concatenated, first, second, third))) 


# # we can also use the map function to count the number of characters in the strings inside a container like below
# my_list = ['dear', 'tracy',' traver', 'james', 'samuelkatwa', 'shirat', 'charleskabunga']

# print(len(my_list[3]))  #instead of doing one by one as this line denotes
# word_length = list(map(len, my_list))

# print(word_length)


# # map function can also be done with lambda functions
# my_list = [1,2,3,4,5,6,7,8,9]

# result = list(map(lambda x: x * x, my_list))
# print(result)



