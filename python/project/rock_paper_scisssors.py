import random
import matplotlib.pyplot as plt

print("Welcome to KC python games, this is rock/ paper/ scissors. Enjoy your time:)\n\n")
name = input("Please enter your name: ")
print(f"Hello {name}, let's play!\n")

computer_won = 0
user_won = 0
options = ["rock", "paper", "scissors"]

while(1):
    user_pick = input("Pick one from (rock, paper, scissors) :) or Q to quit: ").lower()
    if user_pick == "q":
        break
    elif user_pick not in options:
        continue
    else:
        computer = random.randrange(3)
        computer_pick = options[computer]
        if user_pick == "rock" and computer_pick == "scissors":
            user_won +=1
            print(f"Woooh, you won! the computer picked scissors\n")
        elif user_pick == "paper" and computer_pick == "rock":
            user_won +=1
            print(f"Woooh, you won! the computer picked rock\n")
        elif user_pick == "scissors" and computer_pick == "paper":
            user_won +=1
            print(f"Woooh, you won! the computer picked paper\n")
        else:
            computer_won +=1
            print(f"Sorry you lost. The computer picked {computer_pick}, try again your luck.\n")
            
print(f"\nYou have won {user_won} times.")
print(f"The computer has won {computer_won} times.")

if user_won > computer_won:
    print(f"You are the overall winner, congrats! :)\n")
elif user_won < computer_won:
    print(f"The computer is the overall winner, better luck next time! :(\n")
else:
    print(f"It's a draw, no overall winner! :|\n")

x = [1, 2, 3]
y = [user_won, computer_won, 0]
plt.bar(x, y, tick_label= [name, "Computer", "Draw"], width= 0.5, color= ['red', 'yellow', 'black'])
plt.xlabel("Players")
plt.ylabel("Number of wins")
plt.title("Rock/ Paper/ Scissors game results")
plt.show()
labels = [name, "Computer", "Draws"]
print(f"Good bye {name}! :)\n")

            
        
