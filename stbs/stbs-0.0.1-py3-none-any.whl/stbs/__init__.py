import time


class TimerException(Exception):
    """Basic timer exception class to raise custom errors by this module;"""


class Timer():
    """Primary class of the module;"""


    def __init__(self, debug=False):
        self.running = False
        self.start_time = None

        if debug != True:
            self.debug = False


    # Print function adapted to handle debug mode;
    def p(self, txt: str):
        if self.debug:
            print("DEBUG >> " + txt)
        else:
            pass


    # Makes the timer start counting;
    def start(self):
        if not self.running:
            self.p("Timer started")
            self.start_time = time.perf_counter()
            self.running = True
        else:
            if self.debug:
                self.p("Can't start a already runnning timer!")
            else:
                raise TimerException("Can't start a already runnning timer!")


    # Restart the timer;
    def restart(self):
        if self.running:
            self.p("Timer restarted")
            self.start_time = time.perf_counter()
        else:
            if self.debug:
                self.p("Can't restart a not runnning timer!")
            else:
                raise TimerException("Can't restart a not runnning timer!")


    # Stops the timer;
    def stop(self):
        if self.running:
            self.p("Timer Stopped")
            self.running = False
            return round(time.perf_counter() - self.start_time, 4)
        else:
            if self.debug:
                self.p("Can't stop a not running timer!")
            else:
                raise TimerException("Can't stop a not running timer!")

    
    # Returns the current time;
    def current(self):
        if self.running:
            return round(time.perf_counter() - self.start_time, 4)
        else:
            if self.debug:
                self.p("Can't get current time from a not running timer!")
            else:
                raise TimerException("Can't get current time from a not running timer!")

