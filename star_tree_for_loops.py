#!/usr/bin/env python3
'''Prints a triangular tree with it's height provided by the user.
The tree's height and width varies based on user input
Example: 

Height = 6

                    *
                   ***
                  *****
                 *******
                *********
               ***********
'''
from custom_modules.get_positive_number_from_user import get_positive_num


def draw_tree(height):
    """ Draws a tree of a given <height>
    <height> being an integer
    """
    for row in range(height): # Draws one row for every unit of height
    
        # Print Leading spaces; 
            # as row gets bigger, no. of leading spaces gets smaller
        for count in range(height - row):
            print(end=' ')
        
        # Print out stars, twice the current row plus one:
        #   1. No. of stars on the left side of tree = current row value
        #   2. Exacltly one star in the center of the tree
        #   3. No. of stars on the right side of tree = current row value

        for count in range((2 * row) + 1): 
            print(end='*')

        print() # Move to the next line
        



    

if __name__ == '__main__':
    print(__doc__) # Program Greeting
    draw_tree(int(get_positive_num())) # Draw a tree with height from user 


 
###---- Printing Tree ----###

