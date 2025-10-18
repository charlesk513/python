import random
import emoji

print("\nWelcome to Group 6 Hangman game\n")
district_list = ["masaka", "kampala", "jinja", "mbarara", "gulu", "mbale", "hoima", "kalungu", "kabale", "lira"]

RandomDistrict = random.choice(district_list)  #random choosing of the district from the list

number = RandomDistrict.__len__() #counting the characters in the district name
result = '_, ' * number  #district name placeholder
result = result[:-2]  #removing the last comma and space using indexing method
print(f"This is the random district: [{result}]")

chances = number - 1 #iterative number of chances from the characters in the district name

while chances > 0:
    user_guess = input("Guess the letter in the district name: ").lower()
    if len(user_guess) != 1:
        print("Please enter only a single letter.")
        continue
    if not user_guess.isalpha():
        print("Please enter a valid letter from the alphabet.")
        continue
    
    index = [i for i, c in enumerate(RandomDistrict) if c == user_guess]   #list comprehension way to find the index of the letter in the district name 
    
    if not index:
        chances -= 1
        print(f"Sorry, that letter is not in the district name. Chances left: {chances}")
        if chances == 0:
            print(emoji.emojize(f"Game over! :skull: The district was: {RandomDistrict}"))
            break
        
        continue

    for i in index:
        result = result[:i*3] + user_guess + result[i*3+1:]    #substituting the result string underscores with the correctly guessed letter respectively

    print(f"[{result}]\n")

    if '_' not in result:
        print(emoji.emojize(f"Congratulations! You have guessed the district name :thumbs_up: :trophy:"))
        break
        
    