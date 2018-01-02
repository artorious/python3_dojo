#!/usr/bin/env python3
""" String Objects
"""

def get_str():
    """
    Prompt user for a string
    """
    valid_input = False
    while not valid_input:
        try:
            sample_str = input('>>>  ')
            valid_input = True 
            return sample_str

        except Exception as err:
            return 'Expected String : {0}'.format(err)


if __name__ == '__main__':

    name = {}  # Init name
    print('Enter Name :', end='')
    name['Name'] = list(get_str().strip().upper().split(' '))
    print(name)


