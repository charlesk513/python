import random
import emoji

print("Welcome to KC python games\n\n")



def conditions(user_guess, comp_guess, fail):
    if user_guess == 'r' and comp_guess == 'p':
        print(emoji.emojize("You picked :rock: and computer picked :books:"))
    elif user_guess == 'r' and comp_guess == 's':
        print(emoji.emojize("You picked  :rock: and computer picked :scissors:"))
    elif user_guess == 'p' and comp_guess == 's':
        print(emoji.emojize("You picked :paper: and computer picked :scissors:"))
    elif user_guess == comp_guess:
        print(emoji.emojize("Tie! :handshake:"))
    elif fail == 1:
        pass
    else:
        print(emoji.emojize("You lost to the computer!"))
        
        
def play_game():
    fail = 0
    my_tuple = ('r', 'p', 's')
    comp_guess = random.choice(my_tuple)
    user_guess = input("1. Rock, 2.paper, 3.scissors? (r/p/s): ")
    if not user_guess.isalpha():
        print("Please enter a valid letter from the alphabet.")
        fail = 1    
    if user_guess not in my_tuple:
        print("Invalid input!")
        fail = 1
    conditions(user_guess, comp_guess, fail) 
    return comp_guess, user_guess, fail
    
    
    


while(1):
    play_game()
    
        

        
    


