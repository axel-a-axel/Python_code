import random
import copy

def recursion_sum(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + recursion_sum(arr[1:])

def non_rec_sum(arr):
    summed_arr = 0
    for i in range(0, len(arr)):
        summed_arr += arr[i]
    return summed_arr


initial = []
for i in range(0, 5):
    initial.append(random.randint(0, 5))
print('init: %s' % initial)
correct_mod = non_rec_sum(initial)
print('correct sum is %s' % correct_mod)
modified = recursion_sum(initial)
print("modified is %s" % modified)