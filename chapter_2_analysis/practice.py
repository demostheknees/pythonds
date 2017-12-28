# Import modules here
import timeit

# Declare functions here

def min_squared(data):
    result = data[0]
    for x in data:
        for y in data:
            if x < y and x < result:
                result = x
    return result


def min_linear(data):
    result = data[0]
    for x in data:
        if x < result:
            result = x
    return result


def isanagram(phrase1, phrase2):
    alist1 = list(phrase1)
    alist2 = list(phrase2)

    alist1.sort()
    alist2.sort()

    if alist1 == alist2:
        return True



# Set variables here

numbers = [6, 9, 18, 13, 45, 91, 15]

min1 = min_squared(numbers)
min2 = min_linear(numbers)



