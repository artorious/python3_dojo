#!/usr/bin/env python3
"""Demonstration of a simple closure
An example of a closure transporting a captured variable into a 
function call. 

NOTE:
    A closure is a function that can capture the context of its surrounding 
    environment.
"""

def evaluate(function, param1, param2):
    """
    Returns <function>, called with <param1> and <param2>
    """
    return function(param1, param2)
    

if __name__ == '__main__':
    from custom_modules.get_integer_from_user import get_integer

    print('Guess my age or DOB : ', end='')
    sample = get_integer() # Var : Only captured by lambda expr, not evaluate()
    # Call evaluate() with a function (lambda expression) and two integer values
    print(evaluate(
        lambda x, y: True if x == sample or y == sample else False, 30, 1987
        ))
