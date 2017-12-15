#!/usr/bin/env python3
''' Adds up a sequence of non-negative integers from user.
User ends list with a negative integer to display the sum of the non-negative 
integers. Displays 0 if the user enters no non-negative integers. 
'''
# Init
entry = 0 # Control loop
sum = 0

# Get user input
print('Enter numbers to sum up, negative numbers ends list: ')
while entry >= 0: 
    try:
        entry = int(input('>>> '))
        if entry > 0: # Check for negative integer
            sum += entry
    except ValueError:
        print('Expected integers')
print('Sum =', sum)