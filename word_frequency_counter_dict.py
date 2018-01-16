#!/usr/bin/env python3
""" Words Frequency Counter Program

Use a dictionary to count occurrences of each word in a text file.
Reads the content of a text file containing words, 
and prints a count of each word. 

NOTE:
To simplify things, the text file contains only words with no punctuation. 
The user supplies the file name on the command line when launching the program 
"""

import sys # For sys.argv global command line arguments list


def main():
    """ Counts the words in a text file. """
    if len(sys.argv) < 2:   # Did the user not supply a file name?
        print('Usage: python3 word_frequency_counter_dict.py <filename>')
        print('where <filename> is the name of a text file.')
    
    else:                                           # Filename provided
        file_name = sys.argv[1]
        counters = {}                               # Init counting dict
        
        with open(file_name, 'r') as txt_file_obj:  # Open file for reading
            txt_file_content = txt_file_obj.read()  # Read content of whole file
            words = txt_file_content.split()        # Make list of individual words

        for word in words:
            word = word.upper()   # Make All-caps
            
            if word not in counters:
                counters[word] = 1 # 1st occurence of a word
            else:
                counters[word] += 1 # Incr existing count

        # Report
        for word, count in counters.items():
            print('{0} : {1}'.format(word, count))

if __name__ == '__main__':
    main()
