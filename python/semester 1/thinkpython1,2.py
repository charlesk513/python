# pythagorus calculator
# side_a = int(input('The length of the triangle is: '))
# side_b = int(input('The width of the triangle is: '))
# side_c = (side_a **2 + side_b **2) ** (1/2)
# print('The hypotenuse of the trangle is:', side_c, 'cm')

# calculator app
# fast = 542
# fci = 621
# total = fast + fci
# print(total)

# slicing from a container
# todays_list = (23, 54, 21, 34, 43)
# print(todays_list)
# for x in todays_list:
#     print(x) 
#     if x == 21:
#         print('x is 21')
#     print(x, 'something')

# todays_list = (23, 54, 21, 34, 43)
# print(todays_list[::-1])
# print(todays_list[1:5:2])


# how many seconds are in 42 minutes and 42 seconds
# minutes = 42
# seconds = 42
# time = (minutes*60 + seconds)
# print(time)

# how many miles are there in 10 kilometers? 1.61km in a mile
# kilometers = 10
# print(round((kilometers/1.61), 2), 'miles')

# if you run a 10 km race in 42 minutes and 42 seconds, what is your average speed in miles per second
# kilometers = 10
# minutes = 42
# seconds = 42
# distance = (kilometers/1.61)
# time = (minutes*60 + seconds)
# average_speed = (distance/ time)/2
# print(average_speed)

# what is your average speed in minutes and seconds per mile?
# kilometers = 10
# minutes = 42
# seconds = 42 
# distance = (kilometers/1.61)
# time = (minutes*60 + seconds)
# ave_minutes = (minutes + seconds/60)
# print(ave_minutes/distance, 'min/mile')
# print(time/ distance, 'sec/mile')

# what is your average speed in miles per hour
# kilometers = 10
# minutes = 42
# seconds = 42 
# distance = (kilometers/1.61)
# time = (minutes/60 + seconds/3600)
# print(distance/time)

#concatenation of string
#  first_name = 'charles'
# sur_name = 'kabunga'
# print(sur_name + ' '+ first_name)  

#checking for the data type of the value
# x = 1 + 2 * 5
# print(type(x)) 

# The volume of a sphere with radius r is (4/3)*(22/7)**3. What is the volume of a sphere with radius 5?
# r = 5
# volume_of_the_sphere = (4/3)*(22/7)*(r**3)
# print(round(volume_of_the_sphere, 4))

# Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs
# $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for
# 60 copies?
# costPrice = 24.95   #in $
# discount = 0.4
# wholeSalePrice = (costPrice*(1 - discount))*60
# shippingCosts = (3 + (0.75*59))
# print('The total wholesale price of the books is: $', + (round(shippingCosts + wholeSalePrice, 4)))

# If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at
# tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?
timeForLeavingHome = (6*60 + 52)
distanceA = 1       #miles
timeA = (8*60 + 15)/60   #seconds/mile
distanceB = 3
timeB = (7*60 + 12)/60
distanceC = 1
timeC = (8*60 + 15)/60
timeTaken = ((timeA*distanceA)+(timeB*distanceB)+(timeC*distanceC))
print("The time takn to travel back home is ", round((timeTaken + timeForLeavingHome)/60, 3))

