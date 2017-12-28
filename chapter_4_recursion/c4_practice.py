def listsum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listsum(numList[1:])


def toStr(number, base):
    numString = "0123456789ABCDEF"
    if number < base:
        return numString[number]
    else:
        return toStr(number // base, base) + numString[number % base]


def reverse(aString):
    if len(aString) == 1:
        return aString[0]
    else:
        return reverse(aString[1:]) + aString[0]


def prepString(aString):
    acceptedchars = "abcdefghijklmnopqrstuvwxyz"
    stringEdit = list(aString.lower())

    result = ''

    for char in stringEdit:
        if char in acceptedchars:
            result += char

    return result


def isPalindrome(aString):
    testString = prepString(aString)

    if len(testString) < 2:
        return True

    if testString[0] != testString[-1]:
        return False

    return isPalindrome(testString[1:-1])



