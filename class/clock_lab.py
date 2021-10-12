class Clock(object):
    def __init__(self, hour, minutes=0):
        # str() function converts the specified value into a string
        self.minutes = '0' * (2-len(str(minutes)))+str(minutes)
        self.hour = '0' * (2-len(str(hour)))+str(hour)

    @classmethod
    def at(cls, hour, minutes=0):
        return cls(hour, minutes)

    def __str__(self):

    def __add__(self, minutes):

    def __sub__(self, minutes):

    def __eq__(self, other):

    def __ne__(self, other):

# Clock
# Clock(9,8)
# CLock.at(9,8)
# x=Clock.at(9,8)
# x