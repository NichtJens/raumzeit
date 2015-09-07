

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

    def __init__(self, x, y=None, z=None, t=None):
        if y is not None:
            list.__init__(self)
            self += [c for c in (x, y, z, t) if c is not None]
        else:
            list.__init__(self, x)

        # handle alternatives like Vector(L) with L=(1, 2, ...)
        # handle 4d vectors, t should be zeroth component
        # spherical and cylindrical coordinates


    def __repr__(self):
        return repr(tuple(self))


    def __eq__(self, other):
        return False not in [s == o for s, o in zip(self, other)]


    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass


    def __mul__(self, other):
        if isinstance(other, type(self)):
            return dot(self, other)
        else:
            return Vector(*scale(self, other))

    __rmul__ = __mul__


    def __mod__(self, other):
        if isinstance(other, type(self)):
            return Vector(*cross(self, other))
        else:
            return Vector(*[c % other for c in self])


    def __div__(self, other):
        pass

    def __pow__(self, exponent):
        pass



