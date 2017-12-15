#!/usr/bin/env python3
'''Prints all the different arrangements of the letters A,B,C, and D.
Uses a triply-nested loop to print all the different arrangements.
Each string printed is a permutation of ABC.'''

for first in 'ABCD': # First letter varies from A to D
    for second in 'ABCD':    # Second letter varies from A to D
        if second != first: # Check for duplication of first letter
            for third in 'ABCD': # Third letter varies from A to C
                if third != first and third != second:  # Check for duplication of first and second  letters
                    for fourth in 'ABCD':
                        if fourth != first and fourth != second and fourth != third:  # Check for duplication of first, second and third letters
                            print(first + second + third + fourth)