# lambda     we use lambda functon when we want to reeturn a variable but we dont want to use the return function
# double_value = lambda num: num * 2
# print(double_value(10))

# we used the lambda funcion to sort this list 
# random_list = [('Derrick', 54), ('Bridget', 46), ('lynn', 79), ('Mercy', 21)]
# sorted_list = sorted(random_list, key = lambda user_tuple: user_tuple[1])
# print(sorted_list)

# list comprehension
# battleship_board = [f'{j}{i}' for i in range(1,6) for j in ('A', 'B', 'C', 'D', 'E') if f'{j}{i}' != 'C3']
# print(battleship_board)