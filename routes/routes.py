class Orbit(object):
    def __init__(self, traffic_speed, total_craters, distance):
        self.traffic_speed = traffic_speed # calls the setter method
        self.total_craters = total_craters
        self.distance = distance

    @property
    def traffic_speed(self):
        return self._trafficSpeed

    @traffic_speed.setter
    def traffic_speed(self, speed):
        if speed <= 0:
            raise ValueError("Traffic speed cannot be less than or equal to 0 megamiles/hour")
        else:
            self._trafficSpeed = speed

    @property
    def total_craters(self):
        return self._total_craters

    @total_craters.setter
    def total_craters(self, craters):
        if len(craters) == 0:
            raise ValueError("Invalid input. Enter value for craters")
        else:
            if craters[1] == 0:
                self._total_craters = craters[0]
            elif craters[1] > 0:
                self._total_craters = int(craters[0] * ((100+craters[1]) / 100))

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, orbit_distance):
        if orbit_distance < 0:
            raise ValueError("Traffic speed cannot be less than or equal to 0 megamiles/hour")
        else:
            self._distance = orbit_distance


