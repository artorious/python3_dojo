#!/usr/bin/env python3
"""
Create both a set and a list, each containing the first 1,000 perfect squares. 
Performs searches both data structures for, and do nothing with all the 
integers from 0 to 999,999.
Report the time required for the efforts
"""
from time import clock

data_struct_size = 1000
big_set = {x ** 2 for x in range(data_struct_size)}
big_list = [x ** 2 for x in range(data_struct_size)]
search_size = 1000000

print('VERIFY\nSet:\v{0}\nList:\v{1}'.format(type(big_set), type(big_list)))

start_time = clock()
for search_item in range(search_size):
    if search_item in big_set:
        pass
stop_time = clock()
print('Set Search - Elapsed Time: {0}'.format(stop_time - start_time))

start_time = clock()
for search_item in range(search_size):
    if search_item in big_list:
        pass
stop_time = clock()
print('List Search Elapsed Time: {0}'.format(stop_time - start_time))

