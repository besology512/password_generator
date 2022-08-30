# # import random                                 #my sad function
# # def distrip(ncat,nchar):
# #     countDitrip = []
# #     while sum(countDitrip) != nchar:
# #         print('infinte')
# #         countDitrip = []
# #         for i in range(ncat):
# #             countDitrip.append(random.randint(0,nchar))
# #     return countDitrip
# # print(distrip(3,10))


# # import enchant
# # help(enchant)
# # import PyEnchant


# # userinput = ''
# # # def userPass():
# # #     if userinput:

# # x = 'cat'
# # # if word in x:
# # #     print('false')
# # # if x in dict.__dict__:
# # #     print('True')
# # # else:
# # #     print('false')
# # import string
# # print([space for space in string.whitespace][0])
# from sre_parse import SPECIAL_CHARS
# import main as m
# import random
# import string
# import clipboard  # must install it using < pip install clipboard >
# import PyDictionary as dict
# password = 'sdfsdfSD'
# password = [i for i in password]


# def checkPass():  # complete it and check if the password meets the conditions
#     if m.upper == True:
#         for i in range(len(password)-1):
#             if any((n.isupper()) for n in password):
#                 break
#             else:
#                 for j in range(random.randrange(1, 3)):
#                     password[random.randrange(0, len(
#                         password)-1)] = [char for char in string.ascii_uppercase][random.randrange(0, 25)]

#     if m.lower == True:
#         for i in range(len(password)-1):
#             if any((n.islower()) for n in password):
#                 break
#             else:
#                 for j in range(random.randrange(1, 3)):
#                     password[random.randrange(0, len(
#                         password)-1)] = [char for char in string.ascii_lowercase][random.randrange(0, 25)]
#     if m.Numbers == True:
#         for i in range(len(password)-1):
#             if any((n.isdigit()) for n in password):
#                 break
#             else:
#                 for j in range(random.randrange(1, 3)):
#                     password[random.randrange(0, len(
#                         password)-1)] = [digit for digit in string.digits][random.randrange(0, 9)]
#     if m.wspace == True:
#         for i in range(len(password)-1):
#             if any((n == ' ') for n in password):
#                 break
#             else:
#                 for j in range(random.randrange(1, 3)):
#                     password[random.randrange(0, len(password)-1)] = ' '
#     if m.symbols == True:
#         for i in range(len(password)-1):
#             if any((n in SPECIAL_CHARS) for n in password):
#                 break
#             else:
#                 for j in range(random.randrange(1, 3)):
#                     password[random.randrange(0, len(
#                         password)-1)] = [s for s in string.printable][62:94][random.randrange(0, 32)]


# checkPass()
# print(password)
# print(random.randrange(0, 3))
# a  = [[1,2,3]]
# print(a[0][0:])
# grades = {
#     202101074: [1,4,5],
#     202101257: [5,7,8]
# }
# print(grades[202101074][0])
# import string

# print([s for s in string.printable][62:94])