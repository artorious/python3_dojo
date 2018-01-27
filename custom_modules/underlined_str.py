#!/usr/bin/env python3
""" Underlined String """

class UnderlinedStr(str):
    """ Underlined string class definition """

    def __init__(self, u_str):
        """ (UnderlinedStr, str) -> str """
        str.__init__(u_str)
    
    def underline(self):
        """ (UnderlinedStr) -> str """
        
        return str.__str__(self) + '\n' + format('', '-<' + str(len(self)))
    
