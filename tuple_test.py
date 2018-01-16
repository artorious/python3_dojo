#!/usr/bin/env python3
""" A play on Python Tuples
Compare the usage of lists vs. tuples 
"""
# Program Greeting
print(__doc__)
print()

# Init
my_list = [1, 2, 3, 4, 5, 6, 7]
my_tuple = (1, 2, 3, 4, 5, 6, 7)

# Display
print('The list: {0}'.format(my_list))
print('The tuple: {0}'.format(my_tuple))
print()

# Access elem by index
print('The first element in the List: {0}'.format(my_list[0]))
print('The Last element in the tuple: {0}'.format(my_tuple[-1]))
print()

# Iteration
print('Iterate over each list element and display it multiplied by two:', end=' ')
print([elem * 2 for elem in my_tuple])
print('Iterate over each tuple element and display it multiplied by two:', end=' ')
print([elem * 2 for elem in my_tuple])
print()

# Slicing
print('List slice (to reverse): {0}'.format(my_list[::-1]))
print('Tuple slice (to reverse): {0}'.format(my_tuple[::-1]))
print()

# Modification
try:
    moded_list, moded_tuple = False, False # Init
    print('Modify list and tuple')
    my_list[0], moded_list = 9, True
    my_tuple[0], moded_tuple = 9, True

except TypeError as terr:
    print('Oops... Error: {0}'.format(terr))

print('Modifed list : {0} : {1}'.format(moded_list, my_list))
print('Modifed Tuple: {0} : {1}'.format(moded_tuple, my_tuple))
print()

# Construct a sequence of tuples from two lists
lst1 = [1, 2, 3, 4, 5, 6, 7, 8]
lst2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for t in zip(lst1, lst2):
    print(t)