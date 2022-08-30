import random
import string
import clipboard  # must install it using < pip install clipboard >
import PyDictionary as dict
import passwordlist as P
import user_input as u
from sre_parse import SPECIAL_CHARS


def upper_case():
    # one line can be separated
    print('upper case is working')
    return P.pass_options.extend([char for char in string.ascii_uppercase])


def lower_case():
    print('lower case is working')
    return P.pass_options.extend(
        [char for char in string.ascii_lowercase])


def numbers():
    print('numbers is working')
    return P.pass_options.extend([digit for digit in string.digits])


def all_symbols():
    print('all_symbols is working')
    return P.pass_options.extend(
        [s for s in string.printable][62:94])


def not_ambsymbols():
    print('not allsymbols is working')
    return P.pass_options.extend(
        [s for s in string.printable][62:84])


def Space():
    print('space is working')
    return P.pass_options.append(' ')


def copy(passwordcopy):
    clipboard.copy(passwordcopy)



print('circular')
print('operation is working')
