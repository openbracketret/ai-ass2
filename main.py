import math



EARTH_RADIUS = 6371

def get_distance(lat_long1, lat_long2):

    x1 = EARTH_RADIUS * math.cos(lat_long1[0]) * math.cos(lat_long1[1])
    x2 = EARTH_RADIUS * math.cos(lat_long2[0]) * math.cos(lat_long2[1])

    y1 = EARTH_RADIUS * math.cos(lat_long1[0]) * math.sin(lat_long1[1])
    y2 = EARTH_RADIUS * math.cos(lat_long2[0]) * math.sin(lat_long2[1])

    z1 = EARTH_RADIUS * math.sin(lat_long1[0])
    z2 = EARTH_RADIUS * math.sin(lat_long2[0])

    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)