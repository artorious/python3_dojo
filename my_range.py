#!/usr/bin/env python3
""" A play at generators
Simulate  the behaviour of the built-in range expression
NOTE:
    A generator is an object that generates a sequence of values.
    Code that uses a generator may obtaian one value at a time without the 
    possibility of revisiting earlier values. (consume a generator's product)
"""

def range_custom(arg1, arg2=None, step=1):
    """(int, int, int) - generator
    Simulate  the behaviour of the built-in range expression
    """
    
    if arg2 != None: # Do we have atleast two args
        begin = arg1
        end = arg2
    else: # When it's one arg, default start at zero
        begin = 0
        end = arg1
            
    i = begin
    while i != end:
        yield i
        i += step

if __name__ == '__main__':
    for num in range_custom(1, 11, 2):
        print(num, end=' ')

    for i in range(10):
        pass