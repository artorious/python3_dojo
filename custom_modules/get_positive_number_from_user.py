#!/usr/bin/env python3
""" Prompt user for a positve number ( integer or floating-point number).

    Returns  value (float)
"""

def get_positive_num():
    """ Prompt user for a positive number (integer or floating-point number)
    
        Returns the float
    """
    # init
    valid_value = False

    while not valid_value:
        try:
            value = float(input('Enter a positive number: '))  # Enter Max value
            if value > 0:
                valid_value = True # Terminate loop after getting a valid value
            else:
                print('Please enter a positive number')
                continue # Try entering value again

        except ValueError:
            print('Expected a number')

    return value

if __name__ == '__main__':
    get_positive_num()




