#!/usr/bin/env python3
""" A play at decorators
A simple application that uses a number of functions that accept two integer 
paramters and return an integer
"""

from random import randrange


def max(x, y):
    """(int, int) -> int
    Determine the maximum of <x> and <y>
    """
    call_string = "max({}, {})".format(x, y)
    print('>>> Calling {}'.format(call_string))
    result = x if x > y else y
    print('<<< Returning {} from {}'.format(result, call_string))

def summation(begin, end):
    """(int, int) -> int
    Add up the integers in the range <begin> ...<end> -1, inclusive
    """
    call_string = 'summation({0}, {1})'.format(begin, end)
    print('>>> Calling {0}'.format(call_string))

    total = 0

    while begin != end:
        total += begin
        begin += 1
    print('<<< Returning {0} from {1}'.format(total, call_string))
    return total

def gcd(m, n):
    """(int, int) -> int
    Uses Euclid's method to compute the greatest common factor
    (greatest common divisor) of two integers, <m> and <n>
    Returns greatest common factor (gcd) of the two integers
    """
    call_string = 'gcd({0} {1})'.format(m, n)
    print('>>> Calling {0}'.format(call_string))
    if n == 0:
        result = m
    else:
        result = gcd(n, m % n)
    print('<<< Returning {0} from {1}'.format(result, call_string))    
    return result

def star_rect(length, width):
    """(int, int) -> int
    Draw a <length> x <width> rectangle with asterisks
    """
    call_string = 'star_rect({0}, {1})'.format(length, width)
    print('>>> Calling {0}'.format(call_string))
    for row in range(width):
        print('*' * length)
    print('<<< Return {0} from {1}'.format(None, call_string))
max(20, 30)
print('------------------------')
max(30, 20)
print('------------------------')
max(20, 20)
print('------------------------')
gcd(20, 30)
print('------------------------')
gcd(30, 20)
print('------------------------')
gcd(20, 20)
print('------------------------')
summation(20, 30)
print('------------------------')
star_rect(7, 3)
print('------------------------')
star_rect(4, 4)
print('------------------------')
star_rect(12, 5)
print('------------------------')
print(randrange(10, 21), "is a pseudorandom integer in the range 10 to 20, inclusive")