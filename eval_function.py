#!/usr/bin/env python3
'''eval() - Attempt to evaluate a string the same way that the interactive
shell does.'''

print(__doc__)

terminate = False
while not terminate:
    print('Enter Value to evaluate [leave blank to exit]:')
    value = input('Entry: ')
    if value == '':
        terminate = True
    else:
        try:
            value =  eval(value)
            print(format(' Evaluating ', '*^120'))
            print('Entry: {0}  Type: {1}'.format(value, type(value)))
            print(format(' Try Again', '.^80' ))

        except NameError:
            print('Error {0} not defined'.format(value))
            print(format(' Try Again', '.^80' ))
            
    
    