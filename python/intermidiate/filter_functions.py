# filter functions
# using an ordinary looping code
my_list = [1,2,3,4,5,6,7,8,9,10]
bigger_than = []
for x in my_list:
    if x > 6:
        bigger_than.append(x)
print(bigger_than)

# using a filter function
def check_greater_6(num):
    if num > 6:
        return True
    return False
result = list(filter(check_greater_6, my_list))
print(result)

# using a filter function alongside a lambda function
result = list(filter(lambda n: n > 6, my_list))
print(result)


# FILTER functIons also help also filter falsy values from truthy ones
the_list = ['True', 0 , '0', 'False', 'Hello', 1, '1']
result = list(filter(None, the_list))
print(result)   # it removes the falsy ones e.g 'False' and 0


# REDUCE
# 
