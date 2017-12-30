#!/usr/bin/env python3
""" 
Use of global variables to allow a function to remember some information
"""

count = 0

def remember():
    """
    Use global variable to keep track of the number of times it has been invoked
    """
    global count
    count += 1  # Count invocation
    print('Remember me? call #{0}'.format(count))

if __name__ == '__main__':
    # for calls in range(10):
    #     print('index:{0}'.format(calls), end=' - ')
    #     remember()
    
    while count < 10:
        remember()
    

