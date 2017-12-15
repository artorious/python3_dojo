#!/usr/bin/env python
'''Calculates and dispalys the average of five 
non-negative numbers provided by user'''
# Init
count,total = 0,0
print('NOTE: Please enter five non-negative numbers when prompted')

while count < 5:
    try:
        val = float(input('Enter number: '))
        if val < 0:
            print('Negative number {0} IGNORED.'.format(val))
            continue # Back to top
        count += 1
        total += val

    except ValueError:
        print('Expected Integer of Floating-point Number')
    
else:
    print('Average =', total/count)
