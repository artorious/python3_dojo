#!/usr/bin/env python
'''Calculates and dispalys the average of numbers provided by user'''
# Init
count,total = 0,0
done = False

while not done:
    val = input('Enter integer value or [Q/q]uit to Calculate average: ')
    try:
        if isinstance(int(val), int):
            val = int(val)
            count += 1
            total += val
    except ValueError:
        if val in ['Q','q', 'quit', 'Quit', 'QUIT']:
            if count and total:
                print('average =', total/count)
                break # Exit Loop
            else: # Handle division by Zero when Numerator or Denomenator are 0
                print(0)
                done = True # Exit Loop
        else:
            print('Invalid Value "{0}". Expected Integers'.format(val))
            continue # Go back to top
        


