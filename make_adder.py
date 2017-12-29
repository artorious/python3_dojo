#!/usr/bin/env python3
"""Demonstration of a simple closure
An example of a closure transporting a captured local variable out of a 
function. 

NOTE:
    A closure is a function that can capture the context of its surrounding 
    environment.
"""
def make_adder():
    """
    Returns a function
    """
    loc_var = 2 # Init local var
    return lambda x: x + loc_var  


if __name__ == '__main__':
    function = make_adder()
    print(function(10))
    print(function(5))