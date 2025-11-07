from string import ascii_lowercase
import math


class FirstClass:
    def my_func(self):
        a = 'Today is a wednesday'
        letter = ascii_lowercase
        print(letter)
        print(a)
        
    def hypot(self, side_a, side_b):
        side_c = round(math.sqrt(pow(side_a, 2) + pow(side_b, 2)), 3)
        print(f"The hypotenuse of the triangle is {side_c} cm")
        return side_c