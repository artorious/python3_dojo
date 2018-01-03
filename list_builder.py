#!/usr/bin/env python3
""" A play on python lists
Build custom lists as specified by the user
"""


def build_list_of_positive_integers():
    """(None) -> list
    Builds a list of non-negative integers from input provided by user
    Returns the list
    """
    
    result = [] # Init empty list
    in_val = 0 # Ensure loop is entered atleast once

    while in_val >= 0:
        
        try:
            in_val = int(input('Enter positive integer (-1 quits): '))
            
            if in_val >= 0:         # Check for positive int, else exit loop
                result += [in_val]  # Add item to list

        except ValueError as verr:
            print('Expected positive Integer...{0}'.format(verr))
            print('Try again')
            continue # 
        
    return result

def avg_numbers_in_list():
    """
    Averages numbers in a dynamically built list 
    """
    # Init
    total = 0.0
    numbers_list = []
    valid_list_length = False
    # Get length of list from user 
    while not valid_list_length:    
        try:
            print('How many entries to the list? ')
            number_of_entries = int(input('Enter positive integer (-1 quits): '))
            if number_of_entries > 0:
                valid_list_length = True
            elif number_of_entries == -1:
                print('Quiting.........')
                
                break
            else:
                continue
        except Exception as err:
            print('Expected positive integer : {0}'.format(err))
    
    if number_of_entries == -1: 
        return 'Exiting'
    else:
        print('Please enter {0} Numbers'.format(number_of_entries))
        for item_no in range(0, number_of_entries):
            valid_list_item = False
            while not valid_list_item:
                try:
                    list_item = float(input('Enter list item #{0} : '.format(item_no)))
                    numbers_list += [list_item]
                    total += list_item
                    valid_list_item = True

                except Exception as err:
                    print('Expected Number : {0}'.format(err))
                    print('Try again')
                    continue
        
        # Print numbers entered
        print(end='Numbers entered: ')
        for list_item in numbers_list:
            print(list_item, end=', ')
        print()

        # Calculate Avg
        print('Average : {0}'.format(total / number_of_entries))

def prefix_and_sufix_a_list(the_list=[1, 2, 3, 4, 5, 6, 7, 8, 9]):
    """(list) -> str
    Prints all the prefixes and suffixes of <the_list>
    """
    print('Prefixes of {0}'.format(repr(the_list)))
    for lst_item in range(0, len(the_list) + 1):
        print('<{0}>'.format(the_list[0 : lst_item]))
    for lst_item in range(0, len(the_list) + 1):
        print('<{0}>'.format(the_list[lst_item : len(the_list) + 1]))
    print('Suffixes of {0}'.format(repr(the_list)))

if __name__ == '__main__':
    # List slicing 
    lst = [10, 20, 30,40, 50, 60, 70, 80, 90, 100, 110, 120]
    # print(lst)
    # print(lst[0:3])
    # print(lst[4:8])
    # print(lst[2:5])
    # print(lst[-5:-3])
    # print(lst[:3])
    # print(lst[4:])
    # print(lst[:])
    # print(lst[-100:3])
    # print(lst[4:100])
    # print(lst[2:-2:2])
    # print(lst[::2])
    # print(lst[::-1])

    prefix_and_sufix_a_list(lst)