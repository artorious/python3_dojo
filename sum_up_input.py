#!/usr/bin/env python
'''a program that sums a series of (positive) integers entered by the user, 
excluding all numbers that are greater than 100
'''
# Init 
the_total = 0
sum_up = True

while sum_up == True:

    if the_total == 0:
        
        try:
            print('Enter 0 to EXIT')
            integer_for_addition = int(input('Enter First number to add:'))
            
            if integer_for_addition in range(1, 101):
                print(the_total, '+', integer_for_addition ,'=', the_total + integer_for_addition )
                the_total += integer_for_addition
            
            elif integer_for_addition == 0:
                print('Total:', the_total)
                sum_up = False
            
            else:
                print('Please provide an integer under 100')
                print('Current total:', the_total)
        
        except ValueError:
            print('Please enter an integer!!!!!')
            print('Current total:', the_total)
    
    else:
        
        try:
            print('Enter 0 to EXIT')
            integer_for_addition = int(input('Enter number to add: '))
        
            if integer_for_addition in range(1, 101):
                print(the_total, '+', integer_for_addition ,'=', the_total + integer_for_addition  )
                the_total += integer_for_addition
        
            elif integer_for_addition == 0:
                print('Total:', the_total)
                sum_up = False
        
            else:
                print('Please provide an integer under 100')
                print('Current total:', the_total)
        
        except ValueError:
            print('Please enter an integer!!!!!')
            print('Current total:', the_total)
        
    

