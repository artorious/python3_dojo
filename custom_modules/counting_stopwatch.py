#!/usr/bin/env python3
""" Stop Watch Program 

A stopwatch object that records the number of times the watch has been started 
until it is reset. 
"""

from stopwatch import Stopwatch

class CountingStopwatch(Stopwatch):
    """ A stopwatch obj inheriting from  Stopwatch """
    def __init__(self):
        super(CountingStopwatch, self).__init__() # Init base class with inherited instance vars
        self._count = 0 # Init counter var

    def start(self):
        """ Start Clock """
        # Count this start message unless the watch already is running
        if not self._running:
            self._count += 1
        super(CountingStopwatch, self).start()    # Let base class do its start cose
    
    def reset(self):
        """ Reset Clock """
        super(CountingStopwatch, self).reset() # Let base class reset the inherited instance vars
        self._count = 0 # Reset counter

    def counter(self):
        """ number of times the watch has been started until it is reset. """
        return self._count

def main():
    """ Sample client code that uses the CountingStopwatch class """

    from time import sleep

    timer = CountingStopwatch()

    timer.start()
    sleep(10)   # Pause program for 10 secs
    timer.stop()
    print('Time: {0} --- Count Number: {1}'.format(
        timer.elapsed(), timer.counter()))
    
    timer.start()
    sleep(5)   # Pause program for 5 secs
    timer.stop()
    print('Time: {0} --- Count Number: {1}'.format(
        timer.elapsed(), timer.counter()))

    timer.start()
    sleep(17)   # Pause program for 17 secs
    timer.stop()
    print('Time: {0} --- Count Number: {1}'.format(
        timer.elapsed(), timer.counter()))

if __name__ == '__main__':
    main()