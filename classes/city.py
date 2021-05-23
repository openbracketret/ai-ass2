import math


EARTH_RADIUS = 6371

class City:

    def __init__(self, lat, long):
        self.lat = lat
        self.long = long

    def get_distance(self, city):
        lat_long1 = (self.lat, self.long)
        lat_long2 = (city.lat, city.long)

        x1 = EARTH_RADIUS * math.cos(lat_long1[0]) * math.cos(lat_long1[1])
        x2 = EARTH_RADIUS * math.cos(lat_long2[0]) * math.cos(lat_long2[1])

        y1 = EARTH_RADIUS * math.cos(lat_long1[0]) * math.sin(lat_long1[1])
        y2 = EARTH_RADIUS * math.cos(lat_long2[0]) * math.sin(lat_long2[1])

        z1 = EARTH_RADIUS * math.sin(lat_long1[0])
        z2 = EARTH_RADIUS * math.sin(lat_long2[0])

        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)


