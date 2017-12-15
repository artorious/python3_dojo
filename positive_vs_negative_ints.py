#!/usr/bin/env python3
'''Positve Vs Negtive integers. 
The user can enter any number of positive and negative integer values, 

Displays the number of positive values entered, as well as the number 
of negative values.
'''

# Init
positive_int_count = 0
negative_int_count = 0
terminate = False

while not terminate:
    try:
        print('Enter 0 to Finish')
        the_value = int(input('Enter an interger: '))
        if the_value > 0:
            print(the_value, 'is positive')
            positive_int_count += 1
        elif the_value < 0:
            print(the_value, 'is negative')
            negative_int_count += 1
        elif the_value == 0:
            print('Positive integer count: ', positive_int_count)
            print('Negative integer count: ', negative_int_count)
            print('Exiting..............')
            terminate = True

    except ValueError:
        print('Please provide integer')
