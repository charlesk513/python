import random

print("Welcome to KC python games\n\n")
print("----Number guessing game----\n")

while(1):
    real = random.randrange(101)
    print(" ")
    while(1):
        try:
            guess = int(input("Guess the number between 1 and 100: "))
        except ValueError:
            print("Invalid input, value not a number.")
            continue
        
        if guess >100 or guess < 1:
            print("Invalid number our of the possible results")
        elif guess > real:
            print("Too high")
        elif guess < real:
            print("Too low")
        elif guess == real:
            print("Wooh, you have picked it!, congs")
            break
        
        