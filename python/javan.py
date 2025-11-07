# Ekitangabikozi - Bachwezi Cattle Picking Game
# Two players take turns picking cattle from three herds

def display_herds(herds):
    print("\nCurrent herds of cattle:")
    for i, cows in enumerate(herds, start=1):
        print(f"Herd {i}: {cows} cattle")

def is_game_over(herds):
    return sum(herds) == 0

def ekitangabikozi_game():
    print("🐄 Welcome to EKITANGABIKOZI - The Bachwezi Cattle Game 🐄")
    print("There are 3 herds of cattle. Each player takes turns picking from one herd.")
    print("You can pick one or more cattle, but only from one herd at a time.")
    print("Whoever picks the last cattle WINS!\n")

    # Initial number of cattle in each herd
    herds = [5, 7, 9]

    players = ["Player 1", "Player 2"]
    turn = 0  # 0 = Player 1, 1 = Player 2

    while not is_game_over(herds):
        display_herds(herds)
        current_player = players[turn]

        # Get valid herd choice
        while True:
            try:
                choice = int(input(f"\n{current_player}, choose a herd (1-3): "))
                if 1 <= choice <= 3 and herds[choice - 1] > 0:
                    break
                else:
                    print("Invalid choice! Pick a herd that still has cattle.")
            except ValueError:
                print("Please enter a number between 1 and 3.")

        # Get number of cattle to pick
        while True:
            try:
                pick = int(input(f"How many cattle will you pick from herd {choice}? "))
                if 1 <= pick <= herds[choice - 1]:
                    break
                else:
                    print("You can only pick from available cattle.")
            except ValueError:
                print("Enter a valid number.")

        # Update herd
        herds[choice - 1] -= pick
        print(f"{current_player} picked {pick} cattle from herd {choice}.")

        # Check if game is over
        if is_game_over(herds):
            print(f"\n🎉 {current_player} wins the game! 🎉")
            break

        # Switch turns
        turn = 1 - turn

    print("\nGame over. Thanks for playing Ekitangabikozi!")

# Run the game
ekitangabikozi_game()