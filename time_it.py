#!/usr/bin/env python3
'''Measures elapsed time.
Calculates:
    * How long it takes a user to enter a character from the keyboard.  
    * How long it takes for a Python program to add up all the integers
        from 1 to 100,000,000 
'''
from time import clock

print(__doc__) # Program greeting
#######################################
print('Enter Name: ', end='')
start_time = clock()
name = input()
elapsed_time = clock() - start_time
print('It took {0} {1} seconds to respond'.format(name, elapsed_time))
#######################################
# Init
total = 0
start_stopwatch = clock()
for integer in range(1, 100000001):
    total += integer
stop_stopwatch = clock() - start_stopwatch
print('Total: {0:,} -> Calculation time: {1}'.format(total, stop_stopwatch))


