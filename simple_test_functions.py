#!/usr/bin/env python3
""" A few simple functions """

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

def sum_up(lst):
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


class ListManager(object):
    def __init__(self, lst):
        super().__init__()
        self.lst = lst

    def get(self, idx):
        """
        Return list item at index idx
        """
        return self.lst[idx] # Subject to range exception
    