#!/usr/bin/env python3
'''Calculates the Square root of a number supplied by the user
'''

from math import sqrt

print(__doc__) # Program Greeting
# init
valid_value = False

##------ Get positive integer from user ------- ###
while not valid_value:
    try:
        value = int(input('Enter an integer Value: '))  # Enter Max value
        if value > 0:
            value = True # Terminate loop after getting a valid value
        else:
            print('Please enter a positive integer')
            continue # Try entering value again

    except ValueError:
        print('Expected integers...')

##------- The Algorithm -------- ##