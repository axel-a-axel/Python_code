import random

def samestuff(arr):
    wasExecutedOnce = 0
    for i in range(0, len(arr)-1):
        if arr[i] > arr[i+1]:
            temp = arr[i]
            arr[i]= arr[i+1]
            arr[i+1] = temp
            wasExecutedOnce += 1
            print('current array: %s, executed times: %s' % (arr, wasExecutedOnce))
    return arr, wasExecutedOnce
def recursSort(arr):
    nuarr, once = samestuff(arr)
    if once == 0:
        return nuarr
    else:
        return recursSort(nuarr)



initial = []
for i in range(0, 20):
    initial.append(random.randint(-20, 20))
print('init: %s' % initial)
modified = recursSort(initial)
print('final %s' % modified)