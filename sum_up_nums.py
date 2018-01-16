#!/usr/bin/env python3
""" A play on Arbitrary Argument Lists """

def sum_up_nums(*nums):
    """(int or float) -> int or float

    Adds up as many numbers(separate arguments) as the caller can supply. 
    Returns the sum of <*nums> 
    """
    cntr = 0 # Init sum zero
    for num in nums:
        cntr += num
    return cntr

def main():
    print(sum_up_nums(4))
    print(sum_up_nums(3, 4))
    print(sum_up_nums(3, 4, 5.6))
    print(sum_up_nums(3, 3, 3, 3, 4, 1, 9, 44, -2, 8, 8))

if __name__ == '__main__':
    main()
