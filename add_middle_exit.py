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

while True:                         # Enter loop
    try:                            # Error-check user input
        entry = int(input('>>> '))  # Get the Value
        if entry < 0:               # Check for negative integer
            break                   # If negative, exit loop
        sum += entry                # Add entry to running sum
    except ValueError:
        print('Expected integers')
print('Sum =', sum)                 # Display the sum