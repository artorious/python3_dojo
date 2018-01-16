#!/usr/bin/env python3
""" A simple spanish-english translator

Uses a dictionary to assist the translation.
"""

translator = {  
    'uno':'one',
    'dos':'two',
    'tres':'three',
    'cuatro':'four',
    'cinco':'five',
    'seis':'six',
    'siete':'seven',
    'ocho':'eight'
    }

word = '*'
while word != '':   # Loop until user presses return by itself
    # Obtain word from the user
    word = input('Enter Spanish word:\n>>> ')
    if word in translator:
        print(translator[word])
    else:
        print('????') # Unkown word