#!/usr/bin/env python3
'''Measures elapsed time.
Calculates:
    * How long it takes a user to enter a character from the keyboard.  
    * How long it takes for a Python program to add up all the integers
        from 1 -> n (n provided by user) 
    * Countdown from 10 with 1 second intervals between numbers
'''
from time import clock, sleep
from custom_modules.get_positive_number_from_user import get_positive_num

print(__doc__) # Program greeting

#######################################
print('Enter Name: ', end='')
start_time = clock()
name = input()
elapsed_time = clock() - start_time
print('It took {0} {1} seconds to respond'.format(name, elapsed_time))
print('\n')

#######################################
# Init
total = 0
value = int(get_positive_num()) #
start_stopwatch = clock()
for integer in range(1, value + 1):
    total += integer
stop_stopwatch = clock() - start_stopwatch
print('0 + 1 + ..... + {0:,} = {1:,} [Calculation time: {2}]'.format(value, total, stop_stopwatch))
print('\n')

#################
print('Start Countdown: ')
for countdown in range(10, -1, -1): # Range 10, 9, 8, ...., 0
    print(countdown)
    sleep(1)
print()