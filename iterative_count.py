#!/usr/bin/env python3
'''Counts up from zero as long as the user wishes to.
The user continues the count by entering 'Y'.
The user discontinues the count by entering 'N'.
'''

# Init
count = 0
entry = 'Y'

while entry != 'N' and entry != 'n':
    print(count)
    entry = input('Please enter "Y" to continue or "N" to quit:  ')
    if entry.upper() == 'Y':
        count +=1  # Keep Counting
    elif entry.upper() != 'N': # Check for bad input. else must be "N" or "n"
        print('"{0}" is not a valid entry'.format(entry))

