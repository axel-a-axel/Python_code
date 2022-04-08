from collections import deque
import random
import string

def check_if_this_what_i_search(name):
    return name[-2:] == 'gy'

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
    print(list(graph)[0])
    first_in_graph = list(graph)[0]
    fill_que = deque()
    fill_que += graph[first_in_graph]
    while fill_que:
        current = fill_que.popleft()
        graph[current] = [generate_random_string(5), generate_random_string(5), generate_random_string(5)]
    print(graph)
    return graph


graph2 = generate_graph()
print(graph2)
first_in_graph2 = list(graph2)[0]
search_queue(graph2, first_in_graph2)