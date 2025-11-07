x = int(input("Enter initial value for herd A (non-negative integer): "))
y = int(input("Enter initial value for herd B (non-negative integer): "))
z = int(input("Enter initial value for herd C (non-negative integer): "))

def achievers_cloud(x, y, z):
    # Validate input values
    for val in (x, y, z):
        if not isinstance(val, int) or val < 0:
            raise ValueError("All arguments must be non-negative integers.")
    
    piles = {"A": x, "B": y, "C": z}
    players = ["Player 1", "Player 2"]
    turn = 0  # 0 for Player 1, 1 for Player 2

    def display_piles():
        print("\nCurrent values:")
        for k, v in piles.items():
            print(f"{k}: {v}")

    def is_game_over():
        return all(v == 0 for v in piles.values())

    def player_turn(player):
        non_zero = [k for k, v in piles.items() if v > 0]
        print(f"\n{player}'s turn.")
        while True:
            choice = input(f"Choose a variable from {non_zero}: ").upper()
            if choice not in non_zero:
                print("Invalid choice or variable has 0. Try again.")
            else:
                break

        while True:
            try:
                value = int(input(f"Enter value to remove from {choice} (1-{piles[choice]}): "))
                if 1 <= value <= piles[choice]:
                    break
                else:
                    print(f"Value must be between 1 and {piles[choice]}")
            except ValueError:
                print("Enter a valid integer.")
        
        piles[choice] -= value
        print(f"{player} removed {value} from {choice}.")
        display_piles()

    print("Welcome to Achievers Cloud!")
    print("Two-player mode: The player who makes all variables reach 0 loses!")
    display_piles()

    while True:
        current_player = players[turn % 2]
        player_turn(current_player)

        if is_game_over():
            print(f"\nAll variables are zero! {current_player} made the last move and loses.")
            print(f"The winner is {players[(turn + 1) % 2]}!")
            break
        
        turn += 1


# Example run
achievers_cloud(x, y, z)
