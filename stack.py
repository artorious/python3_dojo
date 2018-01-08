#!/usr/bin/env python3
""" A simple programmer-defined stack module - Implemented as a list

Module contains a set of functions that implement stack behavior

Stacks are used to temporarily store and retrieve data.
The last item placed on the stack is the first to be retrieved. 
LIFO - Last In First Out. 
A stack can be viewed as a list that can be accessed only at one end.
"""

def get_stack():
    """ () -> list 
    
    Creates and returns an empty stack 
    """
    return []

def is_empty(the_stack):
    """ (list) -> bool
    
    Returns True if <the_stack> empty, otherwise returns False. 
    """
    if the_stack == []:
        return True
    else:
        return False

def top(the_stack):
    """ 
    Returns value of the top item in <the_stack>, if stack not empty. 
    Otherwise returns None 
    """

    if is_empty(the_stack):
        return None
    else:
        return the_stack[len(the_stack) - 1]

def push(the_stack, item):
    """ Pushes item on the top of stack """
    the_stack.append(item)

def pop(the_stack):
    """ Returns top of stack if stack not empty. Otherwise, returns None """
    if is_empty(the_stack):
        return None
    else:
        item = the_stack[len(the_stack) - 1]
        del the_stack[len(the_stack) - 1]
        return item




def main():
    """ Display and push values 1 through 4 on the stack 
    
    Displays the numbers popped off the stack, retrieved in the reverse order
    that they were pushed
    """
    my_stack = get_stack()
    
    for item in range(1, 5):
        push(my_stack, item)
        print('Pushing {0} on stack'.format(item))

    while not is_empty(my_stack):
        item = pop(my_stack)
        print('Popping {0} from stack'.format(item))
         

if __name__ == '__main__':
    main()