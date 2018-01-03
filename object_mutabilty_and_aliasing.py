#!/usr/bin/env python3
""" Object Mutability and Aliasing
A play at Fraction variables and turtle objects
"""
from fractions import Fraction
from turtle import *

##################################################################
# Init: Assign some Fraction vars
f1 = Fraction(1, 2)
f2 = Fraction(1, 2)
f3 = f1

# Examine the fraction objects involved
print('f1 = {0} : Mem_loc = {1}'.format(f1, id(f1)))
print('f2 = {0} : Mem_loc = {1}'.format(f2, id(f2)))
print('f3 = {0} : Mem_loc = {1}'.format(f3, id(f3)))

# Examine the numerators and denominators separately
print('f1 numerator/denominator : {0}/{1}'.format(f1.numerator, f1.denominator))
print('f2 numerator/denominator : {0}/{1}'.format(f2.numerator, f3.denominator))
print('f3 numerator/denominator : {0}/{1}'.format(f3.numerator, f3.denominator))

# Compare the fractions
print('f1 == f2 : {}'.format(f1 == f2))
print('f1 == f3 : {}'.format(f1 == f3))
print('f1 is f2 : {}'.format(f1 is f2))
print('f1 is f3 : {}'.format(f1 is f3))

##################################################################

# Init turtle objects  part 1
t1 = Turtle() # Create & Assign turtle object
t2 = Turtle() # Createt & Assign turtle object

t1.pencolor('red')  # Set color
t2.pencolor('blue') # Set color

t2.left(90) # Turn & point turtle up (90 deg) (from default right)
t1.forward(100) # Move 100 units right
t2.forward(50)  # Move 50 units up

# Init turtle objects  part 2
t2 = t1 # Alias the turtles
t2.right(45) # Turn turtles right at 45 deg. angle
t2.forward(50) # Move turtles 50 units

done()