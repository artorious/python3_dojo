#!/usr/bin/env python3
""" Stop Watch Program 

A stopwatch object that records the number of times the watch has been started 
until it is reset. 
"""

from custom_modules.stopwatch import Stopwatch

class CountingStopwatch(Stopwatch):
    """ A stopwatch obj inheriting from  Stopwatch """
    def __init__(self):
        super().__init__() # Init base class with inherited instance vars
        self._count = 0 # Init counter var

    def start(self):
        """ Start Clock """
        # Count this start message unless the watch already is running
        if not self._running:
            self._count += 1
        super().start()    # Let base class do its start cose
    
    def reset(self):
        """ Reset Clock """
        super().reset() # Let base class reset the inherited instance vars
        self._count = 0 # Reset counter

    def counter(self):
        """ number of times the watch has been started until it is reset. """
        return self._count