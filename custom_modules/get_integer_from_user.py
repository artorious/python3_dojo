#!/usr/bin/env python3
'''Prompt user for an integer '''

def get_integer():
    '''Prompt user for an integer'''
    # init
    valid_value = False

    while not valid_value:
        try:
            value = int(input('Enter an integer: '))  
            valid_value = True # Terminate loop after getting a valid value
        except ValueError:
            print('Expected a number')
            print('Please enter an interger')
            continue # Try Again
    return value

if __name__ == '__main__':
    get_integer()




