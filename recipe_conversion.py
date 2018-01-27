#!/usr/bin/env python3
""" A Recipe Conversion Program 

Converts the measured amount of ingredients of recipes,
based on a provided conversion factor, to vary the number of servings. 
"""

from custom_modules.rational_numbers import Rational


def get_file():
    """ () -> tuple

    Prompts for a file name to open, returning both the file name and 
    associated file object as a tuple. If the file exceeds three atempts 
    of opening successfully, an IOError exception is raised. 
    """
    file_name = input('Enter file name:\n>>> ')
    input_file_opened = False
    num_attempts = 1

    while not input_file_opened and num_attempts < 3:
        
        try:
            input_file = open(file_name, 'r')
            input_file_opened = True

        except IOError:
            print('Oopss... File open Error!\n')
            num_attempts += 1
            file_name = input('Enter file name:\n>>> ')

    if num_attempts == 3:
        raise IOError('Exceeded number of file open attempts')

    return (file_name, input_file) 

def remove_measure(line):
    """ (str) -> str

    Returns provided line with any initial digits and fractions
    (and any sorrounding blanks) removed.
    """
    char_track = 0
    blank_char = ' '

    while char_track < len(line) and (line[char_track].isdigit() or \
            line[char_track] in ('/', blank_char) ) :
        char_track += 1
    return line[char_track:len(line)]

def scan_as_fraction(line):
    """ (str) -> Rational

    Scans all digits, including fractions, and returns as a
    Rational object. For example, '1/2' would return as a fraction value 1/2,
    '2' would return as fraction 2/1, and '2 1/2' would return as fraction 
    value 3/2.
    """
    # Init
    completed_scan = False # controls scan for initial digit and '/'
    value_as_frac = Rational(0,1) # Fraction value 0/1, Accumulates values when both integer and a fractional values are found

    while not completed_scan:
        # Init
        char_track = 0 # Increamented to scan past each character in line that is a digit char
        
        while char_track < len(line) and line[char_track].isdigit():
            char_track += 1

        numerator = int(line[0:char_track]) # range of chars scaned so far
        
        if char_track < len(line) and line[char_track] == '/':  # Scan for fractional notation
            char_track += 1
            start = char_track # Track begining of a new substring of digits to be scanned
            # Scan chars for denominator, until a non-digit is found
            while char_track < len(line) and line[char_track].isdigit():
                char_track += 1

            denominator = int(line[start : char_track])    
        
        else:
            # '/' fraction notation not found. E.g 2, is returned as 2/1
            denominator = 1
        # update fraction to current value. 
        value_as_frac += Rational(numerator, denominator) 

        if char_track == len(line):
            completed_scan = True   # Terminate scan
        else:
            # Next character to check for digit
            line = line[char_track:len(line)].strip()

            if not line[0].isdigit():
                completed_scan = True  # Terminate scan
                
    return value_as_frac

def convert_line(line, factor):
    """ (str, Rational) -> str

    If a line begins with a digit, returns line with the value multiplied
    by factor. Othewise, returns line unaltered
    (e.g., for a factor of 2, '1/4 cup' returns a '1/2 cup'.)
    """
    if line[0].isdigit():
        blank_char = ' '
        frac_meas = scan_as_fraction(line).__multiply__(factor)

        if frac_meas.get_denominator() == 1:
            frac_meas = frac_meas.get_numerator()
        conv_line = str(frac_meas) + blank_char + remove_measure(line)

    else:
        conv_line = line

    return conv_line

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

        # Convert recipe: line-by-line
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