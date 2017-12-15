#!/usr/bin/env python3
'''Loop to check for something

Uses while loop to check, breaks as soon as it's found, runs the else 
if the while loop completed but the object was not found.  
'''
# Init
numbers = [1,3,5,7,9]
position = 0

while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print('Found even number {0:,}'.format(number))
        break
    position += 1
else: # Break not called
    print('No even numbers found')

# Init
cheeses = []

for cheese in cheeses:
    print('This shop has some lovely', cheese)
    break
else: # no break means no cheese
    print('This is NOT much of a cheese shop is it?')