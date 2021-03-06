#!/usr/bin/env python3
""" Sparse Text Program

Sparse data is data that lacks 'density'. 
Program removes all occurences of the letter 'e' from a provided text file.
"""
# Creation of modified file
def create_modified_file(input_file, output_file):
    """ (file, file) -> tuple 

    For text file <input_file>, creates a new version in file <output_file>
    in which all instances of the letter 'e' are removed

    Returns a tuple containing how many occurences of letter 'e' were removed,
    and the total character count of the file (num_total, num_removals)
    """
    # Init
    empty_str = ''
    num_total_chars = 0
    num_removals = 0

    for line in input_file:
        # Save original line length
        orig_line_length = len(line) - 1
        num_total_chars += orig_line_length # Track No. chars in file
        # Remove all occurrences of letter'e'
        modified_line = line.replace('e', empty_str).replace('E', empty_str)
        num_removals += orig_line_length - (len(modified_line) - 1) # Track No. chars removed
        # Simultaneously output line to screen and outpyr file
        print(modified_line.strip('\n'))
        output_file.write(modified_line)
    return (num_total_chars, num_removals)

def sparse_text():
    print('''
    This program will dispaly the contents of a provided text file
    with all occurences of the letter 'e' removed
    ''')
    # prompt user file for filename, open,read and assign to file object
    file_name = input('Enter file name (including file extension): ')
    input_file = open(file_name, 'r')
    new_file_name = 'e_removed_{0}'.format(file_name)
    output_file = open(new_file_name, 'w')
    # Create a file with all the letters e removed (Track changes)
    print()
    num_total_chars, num_removals = create_modified_file(input_file, output_file)
    # Close current input/output files
    input_file.close()
    output_file.close()
    # Dispaly percentage of charactes removed
    print()
    print('{0} occurences of the letter "e" removed.'.format(num_removals))
    print('Percentage of data lost: {0}%'.format(int((num_removals / num_total_chars) * 100)))
    print('Modified text in file: {0}'.format(new_file_name))

if __name__ == '__main__':
    sparse_text()




