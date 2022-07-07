import random
import string
import json
def generate_random_string(length):
    letters = string.ascii_lowercase
    stroing = ''
    for i in range(0, length):
        stroing += random.choice(letters)
    return stroing

random_dict = dict(zip([generate_random_string(4) for _ in range(5)], [generate_random_string(7) for _ in range(5)]))
random_list = [generate_random_string(3) for _ in range(5)]
random_dict[list(random_dict.keys())[2]] = random_list
print(f'dict: {random_dict}\nlist: {random_list}')
with open('samplejson.json', 'w+') as outjson:
    json.dump(random_dict, outjson)

with open('samplejson.json', 'r') as outjson:
    json_read = json.load(outjson)
print(f'loaded json - {json_read}')
print(json_read[list(json_read.keys())[2]])
