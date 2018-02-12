#!/usr/bin/env python3
""" Automated Testing - a class of simple test objects

Defines the structure of a rudimentary object used to test functions
"""

class FunctionTester(object):
    """ Provides support for testing simple Python functions 

    Simple test objects that enable a client to exercise one or more 
    functions to see if they produce expected results. 
    
    A test object keeps track of the number of tests performed and the number 
    of failures.
    """

    def __init__(self):
        """ (FunctionTester) -> int, int
        
        Establishes the __total_count and __error_count instance variables to
        handle the accounting (counts). Creates a FunctionTester object,
        Resets the counts to zero
        """
        self.__error_count = self.__total_count = 0
        print('+---------------------------------')
        print('|\t Testing                       ')
        print('+---------------------------------')

    
    def check(self, msg, expected, func, *args):
        """(FunctionTester, str, value, func, *args ) -> bool

        <msg> - a human-readable message to uniquely identify the 
        test case (so the tester can determine which test failed), 
        <expected> - return value of a correctly implemented function,
        <func> - the function to test
        <*args> - parameters to pass to the function, if any.

        method calls the function it receives with the specified parameters 
        and compares the actual result to the expected result. 
         
        Provides immediate printed feedback about the test's successs of 
        failiure and adjusts error count accordingly (number of failed tests)
        
        Returns True if the function passed the test;
        otherwise, returns False
        """
        result = True # Test passed unless we determine otherwise
        print('\t', msg, '\t', end=' ')
        self.__total_count += 1         # Count this test
        
        try:
            actual = func(*args)        # Apply function to arguments
            
            if expected == actual:
                print('OK')
            
            else:
                self.__error_count += 1  # Count this failed test
                print('*** Failed!\n\tExpected: {0}\n\tActual: {1}'.format(
                    expected, actual))
                result = False # Test failed

        except Exception as eerr:
            self.__error_count += 1 # Count this failed test
            print('******* Exception: {0}'.format(eerr))
            result = False  # Test Failed
        
        return result # Notify client of tst result
    
    def report_results(self):
        """ Prints the testing statistics after performing all the tests. 
        
        Provides the error statistics for all the tests performed
        """
        print('+--------------------------------')
        print('| {0} Tests run'.format(self.__total_count))
        print('| {0} Passed'.format(self.__total_count - self.__error_count))
        print('| {0} Failed'.format(self.__error_count))
        print('+--------------------------------')