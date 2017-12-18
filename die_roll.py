#!/usr/bin/env python3
'''Die Rolling Simulator

A program that simulates the rolling of a die.
'''
from random import randrange
from custom_modules.get_positive_number_from_user import get_positive_num

def show_die(spots):
    """
    Draws a picture of a die with the number of <spots> indicated.
    <spots> is the number of spots on the top face. 
    """
    print('+-------+')
    if spots == 1:
        print('|       |')
        print('|   *   |')
        print('|       |')
    elif spots == 2:
        print('| *     |')
        print('|       |')
        print('|     * |')
    elif spots == 3:
        print('|     * |')
        print('|   *   |')
        print('| *     |')
    elif spots == 4:
        print('| *   * |')
        print('|       |')
        print('| *   * |')
    elif spots == 5:
        print('| *   * |')
        print('|   *   |')
        print('| *   * |')
    elif spots == 6:
        print('| * * * |')
        print('|       |')
        print('| * * * |')
    else:
        print('*** Error: Illegal die spots ***')
    print('+-------+')

def roll():
    """ Returns a pseudorandom number in the range 1...6, inclusive """
    return randrange(1, 7) # Six die-faces

def simulate_die(num_of_rolls):
    """ Simulates the roll of a die <num_of_rolls> 
    <num_of_rolls> is a positive integer indicating the number of rolls
    """
    for a_roll in range(1, num_of_rolls + 1):
        show_die(roll())


if __name__ == '__main__':
    simulate_die(int(get_positive_num()))

    

