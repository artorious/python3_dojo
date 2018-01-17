#!/usr/bin/env python3
""" Reading comma-separated integer data from a text file. """

def read_file(file_name):
    """ (file) -> list
    
    Read th comma-separated intger data from the text file <file_name>
    Returns the data in a list
    """
    result = [] # Init
    with open(file_name, 'r') as file_obj:
        for line in file_obj:
            # Remove trailing whitespace, comma, newline
            result += [int(x.strip()) for x in line.rstrip(' ,\n').split(',')]
    return result

def main():
    lst = read_file('csv/monitor.data')
    print(lst)

if __name__ == '__main__':
    main()