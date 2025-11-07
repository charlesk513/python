# pythagoras theorem

# calculating the hypotenus
side_a = int(input('The adjuscent of the triangle is: '))
side_b = int(input('The opposite of the triangle is: '))
hypotenuse = (pow(side_a, 2) + pow(side_b, 2)) ** (1/2) 
print('The hypotenuse is:', round(hypotenuse,2), 'cm')

# calculating the adjuscent
side_c = (input('The hypotenus of the triangle is: '))
side_b = (input('The opposite of the triangle is: '))
adjuscent = (pow(side_c, 2) - pow(side_b, 2)) ** (1/2) 
print('The adjuscent is:', round(adjuscent,2), 'cm')

# calculating the opposite
side_c = int(input('The hypotenus of the triangle is: '))
side_b = int(input('The adjuscent of the triangle is: '))
opposite = (pow(side_c, 2) - pow(side_b, 2)) ** (1/2) 
print('The opposite is:', round(opposite,2), 'cm')

