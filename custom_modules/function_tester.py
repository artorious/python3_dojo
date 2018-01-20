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
        pass
    
    def check(self, msg, expected, func, *args):
        """(FunctioTester, str, value, func, *args ) -> bool

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
        return 
    
    def report_results(self):
        """ Prints the testing statistics after performing all the tests. 
        
        Provides the error statistics for all the tests performed
        """
        pass
