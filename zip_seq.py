#!/usr/bin/env python3
""" A play on Python lists and tuples 
 
 Construct a sequence of tuples with their first elements derived from a list
 and their second elements obtained from a generator.
 """
 # NOTE: Zip a list with a generator sequence that is shorter than the list

def sequence_generator(num):
     """ (int) -> generator
     
     Generates the first <num> perfect squares,
     starting with zero: 0, 1, 4, 9, 16, .... (num - 1)^2
     """
     for i in range(num):
        yield i ** 2

[print(p, end=' ') for p in zip(list(range(10)), sequence_generator(5))]   

