#!/usr/bin/env python3
'''Prints all the integers and their associated factors from 1-n'''

# init
count = 1 # Start from 1 (The numbers being examined)
valid_value = False

##------ Get positive integer from user ------- ###
while not valid_value:
    try:
        value = int(input('Enter an integer Value: '))  # Enter Max value
        if value > 0:
            valid_value = True # Terminate loop after getting a valid value
        else:
            print('Please enter a positive integer')
            continue # Try entering value again

    except ValueError:
        print('Expected integers...')

##------- The Algorithm -------- ##

while count <= value:                              # Dont go past max
    factor = 1                                     # 1 is a universal factor
    print('{0:>3}: '.format(repr(count)), end='')  # Which integer are we examining?
    while factor <= count:                         # Factors are <= the number being examined
        if count % factor == 0:                    # Test whether factor is a factor of the number being examined
            print(factor, end=' ')                 # Dispaly the factor if yes
        factor += 1                                # Try next possible factor
    print()                                        # Move to the next line
    count += 1                                     # Examine next number

    