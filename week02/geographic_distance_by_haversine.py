from math import sin, cos, sqrt, radians


def geographic_distance_by_haversine(lat1: float, lng1: float, lat2: float, lng2: float) -> float:
    rad_lat1 = radians(lat1)
    rad_lng1 = radians(lng1)
    rad_lat2 = radians(lat2)
    rad_lng2 = radians(lng2)

    r = 6371

    sub_step1 = sin((rad_lat2 - rad_lat1) / 2)

    sub_step2 = sin((rad_lng2 - rad_lng1) / 2)

    step1 = sub_step1 ** 2 + cos(rad_lat1) * cos(rad_lat2) * sub_step2 ** 2

    step2 = sqrt(step1)

    step3 = 1 / sin(step2)

    d = 2 * r * step3

    return d


print(geographic_distance_by_haversine(
    27.175015, 78.042155, 10.595294, 106.411536))
