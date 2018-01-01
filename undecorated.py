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
    return x if x > y else y

def summation(begin, end):
    """(int, int) -> int
    Add up the integers in the range <begin> ...<end> -1, inclusive
    """
    total = 0

    while begin != end:
        total += begin
        begin += 1
    return total

def gcd(num1, num2):
    """(int, int) -> int
    Uses Euclid's method to compute the greatest common factor
    (greatest common divisor) of two integers, <num1> and <num2>
    Returns greatest common factor (gcd) of the two integers
    """
    if isinstance(num1, int) and isinstance(num2, int):
        if num1 == 0:
            return num2
        elif num2 == 0:
            return num1
        else:   
            if num1 > num2: # Handle RuntimeError: maximum recursion depth exceeded in comparison
                return gcd(num2, num1 % num2)
            else:
                return gcd(num1, num2 % num1)
    else:
        return 'Expected Two Integers'

def star_rect(length, width):
    """(int, int) -> int
    Draw a <length> x <width> rectangle with asterisks
    """
    for row in range(width):
        print('*' * length)

print("The maximum of 20 and 30 is", max(20, 30))
print("The maximum of 30 and 20 is", max(30, 20))
print("The maximum of 20 and 20 is", max(20, 20))
print('------------------------')
print("The GCD of 20 and 30 is", gcd(20, 30))
print("The GCD of 30 and 20 is", gcd(30, 20))
print("The GCD of 20 and 20 is", gcd(20, 20))
print('------------------------')
print("The summation from 20 to 30 is", summation(20, 30))
print('------------------------')
star_rect(7, 3)
print('------------------------')
star_rect(4, 4)
print('------------------------')
star_rect(12, 5)
print('------------------------')
print(randrange(10, 21), "is a pseudorandom integer in the range 10 to 20, inclusive")