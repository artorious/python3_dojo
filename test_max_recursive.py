#!/usr/bin/env python3

import unittest
from max_recursive import r_max

class Test(unittest.TestCase):

    def test_max_of_number_list(self):
        self.assertEqual(r_max([2, 9, 1, 13, 8, 6]), 13)

    def test_max_of_nested_number_list(self):
        self.assertEqual(r_max([2, [[100, 7], 90], [1, 13], 8, 6]), 100)

    def test_max_of_multiple_nested_number_list(self):
        self.assertEqual(r_max([[[13, 7], 90], 2, [1, 100], 8, 6]), 100)
    
    def test_max_of_mixed_list(self):
        self.assertEqual(r_max(["joe", 12, ["sam", "ben"]]), 'sam')

if __name__ == '__main__':
    unittest.main()