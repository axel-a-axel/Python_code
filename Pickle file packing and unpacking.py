import random
import string
import pickle
with open('data.pkl', 'w+b') as data:
    arr1 = [random.randrange(1,100) for _ in range(10)]
    arr2 = [random.choice(string.ascii_lowercase) for _ in range(10)]
    dict1 = dict(zip(arr1, arr2))
    dict2 = dict(zip(arr2, arr1))
    print(dict1, dict2, sep='\n')
    pickle.dump(dict1, data)
    pickle.dump(dict2, data)
with open('data.pkl', 'rb') as data:
    readed = pickle.load(data)
    print(readed)