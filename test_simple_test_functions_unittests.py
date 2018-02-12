#!/usr/bin/env python3
""" Tests for simple_test_functions.py """
import unittest
from simple_test_functions import *

class TestSimpleTestFunctions(unittest.TestCase):
    """ Test class for simple_test_functions.py """
    
    def setUp(self):
        print('Setting up...........')
    
    def tearDown(self):
        print('..........Tearing down')
    
    # test max_of_three_bad()
    def test_max_of_three_bad_1(self):
        self.assertEqual(max_of_three_bad(2, 3, 4), 4)
    
    def test_max_of_three_bad_2(self):
        self.assertEqual(max_of_three_bad(4, 3, 2), 4)

    def test_max_of_three_bad_3(self):
        self.assertEqual(max_of_three_bad(3, 2, 4), 4)
    
    # test max_of_three_good()
    def test_max_of_three_good_1(self):
        self.assertEqual(max_of_three_good(2,3,4), 4)

    def test_max_of_three_good_2(self):
        self.assertEqual(max_of_three_good(4,3,2), 4)

    def test_max_of_three_good_2(self):
        self.assertEqual(max_of_three_good(3,2,4), 4)

    # test maxmum()
    def test_maximum_1(self):
        self.assertEqual(maximum([2, 3, 4, 1]), 4)
        
    def test_maximum_2(self):
        self.assertEqual(maximum([4, 3, 2, 1]), 4)
    
    def test_maximum_3(self):
        self.assertEqual(maximum([-2, -3, 0, -21]), 0)

    # test sum_up()
    def test_sum_up_1(self):
        self.assertEqual(sum_up([0, 3, 4]), 7)
    
    def test_sum_up_2(self):
        self.assertEqual(sum_up([-3, 0, 5]), 2)
        
    # test ListManager - Some code that can throw an exception
    def test_list_manager_1(self):
        lstmgr = ListManager([1, 2, 3])
        self.assertEqual(lstmgr.get(2), 3)

    def test_list_manager_2(self):
        lstmgr = ListManager([1, 2, 3])
        self.assertEqual(lstmgr.get(3), 3)

    def test_list_manager_3(self):
        lstmgr = ListManager([1, 2, 3])
        self.assertEqual(lstmgr.get(0), 1)

    def test_list_manager_4(self):
        lstmgr = ListManager([1, 2, 3])
        self.assertEqual(lstmgr.get(0), 0) 

if __name__ == '__main__':
    unittest.main()
    
        


