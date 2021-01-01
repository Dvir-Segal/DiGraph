class GeoLocation:
    """ This abstract class represents a Node's location """
    _x = 0
    _y = 0
    _z = 0

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z
    """Constructor"""

    def get_location(self):
        return self
    """ This methode return the Node's location.
     @return: the location"""


    def distance(self, g):
        t = pow((self._x-g._x), 2) + pow((self._y-g._y), 2) + pow((self._z-g._z), 2)
        outcome = pow(t, 0.5)
        return outcome
    """ This methode return the distance from this location to g.
     @return: the distance from this location to g"""





