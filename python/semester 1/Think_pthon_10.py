# | Method	 |   Description                                                                           |
# |------------|-----------------------------------------------------------------------------------------|
# | .values()	 |   Checks from within values in the dictionaries only                                    |
# | .keys	     |   Checks from within keys in the dictionaries only                                      |
# | copy()	 |   Returns a copy of the list                                                            |
# | count()	 |   Returns the number of elements with the specified value                               |
# | extend()	 |   Add the elements of a list (or any iterable), to the end of the current list          |
# | index()	 |   Returns the index of the first element with the specified value                       |


#  write a program to print the number of times a letter repeats in a word or statement
# word = input("Enter a word: ").lower()
# def count_letters(word):
#     letter_count = dict()
#     for letter in word:
#         if letter in letter_count:
#             letter_count[letter] += 1
#         else:
#             letter_count[letter] = 1
#     print(letter_count)
#     return letter_count
# result = count_letters(word)

letter_count = {'a': 1, 'b': 2, 'c': 3}
for x in letter_count:
    value = letter_count[x]
    print(f"{x} : {value}")
    