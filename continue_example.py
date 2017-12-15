#!/usr/bin/env python3

sum = 0
done = False

while not done:
    try:
        val = int(input('Enter positive integer (999 quits): '))

        if val < 0:
            print('Negative value {0} ignored'.format(val))
            continue    # Skip th rest of body for this iteration. Go back to top
        if val != 999:
            print('Tallying...... {0}'.format(val))
            sum += val
        else:
            done = (val == 999)
    except ValueError:
        print('Expected Integer')
print('Sum =', sum)
    
    