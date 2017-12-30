#!/usr/bin/env python3
""" A play at generators

NOTE:
    A generator is an object that generates a sequence of values.
    Code that uses a generator may obtaian one value at a time without the 
    possibility of revisiting earlier values. (consume a generator's product)
"""

def generate_multiples(m, n):
    """
    Create a generator inside of a function and 'return' it with yield keyword
    Yields the first <n> multiples of <m>
    """
    count = 0
    while count < n:
        yield m * count
        count += 1

if __name__ == '__main__':
    for mult in generate_multiples(3, 6):
        print(mult)