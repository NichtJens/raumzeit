

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
# conversion from/to spherical coordinates should be possible

class Vector(list):

    def __init__(self, x, y, z, t):
        pass

    def __repr__(self):
        pass


    def __eq__(self, other):
        pass

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __div__(self, other):
        pass

    def __pow__(self, exponent):
        pass



