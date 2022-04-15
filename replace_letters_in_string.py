import random
import string

def generate_random_string(length):
    letters = string.ascii_lowercase
    temp_string= ''
    for i in range(0, length):
        temp_string += random.choice(letters)
    return temp_string


def replace_letters(string, letter1, letter2):
    for i in range(0, len(string)):
        if string[i] == letter1:
            string = string[0:i] + letter2 + string[i+1:]
    return string


initial_string = generate_random_string(random.randint(1, 40))
print('init string %s' % initial_string)
letter_to_replace = generate_random_string(1)
letter_to_be_replaced = generate_random_string(1)
print('imma replacing %s with %s' % (letter_to_be_replaced, letter_to_replace))
print(replace_letters(initial_string, letter_to_be_replaced, letter_to_replace))