# # container setup
# a_list = (1,2,3,'name')
# a_tuple = [1,2,3,'name']
# a_set = {1,2,3,'name',2}
# a_dictionary = {'name':'charles', '100':'age'}



# # how to get values from a container
# my_list = ('alex','disan','charles','kevin')
# print(my_list[0])
# print(my_list[0:3])
# # print(my_list[start:end:step])
# print(my_list[0:3:2])


# set = (1,2,3,4,5,6,7,8,9)
# # print(set[7])
# # print(len(set))

# print(set[2:7])

#.append(adds)  .count(counts items specified)   .index(no of an item)    .clear(empties)   .sort(sorts the list)   .reverse(reverses the list)


# data ='From kcjesuschrist513@gmail.com sat Jan 5 09:14:16 2024'
# atpos = data.find('@')
# stpos = data.find(' ', atpos)
# # atpos = data[atpos+1:stpos]
# print(atpos)
# print(stpos)


# # # exercise
# exercise_list = (1,2,3,4,5,6,7,8,9,10)
# real = exercise_list[:4]
# rea = exercise_list[5:]
# print(real)
# print(rea)
# result = real + rea
# print(result)

# list comprehension
result = list(i for i in range(5))
print(result)
