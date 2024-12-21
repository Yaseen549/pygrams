from math import radians, sin, cos, sqrt, atan2

def calculate_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the distance between two geographic coordinates using the Haversine formula.

    Parameters:
    ----------
    lat1, lon1 : float
        The latitude and longitude of the first location.
    lat2, lon2 : float
        The latitude and longitude of the second location.

    Returns:
    -------
    float
        The distance in kilometers between the two points.

    Examples:
    --------
    >>> calculate_distance(52.5200, 13.4050, 48.8566, 2.3522)
    878.66  # Approximate distance from Berlin to Paris
    """
    # Radius of the Earth in kilometers
    R = 6371.0

    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Haversine formula to calculate the distance
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    # Calculate distance
    distance = R * c
    return distance
