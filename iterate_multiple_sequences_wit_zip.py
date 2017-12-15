#!/usr/bin/env python3
'''Iterate over multiple sequences in parallel using zip() function
NOET:
    zip() stops when the shortest sequence is done
'''
# Init
days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']

for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts) :
    print(day, ': drink', drink, '- eat', fruit, '- enjoy', dessert)
