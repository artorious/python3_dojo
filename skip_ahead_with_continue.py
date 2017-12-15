#!/usr/bin/env python3
'''Skip ahead to the next iteration.

Reads an integer, prints it's square if it's odd, and skip if it's even.
'''

while True:
    value = input('Integer, please [q to quit]: ')
    if value.upper() == 'Q': # Quit
        break
    number = int(value)
    if number % 2 == 0: # Even No.
        continue
    print('{0:,} squared is {1:,}'.format(number,number * number))
