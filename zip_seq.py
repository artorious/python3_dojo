#!/usr/bin/env python3
""" A play on Python lists and tuples """

def perfect_sq_seq_gen(num):
     """ (int) -> generator
     
     Generates the first <num> perfect squares,
     starting with zero: 0, 1, 4, 9, 16, .... (num - 1)^2
     """
     for i in range(num):
        yield i ** 2

def main():    
    """ A play on Python lists and tuples """
    
    print('''
    Construct a sequence of tuples with their first elements derived from a 
    list and their second elements obtained from a generator.
    ''')
    print('Tuple sequence:\v', end='')
     # NOTE: generator sequence is shorter than the list
    [print(_, end=' ') for _ in zip(list(range(10)), perfect_sq_seq_gen(5))]
    print()
    
    print('''
    Make a new list from two existing lists. Where:
    
    The 1st element in the new list is the sum of the first elements from 
    the two original lists. Similarly, the 2nd element in the new list is the
    sum of the second elements in the two original lists, and so forth. 
    ''')
    lst1, lst2  = list(range(1, 6)), list(range(10, 15))
    print('Working lists:\v{0} and {1}'.format(lst1, lst2))
    print('List of sums:\v{0}'.format([x+y for (x, y) in zip(lst1, lst2)]))
    # for (x, y) in zip(lst1, lst2):
    #     print(x + y, end=' ')

if __name__ == '__main__':
    main()
   

