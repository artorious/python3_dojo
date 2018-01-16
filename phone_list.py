#/usr/bin/env python3
""" A simple telephone contact list. 

Uses Python dictionary to implement a simple telephone contact database with 
a rudimentary command line interface.

The contact list associates a name with a telephone number.
A person or company’s name is a unique identifier for that contact. 
The name is a key to that contact.
"""

contacts = {} # Init global telephone contact list
running = True

while running:
    command = input('A)dd D)elete L)ook-up Q)uit: ')
    
    if command == 'A' or command == 'a':
        name = input('Enter new name: ')
        print('Enter phone number for {0}: '.format(name))
        number = input('>>> ')
        contacts[name] = number
    
    elif command == 'D' or command == 'd':
        name = input('Enter name to DELETE: ')
        del contacts[name]

    elif command == 'L' or command == 'l':
        name = input('Enter name to Look-up: ')
        print('Name: {0} - Tel: {1}'.format(name, contacts[name]))
    
    elif command == 'Q' or command == 'q':
        running = False
    
    elif command == 'dump':
        print(contacts)
    
    else:
        print('Oops... {0} - NOT a valid command....Try again')
        
