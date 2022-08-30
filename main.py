import user_input as u
import random
import operations as O
import passwordlist as P
import modify_and_rate as MR

def user_choice():
    if u.upper == True:
        O.upper_case()
    if u.lower == True:
        O.lower_case()
    if u.Numbers == True:
        O.numbers()
    if u.exclude_ambsymbols == True and u.symbols == True:
        O.not_ambsymbols()
    if u.exclude_ambsymbols == False and u.symbols == True:
        O.all_symbols()
def get_password(length):
    user_choice()
    for i in range(length):
        x = random.randrange(0, len(P.pass_options))
        P.password.append(P.pass_options[x])
    MR.check_pass()
    return P.password
final_password = ''.join(get_password(u.Plength))
print(final_password)
O.copy(final_password) #this is copying another password
MR.password_rating(P.password) 
print(MR.passStrength)
print('password is working')
