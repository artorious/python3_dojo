#!/usr/bin/env python3
""" An exploded string type """

class ExplodedStr(str):
    """ Exploded string class 
    ExplodedStr Type as a Subclass of the Built-in str Class
    """
    
    def __init__(self, value=''):
        """ (ExplodedStr, str) -> str """
        str.__init__(value)   

    def explode(self):
        """ (ExplodedStr) -> str
        
        Returns an exploded string, a string with spaces (blank characters) 
        between all characters, for example, 'H e l l o'.
        """
        # Empty str returned unaltered
        if len(self) == 0:
            return self
        else:
            # Create exploded string
            empty_str = ''
            blank_char = ' '
            temp_str = empty_str

            for char_pos in range(0, len(self) - 1):
                temp_str += self[char_pos] + blank_char
            # Append last char without following blank
            temp_str += self[len(self) - 1]
            
            return temp_str # Exploded str 
