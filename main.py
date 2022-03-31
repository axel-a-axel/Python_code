import random

def binarysearch(search_min, search_max, item):
    while search_min <= search_max:
        guess = (search_max + search_min) // 2
        print("looking for %s, guess is %s" % (item, guess))
        if guess == item:
            print("looked for %s and guess was %s" % (item, guess))
            return guess
        elif guess < item:
            search_min = guess + 1
            print("more")
        elif guess > item:
            search_max = guess - 1
            print("less")
        else:
            return None

mmin = random.randint(0, 10)
mmax = random.randint(90000, 150222)
iitem = random.randint(mmin, mmax)
binarysearch(mmin, mmax, iitem)