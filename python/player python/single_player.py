# ACHIEVER'S CLOUD (group 6)
# NAME              	REG NUMBER
# Kabunga Charles	  2025/BCS/084/PS
# Ayebale Ronah	      2025/BCS/058/PS
# Ampwera Javan	      2025/BCS/079/PS
# Lugonvu Joel	      2025/BCS/112/PS
# Assumptah Praise	  2025/BCS/167/PS
# Kebirungi Patricia  2025/BCS/091/PS
# Aijuka David	      2025/BCS/016/PS
# Kanyesigye Joshua	  2025/BCS/195/PS
# Atuheire Edwin	  2025/BCS/212/PS
# Ainomugisha Ronald  2025/BCS/021/PS

import random


x = int(input("Enter initial value for herd A (non-negative integer): "))
y = int(input("Enter initial value for herd B (non-negative integer): "))
z = int(input("Enter initial value for herd C (non-negative integer): "))
def achievers_cloud(x, y, z):
    # Validate inputs
    for val in (x, y, z):
        if not isinstance(val, int) or val < 0:
            raise ValueError("All arguments must be non-negative integers.")

    piles = {"A": x, "B": y, "C": z}

    def display_piles():
        print("\nCurrent values:")
        for key, value in piles.items():
            print(f"{key}: {value}")

    def is_game_over():
        return all(value == 0 for value in piles.values())

    def user_choice():
        non_zero = [k for k, v in piles.items() if v > 0]
        while True:
            choice = input(f"Choose a herd {non_zero}: ").upper()
            if choice not in non_zero:
                print("Invalid choice or empty herd. Try again.")
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
        print(f"You removed {value} from {choice}.")
        display_piles()

    def computer_choice():
        non_zero = [k for k, v in piles.items() if v > 0]

        # Check for misère condition: only one pile > 1, force user to 1
        remaining_values = [v for v in piles.values() if v > 0]
        if remaining_values.count(1) == len(remaining_values) - 1:
            # Only one pile > 1, reduce it to 1
            for k in non_zero:
                if piles[k] > 1:
                    value = piles[k] - 1
                    piles[k] -= value
                    print(f"Computer removed {value} from {k}.")
                    display_piles()
                    return

        # Otherwise play normal Nim (optimal)
        nim_sum = 0
        for val in piles.values():
            nim_sum ^= val

        if nim_sum == 0:
            # No winning move, pick random
            choice = random.choice(non_zero)
            value = random.randint(1, piles[choice])
        else:
            # Make nim_sum = 0
            for k in non_zero:
                target = piles[k] ^ nim_sum
                if target < piles[k]:
                    value = piles[k] - target
                    choice = k
                    break

        piles[choice] -= value
        print(f"Computer removed {value} from {choice}.")
        display_piles()

    print("Welcome to Achievers Cloud! You play against the computer.")
    display_piles()

    while not is_game_over():
        # User turn
        if any(v > 0 for v in piles.values()):
            user_choice()

        if is_game_over():
            print("All variables are zero. You made the last move and lose!")
            break

        # Computer turn
        if any(v > 0 for v in piles.values()):
            computer_choice()

        if is_game_over():
            print("All variables are zero. You lose!")
            break

achievers_cloud(x, y, z)


