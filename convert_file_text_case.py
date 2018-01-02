#!/usr/bin/env python3
""" A Simple File Processing Program.
Combines Python’s string objects and file objects to create a file processing 
program. 
Features:
    * open one file, 
    * read its contents, 
    * and write a modified form of its contents to a second file. 
    
Module provides a simple utility function, capitalize, that capitalizes 
the text within a file.
"""

def capitalize(filename):
    """
    Creates a new file with the prefix 'upper_' added to the name of the 
    original file <filename>.
    All the alphabetic characters in the new are capitalized. 
    This function does not disturb the contents of the original file. 
    """
    with open(filename, 'r') as input_file:
        with open('upper_{0}'.format(filename), 'w') as output_file:
            for line in input_file:
                line = line.strip().upper()
                print(line, file=output_file)


if __name__ == '__main__':
    capitalize('declaration.txt')

