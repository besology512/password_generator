import random
from sre_parse import SPECIAL_CHARS
import passwordlist as P
import string
import user_input as u
import enchant


def check_pass():  # complete it and check if the P.password meets the conditions
    print('check_pass is working')
    if u.upper == True:
        print("upper space runed")
        for i in range(len(P.password)-1):
            if any((n.isupper()) for n in P.password): # create it with one line
                break
            else:
                for j in range(random.randrange(1, 3)):
                    P.password[random.randrange(0, len(
                        P.password)-1)] = [char for char in string.ascii_uppercase][random.randrange(0, 25)]

    if u.lower == True:
        print("lower space runed")
        for i in range(len(P.password)-1):
            if any((n.islower()) for n in P.password):
                break
            else:
                for j in range(random.randrange(1, 3)):
                    P.password[random.randrange(0, len(
                        P.password)-1)] = [char for char in string.ascii_lowercase][random.randrange(0, 25)]
    if u.Numbers == True:
        print("numbers space runed")
        for i in range(len(P.password)-1):
            if any((n.isdigit()) for n in P.password):
                break
            else:
                for j in range(random.randrange(1, 3)):
                    P.password[random.randrange(0, len(
                        P.password)-1)] = [digit for digit in string.digits][random.randrange(0, 9)]
    if u.wspace == True:
        print("white space runed")
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

    score = 0
    # depending on length,symbols, upper and lower cases and correct words
    if len(password) < 8:
        score += 10
    elif 20 > len(password) > 8:
        score += 50  # full score
    else:
        score += 30

    for i in numbersL:
        if i in password:
            score += 12.5
            noNumbers = False
            break
        else:
            noNumbers = True

    for i in lowerCasesL:
        if i in password:
            score += 12.5
            noLower = False
            break
        else:
            noLower = True

    for i in upperCasesL:
        if i in password:
            score += 12.5
            noUpper = False
            break
        else:
            noUpper = True

    for i in allSymbolsL:
        if i in password:
            score += 12.5
            noSymbols = False
            break
        else:
            noSymbols = True

    if score > 80:
        passStrength = "Strong"
    elif score > 60:
        passStrength = "Decent"

    else:
        passStrength = "Weak"

    return score,passStrength


def password_rating(password):  # can be seperated to more than one function

    score = 0
    # depending on length,symbols, upper and lower cases and correct words
    if len(password) < 8:
        score += 10
    elif 20 >= len(password) >= 8:
        score += 50  # full score
    else:
        score += 30

    for i in numbersL:
        if i in password:
            score += 12.5
            noNumbers = False
            break
        else:
            noNumbers = True

    for i in lowerCasesL:
        if i in password:
            score += 12.5
            noLower = False
            break
        else:
            noLower = True

    for i in upperCasesL:
        if i in password:
            score += 12.5
            noUpper = False
            break
        else:
            noUpper = True

    for i in allSymbolsL:
        if i in password:
            score += 12.5
            noSymbols = False
            break
        else:
            noSymbols = True

    if score > 80:
        passStrength = "Strong"
    elif score > 60:
        passStrength = "Decent"

    else:
        passStrength = "Weak"

    return score,passStrength


def check_dictionary(password):
    password = password.lower()
    d = enchant.Dict('en_GB')
    found = [] 
    words = []
    for i in range(len(password)):
        for j in range(i+1, len(password) + 1):
                check = d.check(password[i:j])
                if check == True and j-i > 3:
                    if i == len(password)-1:
                        found.append([i,j+1])
                    else:
                        found.append([i, j])

    for i in range(len(found)):
        first = found[i][0]
        last = found[i][1]
        words.append(password[first:last])


    words = list(set(words))
    word1 = []
    word2 = []
    c = 0
    for word in words:
        c = 0
        for symb in allSymbolsL:
            if word.find(symb) != -1:
                c += 1
        if c == 0:
            word1.append(word)

    for word in word1:
        c = 0
        for num in numbersL:
            if word.find(num) != -1:
                c +=1
        if c == 0:
            word2.append(word)

    words = list(set(word2))
    return words


def password_suggestion(password):
    rating = password_rating(password)

    a,b,c,d = 0,0,0,0
    suggestion = []
    if len(password) < 8:
        suggestion.append("You password is too short try to make it longer")
    elif len(password) > 20:
        suggestion.append("You password is too long try to make it shorter")

    for i in password:
        if i in numbersL:
            a += 1
    if a == 0:
        suggestion.append("Add some numbers to your password")


    for i in password:
        if i in upperCasesL:
            b += 1
    if b == 0:
        suggestion.append("Add some upper case letters to your password")

    for i in password:
        if i in lowerCasesL:
            c += 1
    if c == 0:
        suggestion.append("Add some lower case letters to your password")

    for i in password:
        if i in allSymbolsL:
            d += 1
    if d == 0:
        suggestion.append("Add some symbols to your password")

    words = check_dictionary(password)
    if len(words) != 0:
        words_msg =  f"Your password has some real words ("
        for word in words:
            if word == words[-1]:
                words_msg += f"{word}) try to change them"
            else:
                words_msg += f"{word} - "

        suggestion.append(words_msg)

    while len(suggestion) < 5:
        suggestion.append("")
    c = 0

    for x in suggestion:
         if x == "":
            c += 1

    if c == 5:
        return rating[0],rating[1], ["your password is great. Good Job!","","","",""]
    else:
        return rating[0],rating[1],suggestion