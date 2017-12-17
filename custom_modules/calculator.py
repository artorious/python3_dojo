#!/usr/bin/env python3
"""A simple calculator"""
from get_integer_from_user import get_integer
from get_float_from_user import get_float
from get_positive_number_from_user import get_positive_num
from primality_check import is_prime
from gcd_program import gcd


def help_screen():
    """Displays Help Infomation. How the program works
    Accepts no parameters
    Returns nothing
    """
   
    print('-' * 60)
    print(format('| {0} |', '-^30').format(__doc__))
    print('-' * 60)
    print('Operation 1: Addition (x + y)')
    print('Operation 2: Subtraction (x - y)')
    print('Operation 3: Multiplication (x * y)')
    print('Operation 4: Division (x / y)')
    print('Operation 5: Exponentiation (x ** y)')
    print('Operation 6: Floor division (x // y)')
    print('Operation 7: Modulus division (x % y)')
    print('Operation 8: Greatest Common Divisor gcd(x,y)')
    print('Operation 9: Test for Primality. (True/False)')
    print('Operation 999: Print latest result ')
    print('Operation 0: Help (Displays this help screen)')
    print('Operation -1: Exit Calculator')    
    print('-' * 60)


def menu():
    """Displays Arithmetic  Menu Options.
    Accepts no parameter
    Returns an integer from user
    """
    help_screen()
    print(' [-1]Quit [0]Help [1]Add [2]Sub [3]Multiply [4]Exp [5]Divide [6]Mod')
    print('-' * 60)
    print('Select Operation [0 -5]: ')
    return get_integer()

def arithmetic_ops():
    """Runs a command loop that allows users to perform simple arithmetic"""
    # Init
    latest_result = 0.0
    terminate = False

    while  not terminate:
        op_selection = menu() # Get user's choice

        if op_selection not in (-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 999):
            print('INVALID OPTION')
            continue    # Go back to top of loop
        
        elif op_selection == -1: # Terminate Program
            terminate = True    
        
        elif op_selection == 0: # Help
            help_screen()
        
        elif op_selection == 1: # Add
            print(format(' ADDITITION (x+y) ', '|^60'))
            arg1 = get_float()
            arg2 = get_float()
            latest_result = add_two(arg1, arg2) # Store result
            print('{0:,} + {1:,} = {2:,}'.format(arg1, arg2, latest_result))

            print(format(' RESULT ', '|^60'))
        
        elif op_selection == 2: # Subtraction
            pass
        elif op_selection == 3: # Multiply
            pass
        elif op_selection == 4: # Division
            pass
        elif op_selection == 5: # Exponentiate
            pass
        elif op_selection == 6: # Truncation Div
            pass
        elif op_selection == 7: # Modulo div
            pass
        elif op_selection == 8: # gcd
            print(format(' GCD(x,y) ', '|^60'))
            arg1 = get_integer()
            arg2 = get_integer()
            latest_result = gcd(arg1, arg2) # Store result
            print('gcd({0:,},  {1:,}) = {2:,}'.format(arg1, arg2, latest_result))
            print(format(' RESULT ', '|^60'))

        elif op_selection == 9: # primality
            print(format(' PRIME? (True/False) ', '|^60'))
            arg1 = get_positive_num()
            latest_result =  is_prime(arg1)
            print('{0:,} is prime? - {1} '.format(arg1, latest_result))
            print(format(' RESULT ', '|^60'))
        
        else:   # print
            pass

def add_two(arg1, arg2):
    """(float, float) -> float
    Adds two numbers up
    Returns arg1 + arg2 
    """
    try:
        return arg1 + arg2
    except TypeError:
        return 'Unsupported operation: {0} + {1} '.format(arg1, repr(arg2))
    

                           

def multiply_two(arg1, arg2):
    """(float, float) -> float
    multiplies two numbers (arg1 * arg2)
    Returns the product  
    """
    try:
        return arg1 * arg2
    except TypeError:
        return 'Unsupported operation: {0} * {1} '.format(arg1, repr(arg2))

def subtract_two(arg1, arg2):
    """(float, float) -> float
    multiplies two numbers (arg1 - arg2)
    Returns the difference 
    """
    try:
        return arg1 - arg2
    except TypeError:
        return 'Unsupported operation: {0} - {1} '.format(arg1, repr(arg2))

def divide(arg1, arg2):
    """(float, float) -> float
    Divides two numbers (arg1 / arg2)
    Returns arg1 / arg2
    """
    try:
        return arg1 / arg2
    except TypeError:
        return 'Unsupported operation: {0} / {1} '.format(arg1, repr(arg2))

def floor_div(arg1, arg2):
    """(float, float) -> float
    Prerforms floor division on two numbers
    Returns  arg1 // arg2
    """
    try:
        return arg1 + arg2
    except TypeError:
        return 'Unsupported operation: {0} // {1} '.format(arg1, repr(arg2))

def exp_two(arg1, arg2):
    """(float, float) -> float
    Exponentiates two numbers (arg1 ** arg2)
    Returns the exponent
    """
    try:
        return arg1 ** arg2
    except TypeError:
        return 'Unsupported operation: {0} ** {1} '.format(arg1, repr(arg2))

if __name__ == '__main__':
    arithmetic_ops()