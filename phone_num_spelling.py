#!/usr/bin/env python3
""" Phone Number Spelling Program

Generates all possible spellings of the last four digits of any given 
phone number
"""

def get_phone_num():
    """ () -> str

    Returns entered phone number in the form 123-456-7890.
    """
    return

def display_all_spellings(phone_num):
    """ (str) -> 
    
    Displays all posible phone numbers with the last four digits
    replaced with a corresponding letter from the phone keys
    """

    pass


if __name__ == '__main__':
    # Prog greeting
    print('''
    This program will generate all possible spaellings of the
    last four digits of any phone number\n''')
    terminate = False # Get phone number and display spellings
    while not terminate:
        phone_num = get_phone_num()
        display_all_spellings(phone_num)
        # Continue?
        response = input('Enter another phone number? (y/n): ')
        if response.lower() == 'n':
            terminate = True 