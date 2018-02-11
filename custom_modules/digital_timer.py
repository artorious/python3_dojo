#!/usr/bin/env python3
""" A string containing the digital representation of the time. """

from timer import Timer

class DigitalTimer(Timer):
    """ Digital representation of the time. """
    def __init__(self, **kwargs):
        super(DigitalTimer, self).__init__(**kwargs)
        print('Initializing digital stopwatch')
    
    def digital_time(self):
        """
        Returns a string representation of the elapsed time in 
        hours : minutes : seconds
        """
        # Compute time in hours, minutes, and seconds
        seconds = round(self.elapsed())
        hours =  seconds // 3600    # Compute total hours
        seconds %= 3600             # Update seconds remaining
        minutes = seconds // 60     # Compute minutes
        seconds %= 60               # Update seconds remaining

        # Each digit occupies two spaces; pad with leading zeros, if necessary
        return '{0:0>2}:{1:0>2}:{2:0>2}'.format(hours, minutes, seconds)


if __name__ == '__main__':
    from time import sleep
    timer = DigitalTimer()
    timer.start()
    sleep(5)
    timer.stop()
    print('Five sec sleep: {0}'.format(timer.elapsed()))
