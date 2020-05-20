class Point3D:

    def __init__(self, x=None, y=None, z=None):
        self.x = x
        self.y = y
        self.z = z

    def distance(self, other):
        if isinstance(other, Point3D):
            distance = ((other.x - self.x) ** 2 + (other.y - self.y) ** 2
                        + (other.z - self.z) ** 2) ** 0.5
        else:
            raise ValueError
        return distance


class Point3D1:

    def __init__(self, *args):
        for x in args:
            if not isinstance(x, (int, float)):
                raise ValueError
        self.args = args

    def distance(self, other):
        distance = ((other.args[0] - self.args[0]) ** 2 + (other.args[1] - self.args[1]) ** 2
                    + (other.args[2] - self.args[2]) ** 2) ** 0.5
        return distance


a = [-74.47220433185721, 33.7341005642194, -77.5037737985927]
b = [-47.735349609428624, -76.5908841887246, -20.063098551336765]
c = Point3D1(*a)
y = Point3D1(*b)
print(c.distance(y))
