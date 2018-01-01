#!/usr/bin/env python3
""" Local function mimicing a generator """

def create_counter(n):
    """ (int) -> function
    Creates a counting function that counts up to <n> 
    Returns it's own local function counter()
    """
    count = 0 # Init
    
    def counter():
        """ 
        Increaments the outer var unless it has reached its's limit 
        NOTE:
            'Remembers' the value of it's enclosing function's local var count
            thue, it represents a closure
        """

        nonlocal count
        if count < n:
            count += 1
        
        return count 

    return counter


if __name__ == '__main__':
    cntr = create_counter(4)
    print(cntr())
    print(cntr())
    print(cntr())
    print(cntr())
    print(cntr())
    print(cntr())
    print(cntr())
    print(cntr())
    print(cntr())