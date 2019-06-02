class Vehicle(object):
    def __init__(self, maxSpeed, timeToCrossCrater):
        self.maxSpeed = maxSpeed
        self.timeToCrossCrater = timeToCrossCrater
    
    @property
    def maxSpeed(self):
        return self._maxSpeed

    @maxSpeed.setter
    def maxSpeed(self, speed):
        if speed <= 0:
            raise ValueError("Vehicle speed cannot be less than or equal to 0 megamiles/hour")
        else:
            self._maxSpeed = speed

    @property
    def timeToCrossCrater(self):
        return self._timeToCrossCrater

    @timeToCrossCrater.setter
    def timeToCrossCrater(self, craterTime):
        if craterTime < 0:
            raise ValueError("Time to cross crater cannot be less than 0")
        else:
            self._timeToCrossCrater = craterTime

    