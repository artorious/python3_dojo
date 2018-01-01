#!/usr/bin/env python3
""" A play at decorators
A simple application that uses a number of functions that accept two integer 
paramters and return an integer
"""

from random import randrange

# Decorator
def show_call_and_return(f):
    """(function) -> function
    Accepts a single function <f> as a parameter
    Decorates <f> so its call will display the parameter and return values
    by wrapping <f> in some additional code in a local function

    Returns it's local function
    """
    
    func_name = f.__name__  # Get the function's name
    
    def execute_augmented(x, y):
        """ (int, int) -> int """
        
        call_string = '{0}({1}, {2})'.format(func_name, x, y)
        print('>>> Calling {}'.format(call_string))
        result = f(x, y)
        print('<<< Returning {} from {}'.format(result, call_string))        
        
        return result

    return execute_augmented

@show_call_and_return # Decorate
def max(x, y):
    """(int, int) -> int
    Determine the maximum of <x> and <y>
    """
    return x if x > y else y

@show_call_and_return # Decorate
def summation(begin, end):
    """(int, int) -> int
    Add up the integers in the range <begin> ...<end> -1, inclusive
    """
    
    total = 0

    while begin != end:
        total += begin
        begin += 1
    
    return total

@show_call_and_return # Decorate
def gcd(m, n):
    """(int, int) -> int
    Uses Euclid's method to compute the greatest common factor
    (greatest common divisor) of two integers, <m> and <n>
    Returns greatest common factor (gcd) of the two integers
    """
    
    if n == 0:
        result = m
    else:
        result = gcd(n, m % n)
    
    return result

@show_call_and_return # Decorate
def star_rect(length, width):
    """(int, int) -> int
    Draw a <length> x <width> rectangle with asterisks
    """
    call_string = 'star_rect({0}, {1})'.format(length, width)
   
    for row in range(width):
        print('*' * length)


if __name__ == '__main__':
    # Init: Decorate functions whose definition we do NOT control
    randrange_deco = show_call_and_return(randrange)

    # Display
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

    print("{0} is a pseudorandom integer in the range 10 to 20, inclusive".format(randrange_deco(10, 21)))