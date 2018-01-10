#!/usr/bin/env python3
""" Phone Number Spelling Program

Generates all possible spellings of the last four digits of any given 
phone number
"""

def get_phone_num():
    """ () -> str

    Returns entered phone number in the form 123-456-7890.
    """
    # Init
    valid_ph_num = False
    empty_str = ''
    # Prompt for phone number
    while not valid_ph_num:
        phone_num = input('Enter phone numbr (xxx-xxx-xxxx): ')
        # check if valid form
        if len(phone_num) != 12 or phone_num[3] != '-' or phone_num[7] != '-':
            print('Invalid Entry - Must be of the form xxx-xxx-xxxx\n')
        else:
            # Check for non-digis
            digit_index = 0
            valid_ph_num = True
            phone_num_digits = phone_num.replace('-', empty_str)
        
            while valid_ph_num and digit_index < len(phone_num_digits):
                if not phone_num_digits[digit_index].isdigit():
                    print('* Non-digit: {0} *\n'.format(phone_num_digits[digit_index]))
                    valid_ph_num = False
                else:
                    digit_index += 1
    return phone_num

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