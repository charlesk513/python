# code a parindram checker (a word that is the reverse of another word)

def is_parindram(word1, word2):
    result = ''.join(list(reversed(word1)))
    if word2 == result:
        print("Parindram")
    else:
        print("Not Parindram")
is_parindram('takes', 'sekat')



# code an anagram checker (a word that has the same letters as another word)

def is_anagram(word1, word2):
    if sorted(word1) == sorted(word2):
        print("Anagram")
    else:
        print("Not anagram")
is_anagram('fairy tales', 'rail safety')



# reverse the sentence

sentence = input("Enter a sentence to reverse: ")

def reverse_statement(sentence):
    sentence = sentence[0].lower() + sentence[1:]
    sentence = sentence.split()
    sentence = sentence[::-1]
    sentence = ' '.join(sentence)
    sentence = sentence[0].upper() + sentence[1:]
    print(f"Reversed statement: {sentence}")
reverse_statement(sentence)



# total length
my_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

total = list(map(len, my_list))
print(total)
print(f"The total letters are: {(sum(total))}")



def count_letters(my_list):
    total = 0
    number_list = []
    for i in my_list:
        number_list.append(len(i))
        total += len(i)
    print(number_list)
    print(f"The total letters are: {total}")
count_letters(my_list)
        
        
