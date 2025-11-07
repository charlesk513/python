import random
import matplotlib.pyplot as plt

print("Welcome to KC python games, enjoy your time please\n\n")
numberOfTimesGuessed = 0

top_value = int(input("Enter the limit value: "))

if top_value < 0:
    print("Enter another number please, negatives are not allowed")
    exit(0)
elif top_value == 0:
    print("Entered value is a zero, enter a positive value next time")
else:
    while(1):
        guess_work = int(input("Guess the number: "))
        randomValue = random.randrange(top_value)
        if randomValue == guess_work:
            print(f"Woooh, you have guessed the number after {numberOfTimesGuessed} chances, you are lucky")
            break
        elif randomValue < guess_work:
            print("The number is greater than your guess, try again again your luck! :)")
        elif randomValue <= guess_work <= 0:
            print("The number is greater than your guess, try again again your luck! :)")
        else:
            print("The number is lower than your guess, try again again your luck! :)")
        numberOfTimesGuessed +=1
        

