#!/usr/bin/env python3
""" A Recipe Conversion Program 

Converts the measured amount of ingredients of recipes,
based on a provided conversion factor, to vary the number of servings. 
"""

from custom_modules.rational_numbers import Rational


def get_file():
    """ () -> tuple

    Returns as a tuple the file name entered by the user and the 
    open file object. If the file exceeds three atempts of opening
    successfully, an IOError exception is raised. 
    """
    return 

def remove_measure(line):
    """ (str) -> str

    Returns provided line with any initial digits and fractions
    (and any sorrounding blanks) removed.
    """
    return

def scan_as_fraction(line):
    """ (str) -> Rational

    Scans all digits, including fractions, and returns as a
    Rational object. For example, '1/2' would return as a fraction value 1/2,
    '2' would return as fraction 2/1, and '2 1/2' would return as fraction 
    value 3/2.
    """

    return

def convert_line(line, factor):
    """ (str, Rational) -> str

    If a line begins with a digit, returns line with the value multiplied
    by factor. Othewise, returns line unaltered
    (e.g., for a factor of 2, '1/4 cup' returns a '1/2 cup'.)
    """
    return

def main():
    """ Recipe Conversion """
    # Program Greeting
    print('''
    This program will convert a given recipe to a different
    quantity based on a specified conversion factor. Enter a
    factor of 1/2 to halve, 2 to double, 3 to tripple, etc.\n
    ''')

    try:
        # get file name and open file
        file_name, input_file = get_file()

        # get conversion factor
        conv_factor = input('Enter conversion factor:\n>>> ')
        conv_factor = scan_as_fraction(conv_factor)

        # open output file named 'conv_' + file_name
        output_file_name = 'conv_' + file_name
        output_file = open(output_file_name, 'w')

        # Convert recipe
        empty_str = ''
        recipe_line = input_file.readline()

        while recipe_line != empty_str:   
            recipe_line = convert_line(recipe_line, conv_factor)
            output_file.write(recipe_line)
            recipe_line = input_file.readline()
        
        # Close files
        input_file.close()
        output_file.close()

        # Display completion message to user
        print('Converted recipe in file: {0}'.format(output_file_name))
        
    # Catch file open error
    except IOError as ioerr: 
        print(ioerr)

if __name__ == '__main__':
    main()