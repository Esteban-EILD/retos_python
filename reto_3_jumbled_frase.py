"""
Theory:
Split() method: string.split() splits a string into a list of substrings based on whitespace by default, or based on a specified separator.
Sorted() function: sorted(iterable) returns a new sorted list from the elements of the iterable.
sort() method: list.sort() sorts the elements of a list in place and returns None.(it does not create a new list)
Join() method: separator.join(list) concatenates the elements of the iterable (like a list or tuple) into a single string, with a separator between the characters of the string.
"""
# 1.- Problem decomposition: 3-letter word or less (it keeps the same); more than 3 letters(it sorts the intermediate letters in alphabetical order)
# Therefore we must use a conditional
# Create a function that takes a string as input and returns the jumbled version of the string according to the rules specified above.

def jbelmu(text):
    list_of_words = text.split()
    jumbled_version = []
    for word in list_of_words:
        jumbled_version.append(jumbled_word(word))
    return " ".join(jumbled_version)

def jumbled_word(word):
    if len(word) <= 3:
        return word
    else:
        first_letter = word[0]
        last_letter = word[-1]
        intermediate_letters = word[1:-1]
        sorted_intermediate_letters = sorted(intermediate_letters)
        jumbled_word = first_letter + ''.join(sorted_intermediate_letters) + last_letter   
    return jumbled_word

first_try = jbelmu("freecodecamp is my favorite place to learn to code")
print(first_try)