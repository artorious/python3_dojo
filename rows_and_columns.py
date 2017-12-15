#!/usr/bin/env python3
'''Rows and Columns.

A program that displays the integer values 1–100, 
ten numbers per row, with the columns aligned as shown below,
 
     1  2  3  4  5  6  7  8  9 10
    11 12 13 14 15 16 17 18 19 20
    21 22 23 24 25 26 27 28 29 30
    .
    .
    91 92 93 94 95 96 97 98 99 100
'''

# init
cntr = 1


while cntr <= 100:
    for column_count in range(10):
        if cntr < 10:
            print('', cntr, end=' ')
            cntr += 1
        else:
            print(cntr, end=' ')
            cntr += 1
    print()
   
