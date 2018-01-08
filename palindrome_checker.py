#!/usr/bin/env python3
"""A Palindrome Checker Program

Determines if a given string is a palindrome.
NOTE: A Palindrome is something that reads the same forwards and backwards. 
E.g the words 'level' and 'radar'
"""

import custom_modules.stack as stack

print(__doc__) # Greeting
print()
# Init
char_stack = stack.get_stack() # Empty list
empty_string = ''
chars = input('Enter test-string [Return exits]: ').strip() # User Input

while chars != empty_string:
    if len(chars) == 1: # Empty string
        print('A one letter word is by definition a palindrome\n')
    else:
        # Init
        is_palindrome = True # Assume b4 testing
        # chars (from front) that must match chars on the rear (working backwards) 
        compare_len = len(chars) // 2 
        # push 2nd half of string onto stack
        for char in range(compare_len, len(chars)):
            stack.push(char_stack, chars[char])
        # pop chars and compare to 1st half of string
        compared_items = 0
        while compared_items < compare_len and is_palindrome:
            char_to_check = stack.pop(char_stack)
            if chars[compared_items].lower() != char_to_check.lower():
                is_palindrome = False # Exit comparison loop
            compared_items += 1 # Next char to compare
        # Display Results
        if is_palindrome:
            print('{0} IS a palindrome\n'.format(chars))
        else:
            print('{0} IS NOT a palindrome\n'.format(chars))
    # Get next string
    chars = input('Enter test-string [Return exits]: ').strip() # User Input



