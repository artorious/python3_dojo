#!/usr/bin/env python3
'''A Rudimentary Python interpreter
exec() - Accept a string parameter that consists of a Python source 
statement. Itrerprate the statement and execute it.'''

from sys import exit
print(__doc__)
while True:
    print('')
    exec(input('[exit(0) to Quit] ~ >>> '))