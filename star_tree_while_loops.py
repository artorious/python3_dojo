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

print(__doc__) # Program Greeting
# init
row= 0  # Draw one row for every unit of height
height = int(get_positive_num()) # Get tree height (positive integer) from user

###---- Printing Tree ----###

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
