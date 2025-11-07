exercise_list = [1,2,3,4,5]
exercise_counter = 0
for x in exercise_list:
    if x == 2:
        print('The value is 2')
    else:
        print('The value is not 2')
    while exercise_counter <= 5:
        print('Last item')
        exercise_counter += 1
