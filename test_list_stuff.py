#!/usr/bin/env python3
""" Uses FunctionTester class to test a few simple functions """

from custom_modules.function_tester import FunctionTester

def max_of_three_bad(x, y, z):
    """ (int, int, int) -> int

    Attempts to determine and return the maximum of three
    numeric values
    """
    result = x
    if y > result:
        result = y
    elif z > result:
        result = z
    return result

def max_of_three_good(x, y, z):
    """ (int, int, int) -> int

    Computes and returns the maximum of three numeric values
    """
    result = x
    if y > result:
        result = y
    if z > result:
        result = z
    return result

def sum(lst):
    """ (list) -> int

    Attempts to compute and return the sum of all the elements in a list
    of integers
    """
    total = 0
    for i in range(1, len(lst)):
        total  += lst[i]
    return total

def maximum(lst):
    """(list) -> int

    Computes the maximum element in a list of integers
    """
    return 0 # Not implemented

def run_tests():
    """ Sample Test cases """
    test_obj = FunctionTester()

    # test max_of_three_bad()
    test_obj.check('max_of_three_bad test: #1:', 4, max_of_three_bad, 2,3,4)
    test_obj.check('max_of_three_bad test: #2:', 4, max_of_three_bad, 4,3,2)
    test_obj.check('max_of_three_bad test: #3:', 4, max_of_three_bad, 3,2,4)

    # test max_of_three_good()
    test_obj.check('max_of_three_good test: #1:', 4, max_of_three_good, 2,3,4)
    test_obj.check('max_of_three_good test: #2:', 4, max_of_three_good, 4,3,2)
    test_obj.check('max_of_three_good test: #3:', 4, max_of_three_good, 3,2,4)

    # test maxmum()
    test_obj.check('maximum test: #1:', 4, maximum, [2, 3, 4, 1])
    test_obj.check('maximum test: #2:', 4, maximum, [4, 3, 2, 1])
    test_obj.check('maximum test: #3:', 0, maximum, [-2, -3, 0, -21])

    # test sum
    test_obj.check('sum test: #1:', 7, sum, [0, 3, 4])
    test_obj.check('sum test: #2:', 2, sum, [-3, 0, 5])

    test_obj.report_results()

if __name__ == '__main__':
    run_tests()
