

# the types of multiplication should be defined as standalone functions:

def scale(V, s):
    pass

def dot(A, B):
    pass

def cross(A, B):
    pass



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



