""" Teoría y recuros utilizados en el reto 1 """
""" array se representa con una lista []"""
def fibonacci_sequence(start_sequence, length):
    if length <= 2:
        return start_sequence[:length]
    for i in range(length-2):
        start_sequence.append(start_sequence[-1] + start_sequence [-2])
    return start_sequence

fibonnaci_sequence = fibonacci_sequence([0, 1], 20)
print(fibonnaci_sequence)