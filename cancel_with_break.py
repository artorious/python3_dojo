#!/usr/bin/env python3
''' Infinite loop with a break statement
Loops until requirement is met and cancels loop with break.
'''

while True:
    stuff = input('String to Capitalize [type q to quit]: ')
    if stuff.upper() == 'Q':
        break
    print(stuff.capitalize())