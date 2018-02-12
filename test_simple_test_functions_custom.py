#!/usr/bin/env python3
""" Uses FunctionTester class to test a few simple functions """
from custom_modules.function_tester import FunctionTester
from simple_functions import *

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
    test_obj.check('sum_up test: #1:', 7, sum_up, [0, 3, 4])
    test_obj.check('sum_up test: #2:', 2, sum_up, [-3, 0, 5])

    test_obj.report_results()

if __name__ == '__main__':
    run_tests()