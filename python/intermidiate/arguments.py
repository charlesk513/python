# the usage of args, we can create a tuple and we dont specify the number of parameters to hold

def addition(*args):
    sum = 0
    for i in args:
        sum += i
        print(i)
addition(1, 4, 6, 8, 10, 3, 5)


# the usage of kwargs, we can create a dictionary and we dont specify the number of parameters to hold

def addition(**kwargs):
    
        print(kwargs)
addition(name = 3, size = 49, desire = 'money', age= 25)


