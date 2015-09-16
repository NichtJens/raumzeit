
import math


def iseven(i):
    return i % 2 == 0

def isodd(i):
    return not iseven(i)


# the types of multiplication should be defined as standalone functions
# for now: operating on lists

def scale(V, s):
    return [c * s for c in V]

def dot(A, B):
    return sum(a * b for a, b in zip(A, B))

def cross(A, B):
    x = A[1]*B[2] - A[2]*B[1]
    y = A[2]*B[0] - A[0]*B[2]
    z = A[0]*B[1] - A[1]*B[0]
    return [x, y, z]



# x, y, z, and t should be properties of the class
# further properties: dimension, length (and alternative names for these)

class Vector(list):

    def __init__(self, x, y=None, z=None):
        if y is not None:
            list.__init__(self)
            self += [c for c in (x, y, z) if c is not None]
        else:
            list.__init__(self, x)

        # handle alternatives like Vector(L) with L=(1, 2, ...)
        # handle 4d vectors, t should be zeroth component
        # spherical and cylindrical coordinates

        # negative exponents?
        # add: V.normalized -> V/V.length


    def __repr__(self):
        return repr(tuple(self))

    def __eq__(self, other):
        return False not in [s == o for s, o in zip(self, other)]

    @property
    def dimension(self):
        return len(self)

    dim = dimension


    # these can probably be done more generic
    @property
    def x(self):
        return self[0]

    @x.setter
    def x(self, value):
        self[0] = value

    @property
    def y(self):
        return self[1]

    @y.setter
    def y(self, value):
        self[1] = value

    @property
    def z(self):
        try:
            return self[2]
        except IndexError:
            return None

    @z.setter
    def z(self, value):
        try:
            self[2] = value
        except IndexError:
            self += [value]


    def __abs__(self):
        return math.sqrt(sum(s**2 for s in self))

    length = property(__abs__)
    mag = magnitude = norm = abs = absolute = len = length
    r = rad = radius = length


    @property
    def theta(self):
        if self.radius != 0 and self.z is not None:
            return math.acos(self.z / self.radius)
        else:
            return 0.


    @property
    def phi(self):
        return math.atan2(self.y, self.x)


    def __add__(self, other):
        return Vector(*[s + o for s, o in zip(self, other)])

    def __sub__(self, other):
        return Vector(*[s - o for s, o in zip(self, other)])


    def __mul__(self, other):
        if isinstance(other, type(self)):
            return self.dot(other)
        else:
            return self.scale(other)

    __rmul__ = __mul__


    def __mod__(self, other):
        if isinstance(other, type(self)):
            return self.cross(other)
        else:
            return Vector(*[s % other for s in self])


    def __div__(self, other):
        return self.scale(1/float(other))


    def __pow__(self, exponent):
        if iseven(exponent):
            return self.length**exponent
        else:
            return self * self**(exponent - 1)


    def scale(self, other):
        return Vector(*scale(self, other))

    def dot(self, other):
        return dot(self, other)

    def cross(self, other):
        x = self.y * other.z - self.z * other.y
        y = self.z * other.x - self.x * other.z
        z = self.x * other.y - self.y * other.x
        return Vector(x, y, z)



