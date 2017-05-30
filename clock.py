class Clock:

    def __init__(self, hours, minutes):
        """Creates a clock that displays the time based on user input of hours and minutes"""
        
        assert (isinstance(hours, int))
        assert (isinstance(minutes, int))

        self.hours = hours
        self.minutes = minutes

        # Convert hours and minutes so they roll over correctly
        self.convert()

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

        return self.get_time()

    def add(self, more_minutes):
        self.minutes += more_minutes
        self.convert()

        return self.get_time()
