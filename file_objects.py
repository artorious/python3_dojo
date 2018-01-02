#!/usr/bin/env python3
""" File Objects
Use Python's file class to store/retrieve data to/from a text file

Allows the user to enter numbers from the keyboard and save them to a file
Also allows retrieval of the data prevously saved to file
User can specify the name of the file and thus works with multiple files
"""

def load_data(filename):
    """ (file) -> int
    Print the elements stored in the text file <filename>
    """

    with open(filename) as f_obj: # Open file to read & assign file object
        for line in f_obj:  # Read each line as text
            print(int(line))   # Convert to int & display

def store_data(filename):
    """
    Store data to <filename> text file
    """
    with open(filename, 'w') as f_obj:  
        number = 0
        while number != 999:
            
            number = int(input('Pls enter a number (999 quits): '))
            if number != 999:
                f_obj.write(str(number) + '\n')
            else:
                break # Exit loop

def work_with_file():
    """
    Interactive function that allows the user to create or
    consume files of numbers
    """
    done = False    # Init

    while not done:
        cmd = input('S)ave L)oad Q)uit: ')
        if cmd.upper() == 'S':
            store_data(input('Enter file name: '))
        elif cmd.upper() == 'L':
            load_data(input('Enter file name: '))
        elif cmd.upper() == 'Q':
            done = True

if __name__ == '__main__':
    work_with_file()