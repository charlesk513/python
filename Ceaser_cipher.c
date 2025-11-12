alphabet = 'abcdefghijklmnopqrstuvwxyz'
user_input = input("word: ")
shift = int(input("Shift: ")
new = ' '
for ch in user_input:
    if ch.isalpha():
        index = alphabet.index(ch) + shift
        new_index = (index + shift) % 26
        new += alphabet[new_index]
    else:
        new += ch
print(new)
