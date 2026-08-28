"""
Anagram Checker
Problem Decomposition:
1.- Cleaning and normalizing the input strings: Remove spaces and convert to lowercase.
2.- Anagram comparison
"""

def are_anagrams(str1, str2):
    str1 = sorted(str1.lower().replace(" ",""))
    str2 = sorted(str2.lower().replace(" ",""))
    return str1 == str2

print(are_anagrams("listen", "silent")) 