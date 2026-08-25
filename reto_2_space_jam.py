"""Theory:
1.- Replace method: string.replace("old", "new") replaces all occurrences of the substring "old" with the substring "new" in the string.
2.- Upper method: string.upper() converts all characters in the string to uppercase.
3.- Join method: separator.join(iterable) concatenates the elements of the iterable (like a list or tuple) into a single string, with a separator between the characters of the string
"""
def space_jam(s):
    without_spaces = s.replace(" ","")
    upper_case = without_spaces.upper()
    spaces_between_characters = "  ".join(upper_case)
    return spaces_between_characters

prueba = space_jam("Esteban")
print(prueba)