#!/usr/bin/env python3
"""An example of a function returning a local closure.

Uses the derivative function on;
    f (x) = 3x 2 + 5 
and compares its results with the known solution;
    f (x) = 6x.

NOTE:
Consider the calculation of a derivative.
In Calculus, the derivative of a function f at a is defined to be:

f'(a) = lim(h→0).(f (a + h) − f (a)) / h

The derivative of a function is itself a function; 
The process of computing a derivative is known as differentiation. 
The lim h→0 notation indicates that the answer becomes more precise as the 
value h gets closer to zero. 
Letting h be exactly zero would result in division by zero, which is undefined.
The trick is to make h as small as possible, keeping in mind that the 
computer’s floating-point values have limitations.

Based on the mathematical definition we can define a Python function that 
computes the derivative of another function;

    def derivative(f, h):
        return lambda x: (f(x + h) - f(x)) / h

Note that the derivative function returns a function—a lambda expression is a 
simple function definition. The function that derivative returns is a closure 
because it captures the function parameters f and h.

"""

def derivative(f, h):
    """(function, float) -> function
    Approximates the derivative of function <f> given an <h> value.
    The closer <h> is to zero, the better the estimate
    """
    return lambda x: (f(x + h) - f(x)) / h

def fun(x):
    """ (function) -> float
    <x> is the function to differentiate
    """
    return 3 * x ** 2 + 5

def ans(x):
    """(func) -> float
    <x> the known derivative to fun()
    """
    return 6 * x

h = 0.0000001 # Difference: Approx better as h -> 0
der = derivative(fun, h) # func rep an approx of the derivative of func()
x = 5.0 # Init

# Compare the compare derivative to the exact derivative derived symbolically
print('-' * 65)
print('{0:>50}  {1:^10}'.format('Approx.','Actual'))
print('{0:^10}  {1:^10}  {2:^15}  {3:^10}  {4:^10}'.format(
    'x', 'f(x)', 'h', 'f\'(x)', 'f\'(x)'))
print('-' * 65)

while x < 5.1:
    print('{0:^10.5f}  {1:^10.5f}  {2:^15.8f}  {3:^10.5f}  {4:^10.5f}'.format(
        x, fun(x), h, der(x), ans(x)))
    x += 0.01