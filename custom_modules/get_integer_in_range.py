#!/usr/bin/env python3
"""Prompt user for an integer within the specified range
"""

def get_int_in_range(first, last):
    """ (int, int) -> int
    
        Prompt user for an integer within the specified range
        <first> is either a min or max acceptable value.
        <last> is the corresponding other end of the range, either a min or max 
        acceptable value.
        Returns an acceptable value from the user
    """
    if isinstance(first, int) and isinstance(last, int):
        if first > last:    # If larger no. is provided 1st
            first, last = last, first   # Switch the parameters
        # Insist on value in the range <first>...<last>
        try:
            in_value = int(input('Enter value in the range {0} .... {1} : '\
                    .format(first, last)))
        
            while in_value < first or in_value > last:
                print('{0} IS NOT in the range {1} .... {2}'.format(in_value, first, last))
                in_value = int(input('Try again: '))
            
            return in_value

        except ValueError as err:
            return err
        

    else:
        return 'Expected an integers. int_in_range({0}, {1}) not surpported' \
                .format(type(first), type(last))

if __name__ == '__main__':
    print(__doc__)
    print(get_int_in_range(-100, 100))
    print(get_int_in_range(10, 20))
    print(get_int_in_range(5, 5))
    print(get_int_in_range(-1, 1))