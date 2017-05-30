import logging
logging.basicConfig(level=logging.INFO, format=' %(asctime)s -%(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)


class Clock:

    def __init__(self, hours, minutes):
        """Creates a clock that displays the time based on user input of hours and minutes"""
        
        assert (isinstance(hours, int))
        assert (isinstance(minutes, int))

        logging.info("Hours: " + str(hours) + " Minutes: " + str(minutes))

        self.hours = hours
        self.minutes = minutes

        logging.info("(Before conversion) Hours: " + str(self.hours))
        logging.info("(Before conversion) Minutes: " + str(self.minutes))

        # Convert hours and minutes so they roll over correctly
        self.convert()

        logging.info("(After conversion) Hours: " + str(self.hours))
        logging.info("(After conversion) Minutes: " + str(self.minutes))

    def __str__(self):
        return self.get_time()

    def __eq__(self, other):
        return self.get_time() == other.get_time()

    def get_time(self):
        return "{:02d}:{:02d}".format(self.hours, self.minutes)

    def convert(self):
        # 80 minutes -> 1 hour and 20 minutes
        # 26 hours -> 2 hours

        self.hours += self.minutes // 60
        self.minutes = self.minutes % 60
        self.hours = self.hours % 24

        logging.info("(Before adding) Time: " + self.get_time())

        return self.get_time()

    def add(self, more_minutes):
        self.minutes += more_minutes
        self.convert()

        logging.info("(After adding) Time: " + self.get_time())

        return self.get_time()

clock = Clock(7274, -682)
print(clock)
