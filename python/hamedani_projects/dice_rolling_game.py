import random
print("\n\n\nWelcome to KC python games.\n")
print("\n----Dice rolling game---")
number = int(input("How many die do you want to engage with? "))

while(1):
    permission = input("Roll the dice? (y/n): ").lower()
    die = []
    for x in range(number):
        dice = random.randrange(7)
        die.append(dice)
        
    if permission == 'y':
        print(f"{die}")
    elif permission == 'n':
        print("Quited the game, goodbye!")
        break
    else:
        print("Invalid input entered")
        