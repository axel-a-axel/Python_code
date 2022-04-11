from collections import deque
import random
import string

def check_if_this_what_i_search(name, piece):
    return name[-2:] == piece

def search_queue(grapp, name, piece):
    search_q = deque()
    search_q += grapp[name]
    searched = []
    while search_q:
        current = search_q.popleft()
        if not current in searched:
            if check_if_this_what_i_search(current, piece):
                print('i found %s' % current)
                return True
            else:
                search_q += grapp[current]
                searched.append(current)
    return False
def generate_random_string(length):
    letters = string.ascii_lowercase
    stroing = ''
    for i in range(0, length):
        stroing += random.choice(letters)
    return stroing


def generate_graph():

    graph = {}
    graph[generate_random_string(3)] = [generate_random_string(4), generate_random_string(4), generate_random_string(4)]
    print(graph)
    print('first item is %s' % list(graph)[0])
    first_in_graph = list(graph)[0]
    fill_que = deque()
    fill_que += graph[first_in_graph]
    while fill_que:
        current = fill_que.popleft()
        graph[current] = [generate_random_string(5), generate_random_string(5), generate_random_string(5)]
    print(graph)
    empty_fill_que = deque()
    empty_fill_que += graph[first_in_graph]
    while empty_fill_que:
        ecurrent = empty_fill_que.popleft()
        if ecurrent not in graph:
            graph[ecurrent] = []
        else:
            empty_fill_que += graph[ecurrent]

    return graph


graph2 = generate_graph()
print('initial graph is %s' % graph2)
item_to_search = generate_random_string(2)
first_in_graph2 = list(graph2)[0]
print('i am searching for -%s in graph' % item_to_search)
isFound = search_queue(graph2, first_in_graph2, item_to_search)
print('did i find item? %s' % isFound)