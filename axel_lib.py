import random
import string

def generate_random_lowercase_string(length,*, lower=True,spaces=False, upper=False, digits=False, punct=False):
    letters = ''
    if lower == True:
        letters += string.ascii_lowercase
    if upper == True:
        letters += string.ascii_uppercase
    if digits == True:
        letters += string.digits
    if length == 1:
        return random.choice(letters)
    if punct == True:
        letters += string.punctuation
    if spaces == True:
        letters += ' '

    res_string = ''
    for i in range(1, length):
        res_string += random.choice(letters)
    return res_string
