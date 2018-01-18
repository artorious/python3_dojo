#!/usr/bin/env python3
""" enumurate - demostrate with lists, tuples, dictionaies, sets 
and generators """

a_list = [10, 20, 30, 40, 50]
a_tuple = 100, 200, 300, 400, 500
a_dict = {'A': 4, 'B': 18, 'C': 0, 'D': 3}
a_set = {1000, 2000, 3000, 4000, 5000}
names = ['Bob', 'Alice', 'Guido']

def gen(n):
    """ (int) -> generator
    Generate n, n - 2, n - 3, ..., 0
    """
    for i in range(n, -1, -2):
        yield i



print(a_list)
print(a_tuple)
print(a_dict)
print(a_set)
print()
[print(_, end=' ') for _ in enumerate(a_list, 1)]
print()
[print(_, end=' ') for _ in enumerate(a_tuple)]
print('\n')
[print('{}: {}'.format(index,value)) for index, value in enumerate(names)]
print()
{print(_, end=' ') for _ in enumerate(a_dict, 1)}
print()
{print(_, end=' ') for _ in enumerate(a_set, 1)}
print()

for x in enumerate(gen(10)):
    print(x, end=' ')
print()

for x in enumerate(gen(10), 1):
    print(x, end=' ')
print()