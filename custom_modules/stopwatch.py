#!/usr/bin/env python3
""" Stopwatch Objects - Keep track of time

Defines the structure and capabilities of a Stopwatch object
"""

from time import clock

class Stopwatch(object):    
    """
    Provides stopwatch objects that a programmer can use to time the
    execution time of portions of a program
    """

    def __init__(self):
        """ 
        Makes a new stopwatch ready for timing 
        """
        self.reset()
    
    def start(self):
        """
        Starts the stopwatch, unless it is already runnng.
        This method does not afect any time that may have already accumulated
        on the stopwatch
        """
        if not self._running:
            self._start_time = clock() - self._elapsed
            self._running = True # Clock now running

    def stop(self):
        """
        Stops the stopwatch, unless it is not running.
        Updates the accumulated elapsed time.
        """
        if self._running:
            self._elapsed = clock() - self._start_time
            self._running = False # Clock stopped
    
    def reset(self):
        """ Resets stopwatc to zero """
        self._start_time = self._elapsed = 0
        self._running = False

    def elapsed(self):
        """ Reveals the stopwatch running time since it was last reset. """
        if not self._running:
            return self._elapsed
        else:
            return clock() - self._start_time
