from random import randint


def randomCharacter(characters):
    n = len(characters)
    r = randint(0, n - 1)
    return characters[r]


def insertAtRandom(string, toInsert):
    n = len(string)
    r = randint(0, n)
    result = ''

    for i in range(r):
        result = result + string[i]
    result = result + toInsert

    for i in range(r, n):
        result = result + string[i]

    return result


def makePassword(length):
    password = ""
    for i in range(length - 2):
        password = password + randomCharacter("abcdefghijklmnopqrstuvwxyz")
    randomDigit = randomCharacter("0123456789")
    password = insertAtRandom(password, randomDigit)
    randomSymbol = randomCharacter("+-*/?!@#$%&")
    password = insertAtRandom(password, randomSymbol)
    return password


def main():
    result = makePassword(8)
    print(result)


main()
