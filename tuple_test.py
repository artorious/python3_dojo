#!/usr/bin/env python3
""" Compare the usage of lists vs. tuples """
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
for elem in my_list:
    print(elem * 2, end=' ')
print()

# Iteration
print('Iterate over each tuple element and display it multiplied by two:', end=' ')
for elem in my_tuple:
    print(elem * 2, end=' ')
print()

# Slicing
print('List slice (to reverse): {0}'.format(my_list[::-1]))
print('Tuple slice (to reverse): {0}'.format(my_tuple[::-1]))
print()
# Modification
try:
    print('Modify list and tuple')
    my_list[0] = 9
    my_tuple[0] = 9
except TypeError as terr:
    print(terr)

print('Modifed list : {0}'.format(my_list))
print('Modifed Tuple?: {0}'.format(my_tuple))