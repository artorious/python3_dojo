#!/usr/bin/env python3
""" Use a Python dictionary to group the words in a text file according to
their length (number of letters)
"""

import sys      # For argv global command line arguments list

def main():
    """ Group the words by length in a text file """
    if len(sys.argv) < 2: # Did the user not supply a file name?
        print('Usage: python3 group_words_from_file.py <file_name>')
        print('\tWhere <file_name> is the name of the text file.')
    
    else:   # User provided file name
        file_name = sys.argv[1]
        word_groups = {}     # Init grouping dict

        with open(file_name, 'r') as file_obj:  # Open file for reading
            file_content = file_obj.read() # Read in content of the entire file
            words = [word.upper() for word in file_content.split()]  # Make list of individual words (All-caps)
            
            for word in words:
                word_len = len(word)
                if word_len in word_groups:
                    if word not in word_groups[word_len]:    # Avoid duplication
                        word_groups[word_len] += [word]       # Add th word to its group
                else:
                    word_groups[word_len] = [word]           # Add the word to a new group
            
            # Display 
            for word_len, word_group in word_groups.items():
                print('{0} : {1}'.format(word_len, word_group))

if __name__ == '__main__':
    main()