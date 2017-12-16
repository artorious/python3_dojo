#!/usr/bin/env python3
'''Prompt user for an float '''

def get_float():
    '''Prompt user for an float'''
    # init
    valid_value = False

    while not valid_value:
        try:
            value = float(input('Enter an floating-point number: '))  
            valid_value = True # Terminate loop after getting a valid value
        except ValueError:
            print('Expected a number')
            print('Please enter a floating-point number')
            continue # Try Again
    return value

if __name__ == '__main__':
    get_float()




