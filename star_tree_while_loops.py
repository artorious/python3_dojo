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
    row = 0 # Init first row, from the top, to draw
    while row < height: # Draws one row of the tree each time its's body executes
    
        # Print Leading spaces; 
            # as row gets bigger, no. of leading spaces gets smaller
        count = 0
        while count < height - row:
            print(end=' ')
            count += 1
        
        # Print out stars, twice the current row plus one:
        #   1. No. of stars on the left side of tree = current row value
        #   2. Exacltly one star in the center of the tree
        #   3. No. of stars on the right side of tree = current row value

        count = 0
        while count < ((2 * row) + 1): 
            print(end='*')
            count += 1
        print() # Move to the next line
        row += 1 # Next row


    

if __name__ == '__main__':
    print(__doc__) # Program Greeting
    draw_tree(int(get_positive_num()))  # Draw a tree with height from user


