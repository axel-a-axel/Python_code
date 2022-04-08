from collections import deque
import random

def generate_random_int_string(length):
    string = ''
    for i in range(0, length):
        string += str(random.randint(0,9))
    return string

def check_if_this_what_i_search(name):
    return name[-2:] == '00'

def search_queue(grapp, name):
    search_q = deque()
    search_q += grapp[name]
    print(search_q)
    searched = []
    while search_q:
        current = search_q.popleft()
        if not current in searched:
            if check_if_this_what_i_search(current):
                print('i found %s' % current)
                return True
            else:
                search_q += grapp[current]
                searched.append(current)
    return False




graph = {}
graph['firsts'] = ['second1', 'second2', 'second3']
graph['second1'] = [generate_random_int_string(4), generate_random_int_string(4), generate_random_int_string(4)]
graph['second2'] = [generate_random_int_string(4), generate_random_int_string(4), generate_random_int_string(4)]
graph['second3'] = [generate_random_int_string(4), generate_random_int_string(4), generate_random_int_string(4)]

print(graph)
search_queue(graph, 'firsts')

