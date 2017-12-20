#!/usr/bin/env python3
"""A simple calculator"""
from get_integer_from_user import get_integer
from get_float_from_user import get_float
from get_positive_number_from_user import get_positive_num
from primality_check import is_prime
from gcd_program import gcd_recursive
from get_integer_in_range import get_int_in_range

# init global variables
global latest_result, arg1, arg2, operator

latest_result = 0.0
arg1 = 0.0
arg2 = 0.0
operator = 'None'

def help_screen():
    """Displays Help Infomation. How the program works
    Accepts no parameters
    Returns nothing
    """
    print('-' * 60)
    print(format('| {0} |', '-^44').format(__doc__))
    print('-' * 60)
    print(format(' Operation [1]: Addition (x + y) ', '_^60' ))
    print(format(' Operation [2]: Subtraction (x - y) ', '_^60'))
    print(format(' Operation [3]: Multiplication (x * y) ', '_^60'))
    print(format(' Operation [4]: Division (x / y) ', '_^60'))
    print(format(' Operation [5]: Exponentiation (x ** y) ', '_^60'))
    print(format(' Operation [6]: Floor division (x // y) ', '_^60'))
    print(format(' Operation [7]: Modulus division (x % y) ', '_^60'))
    print(format(' Operation [8]: Greatest Common Divisor gcd(x,y) ', '_^60'))
    print(format(' Operation [9]: Test for Primality. (True/False) ', '_^60'))
    print(format(' Operation [10]: Print latest result ', '_^60'))
    print(format(' Operation [0]: Help (Displays this help screen) ', '_^60'))
    print(format(' Operation [-1]: Exit Calculator', '_^60')) 
    print('-' * 60)

def menu():
    """Displays Arithmetic  Menu Options.
    Accepts no parameter
    Returns an integer from user
    """
    help_screen()
    print(format(' Enter Command to Porceed ', '|^60'))
    print(format(' [-1]Quit [0]Help ', '|^60'))
    print(format(' [1]Add [2]Sub [3]Multiply [4]Divide', '|^60'))
    print(format(' [5]Exp [6]Floor [7]Mod [8]gcd [9]pimality ', '|^60' ))
    print('-' * 60)
    print('Select Operation [-1 - 10]: ')
    return get_int_in_range(-1, 10)

def arithmetic_ops():
    """Runs a command loop that allows users to perform simple arithmetic"""
    # Init
    latest_result = 0.0
    terminate = False

    while  not terminate:
        op_selection = menu() # Get user's choice
        
        if op_selection == -1: # Terminate Program
            terminate = True    
        
        elif op_selection == 0: # Help
            help_screen()
        
        elif op_selection == 1: # Add
            print(format(' ADDITITION (x+y) ', '|^60'))
            # Init
            # global arg1, arg2, latest_result, operator
            arg1 = get_float() 
            arg2 = get_float()
            operator = '+'
            print()
            latest_result = add_two(arg1, arg2) # Store latest result
            print('{0:,} + {1:,} = {2:,}'.format(arg1, arg2, latest_result)) # Display operation
            print(format(' RESULT ', '|^60'))
        
        elif op_selection == 2: # Subtraction
            print(format(' SUBTRACTION (x-y) ', '|^60'))
            # Init
            # global arg1, arg2, latest_result, operator
            arg1 = get_float() 
            arg2 = get_float()
            operator = '-'
            print()
            latest_result = subtract_two(arg1, arg2) # Store latest result
            print('{0:,} - {1:,} = {2:,}'.format(arg1, arg2, latest_result)) # Display operation
            print(format(' RESULT ', '|^60'))

        elif op_selection == 3: # Multiply
            print(format(' MULTIPLY (x*y) ', '|^60'))
            # Init
            # global arg1, arg2, latest_result, operator
            arg1 = get_float() 
            arg2 = get_float()
            operator = '*'
            print()
            latest_result = multiply_two(arg1, arg2) # Store latest result
            print('{0:,} * {1:,} = {2:,}'.format(arg1, arg2, latest_result)) # Display operation
            print(format(' RESULT ', '|^60'))

        elif op_selection == 4: # Division
            print(format(' INTEGER DIVISION (x/y) ', '|^60'))
            # Init
            # global arg1, arg2, latest_result, operator
            arg1 = get_float() 
            arg2 = get_float()
            operator = '/'
            print()
            latest_result = divide(arg1, arg2) # Store latest result
            print('{0} / {1} = {2}'.format(arg1, arg2, latest_result)) # Display operation
            print(format(' RESULT ', '|^60'))

        elif op_selection == 5: # Exponentiate
            print(format(' EXPONENTION (x**y) ', '|^60'))
            # Init
            # global arg1, arg2, latest_result, operator
            arg1 = get_float() 
            arg2 = get_float()
            operator = '**'
            print()
            latest_result = exp_two(arg1, arg2) # Store latest result
            print('{0:,} ** {1:,} = {2:,}'.format(arg1, arg2, latest_result)) # Display operation
            print(format(' RESULT ', '|^60'))

        elif op_selection == 6: # Truncation Div
            print(format(' FLOOR DIVISION (x//y) ', '|^60'))
            # Init
            # global arg1, arg2, latest_result, operator
            arg1 = get_float() 
            arg2 = get_float()
            operator = '//'
            print()
            latest_result = floor_div(arg1, arg2) # Store latest result
            print('{0:,} // {1:,} = {2:,}'.format(arg1, arg2, latest_result)) # Display operation
            print(format(' RESULT ', '|^60'))

        elif op_selection == 7: # Modulo div
            print(format(' MODULO DIVISION (x%y) ', '|^60'))
            # Init
            # global arg1, arg2, latest_result, operator
            arg1 = get_float() 
            arg2 = get_float()
            operator = '%'
            print()
            latest_result = modulo_div(arg1, arg2) # Store latest result
            print('{0} % {1} = {2}'.format(arg1, arg2, latest_result)) # Display operation
            print(format(' RESULT ', '|^60'))

        elif op_selection == 8: # gcd
            print(format(' GCD(x,y) ', '|^60'))
            # Init
            # global arg1, arg2, latest_result, operator
            arg1 = get_integer()
            arg2 = get_integer()
            operator = 'gcd'
            latest_result = gcd_recursive(arg1, arg2) # Store result
            print('gcd({0:,},  {1:,}) = {2:,}'.format(arg1, arg2, latest_result))
            print(format(' RESULT ', '|^60'))

        elif op_selection == 9: # primality
            print(format(' PRIME? (True/False) ', '|^60'))
            # Init
            # global arg1, latest_result, operator
            arg1 = int(get_positive_num())
            operator = 'prime'
            print()
            latest_result =  is_prime(arg1)
            print('{0:,} is prime? - {1} '.format(arg1, latest_result))
            print(format(' RESULT ', '|^60'))
        
        else:   # print
            try:
                if operator in ['+', '-', '*', '**', '%', '//', '/']:
                    print('latest_operation: {0} {1} {2} = {3}'.format(arg1, operator, arg2, latest_result) )
                elif operator == 'gcd':
                    print('latest_operation: gcd({0}, {1})  = {2}'.format(arg1, arg2, latest_result) )
                elif operator == 'prime':
                    print('latest_operation: is_prime({0})  = {1}'.format(arg1, latest_result) )
            except UnboundLocalError as no_history:
                print(no_history)
            except Exception as other_error:
                print(other_error)
            
            

def add_two(arg1, arg2):
    """(float, float) -> float
    Adds two numbers up
    Returns arg1 + arg2 
    """
    try:
        return arg1 + arg2
    except TypeError:
        return 'Unsupported operation: {0} + {1} '.format(type(arg1), type(arg2))

def multiply_two(arg1, arg2):
    """(float, float) -> float
    multiplies two numbers (arg1 * arg2)
    Returns the product  
    """
    try:
        return arg1 * arg2
    except TypeError:
        return 'Unsupported operation: {0} * {1} '.format(type(arg1), type(arg2))

def subtract_two(arg1, arg2):
    """(float, float) -> float
    multiplies two numbers (arg1 - arg2)
    Returns the difference 
    """
    try:
        return arg1 - arg2
    except TypeError:
        return 'Unsupported operation: {0} - {1} '.format(type(arg1), type(arg2))

def divide(arg1, arg2):
    """(float, float) -> float
    Divides two numbers (arg1 / arg2)
    Returns arg1 / arg2
    """
    try:
        return arg1 / arg2
    except TypeError:
        return 'Unsupported operation: {0} / {1} '.format(type(arg1), type(arg2))
    except ZeroDivisionError as zero_error:
        return 'Unsupported operation: {0} / {1} -> {2}'.format(arg1, arg2, zero_error)
    except Exception as other_error:
        return 'Oops... {0}'.format(other_error)

def floor_div(arg1, arg2):
    """(float, float) -> float
    Prerforms floor division on two numbers
    Returns  arg1 // arg2
    """
    try:
        return arg1 + arg2
    except TypeError:
        return 'Unsupported operation: {0} // {1} '.format(type(arg1), type(arg2))

def exp_two(arg1, arg2):
    """(float, float) -> float
    Exponentiates two numbers (arg1 ** arg2)
    Returns the exponent
    """
    try:
        return arg1 ** arg2
    except TypeError:
        return 'Unsupported operation: {0} ** {1} '.format(type(arg1), type(arg2))

def modulo_div(arg1, arg2):
    """(float, float) -> float
    Modulo division of  two numbers
    Returns  (arg1 % arg2)
    """
    try:
        return arg1 % arg2
    except TypeError:
        return 'Unsupported operation: {0} % {1} '.format(type(arg1), type(arg2))
    except ZeroDivisionError as zero_error:
        return 'Unsupported operation: {0} % {1} -> {2}'.format(arg1, arg2, zero_error)
    except Exception as other_error:
        return 'Oops... {0}'.format(other_error)

if __name__ == '__main__':
    arithmetic_ops()