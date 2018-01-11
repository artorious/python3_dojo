#!/usr/bin/env python3
"""Word Frequency Count Program

Prompts the user for the name of text file to open and a word to search for,
and displays th number of times that the word occurs within the file.
"""

def get_file():
    """() -> tuple

    Prompts the user for the file name to open for reading.
    Returns the file name and the associated input file object
    for reading as a tuple of the form (file_name, input_file) 
    """
    input_file_opened = False
    while not input_file_opened:
        try:
            file_name = input('Enter input file path(name with extension):\n>>> ')
            input_file = open(file_name, 'r')
            input_file_opened = True
        except IOError as ioerr:
            print('Input file not found - Please re-enter path:\n>>> ')
    return (file_name, input_file) 

def count_words(input_file, search_word):
    """(file obj, str) -> int
    Returns the number of occurrences of <search_word> in the 
    provide <input_file> object.
    """
    # Init
    space = ' '
    num_occurrences = 0
    word_delimiters = (space, ',',';',':','.',',','\n','"',"'",'(',')')
    search_word_len = len(search_word)

    for line in input_file:
        end_of_line = False
        line = line.lower() # Convert line read to lowercase
        while not end_of_line:
            try:
                index = line.index(search_word) # Search for word in current line
                # If word at start of line is followed by a delimiter
                if index == 0 and line[search_word_len] in word_delimiters:
                    found_search_word = True
                # If search word within line, check chars before/after
                elif line[index - 1] in word_delimiters and line[index + search_word] in word_delimiters:
                    found_search_word = True
                # If found within other letters, then NOT search word
                else:
                    found_search_word = False
                # If search word found, increament count
                if found_search_word:
                    num_occurrences += 1
                # Reset line to rest of line following search word
                line = line[index + search_word_len: len(line)]

            except ValueError:
                end_of_line = True

    return num_occurrences

def main():
    """ Word Frequency Count Program """
    
    print('''
    This program will display the number of occurrences
    of a specified word within a given text file.''')   # Prog Greeting
    file_name, input_file = get_file()                  # Open file to search
    search_word = input('Enter word to search: ')       # Get search word
    search_word = search_word.lower()                   # convert to lowercase
    num_occurrences = count_words(input_file, search_word)  # Count all occurrences of search word
    # Display Results
    if num_occurrences == 0:
        print("NO occurrences of the word '{0}' in file: {1}".format(
            search_word, file_name))
    else:
        print("The word '{0}' occurs {1} times in the file: {1}".format(
            search_word, file_name))
        


if __name__ == '__main__':
    main()



#### ---Main


# Prompt user for word to search for, assign to var search_word