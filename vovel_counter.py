#!/usr/bin/env python3
''' Counts and displays the number of vowels in user input'''

word = input('Enter a Word(s) : ')
vowel_count = 0

for letter in word:
    if letter.upper() in ['A', 'E', 'I', 'O', 'U']:
        print('{0}, '.format(letter), sep='', end='')
        vowel_count +=1
print('({0} vowels)'.format(vowel_count), sep='')