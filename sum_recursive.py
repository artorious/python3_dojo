#!/usr/bin/env python3
"""
A Function that sums up all the values in a nested number list
"""

def r_sum(nested_num_list):
    """ (list) -> float 
    
    Sum up the values in a nested numbers list
    """
    cntr = 0
    for elem in nested_num_list:    # Traverse the list
         # Recursive call for nested lists
        if isinstance(elem, list):
            cntr += r_sum(elem) 
        # Base case   
        elif isinstance(elem, (int, float)):
            cntr += elem            
        else:
            raise TypeError('Invalid value found in list: {0}'.format(elem)) 
    return cntr

def main():
    print(r_sum([4]))
    print(r_sum([3, 4]))
    print(r_sum([3, 4, 5.6]))
    print(r_sum([3, 3, 3, 3, 4, 1, 9, 44, -2, 8, 8]))
    print(r_sum([3, 3, 3, 3, 'four', 1, 9, 44, -2, 8, 8]))

if __name__ == '__main__':
    main()