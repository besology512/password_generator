import random
from sre_parse import SPECIAL_CHARS
import passwordlist as P
import string
import user_input as u


def check_pass():  # complete it and check if the P.password meets the conditions
    print('check_pass is working')
    if u.upper == True:
        for i in range(len(P.password)-1):
            if any((n.isupper()) for n in P.password): # create it with one line
                break
            else:
                for j in range(random.randrange(1, 3)):
                    P.password[random.randrange(0, len(
                        P.password)-1)] = [char for char in string.ascii_uppercase][random.randrange(0, 25)]

    if u.lower == True:
        for i in range(len(P.password)-1):
            if any((n.islower()) for n in P.password):
                break
            else:
                for j in range(random.randrange(1, 3)):
                    P.password[random.randrange(0, len(
                        P.password)-1)] = [char for char in string.ascii_lowercase][random.randrange(0, 25)]
    if u.Numbers == True:
        for i in range(len(P.password)-1):
            if any((n.isdigit()) for n in P.password):
                break
            else:
                for j in range(random.randrange(1, 3)):
                    P.password[random.randrange(0, len(
                        P.password)-1)] = [digit for digit in string.digits][random.randrange(0, 9)]
    if u.wspace == True:
        for i in range(len(P.password)-1):
            if any((n == ' ') for n in P.password):
                break
            else:
                for j in range(random.randrange(1, 3)):
                    P.password[random.randrange(0, len(P.password)-1)] = ' '
    if u.symbols == True:
        for i in range(len(P.password)-1):
            if any((n in SPECIAL_CHARS) for n in P.password):
                break
            else:
                for j in range(random.randrange(1, 3)):
                    P.password[random.randrange(0, len(
                        P.password)-1)] = [s for s in string.printable][62:94][random.randrange(0, 32)]


numbersL = [digit for digit in string.digits]
upperCasesL = [char for char in string.ascii_uppercase]
lowerCasesL = [char for char in string.ascii_lowercase]
allSymbolsL = [digit for digit in string.printable][62:94]
AmbSymbolsL = [digit for digit in string.printable][84:94]


def password_rating(password):  # can be seperated to more than one function
    global score
    global noNumbers  # we will use them for the suggestions
    global noUpper
    global noLower
    global noSymbols
    global passStrength

    score = 0

    # depending on length,symbols, upper and lower cases and correct words
    if len(P.password) < 8:
        score += 10
    elif 20 > len(P.password) > 8:
        score += 50  # full score
    else:
        score += 30

    for i in numbersL:
        if i in P.password:
            score += 12.5
            noNumbers = False
            break
        else:
            noNumbers = True

    for i in lowerCasesL:
        if i in P.password:
            score += 12.5
            noLower = False
            break
        else:
            noLower = True

    for i in upperCasesL:
        if i in P.password:
            score += 12.5
            noUpper = False
            break
        else:
            noUpper = True

    for i in allSymbolsL:
        if i in P.password:
            score += 12.5
            noSymbols = False
            break
        else:
            noSymbols = True

    if score > 80:
        passStrength = "Strong"
    elif score > 60:
        passStrength = "Decent"

    elif score > 40:
        passStrength = "Weak"

