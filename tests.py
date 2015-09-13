#!/usr/bin/env python

import unittest

from vector import scale, dot, cross
from vector import isodd, iseven
from vector import Vector


class TestCaseMultiplication(unittest.TestCase):

    def test_mul_scale_zero(self):
        v = [0] * 3
        n = scale(v, 2)
        self.assertEqual(n, v)

    def test_mul_scale_2d(self):
        v = [4, 5]
        n = scale(v, 1.23)
        self.assertEqual(n, [4.92, 6.15])

        n = scale(n, 1/1.23)
        self.assertEqual(n, v)

    def test_mul_scale_3d(self):
        v = [1., 2., 3.]
        n = scale(v, 2)
        self.assertEqual(n, [2, 4, 6])

        n = scale(n, 1/2.)
        self.assertEqual(n, v)


    def test_mul_dot_zero(self):
        v = [0] * 3
        self.assertEqual(dot(v, v), 0)

    def test_mul_dot_2d(self):
        v = [4., 5.]
        self.assertEqual(dot(v, v), 41)

    def test_mul_dot_3d(self):
        v = [1, 2, 3]
        self.assertEqual(dot(v, v), 14)


    def test_mul_cross_zero(self):
        n = [0] * 3
        self.assertEqual(cross(n, n), n)

    def test_mul_cross_normal(self):
        n1 = [1., 0,  0]
        n2 = [0,  1., 0]
        n3 = [0,  0,  1.]
        self.assertEqual(cross(n1, n2), n3)

    def test_mul_cross(self):
        v1 = [ 1, 2,  3]
        v2 = [ 4, 5,  6]
        v3 = [-3, 6, -3]
        self.assertEqual(cross(v1, v2), v3)



class TestCaseVector(unittest.TestCase):

    def test_vec_init_2d(self):
        v = Vector(1, 2)
        ns = []
        ns.append( Vector(*[1, 2]) )
        ns.append( Vector(*(1, 2)) )
        ns.append( Vector( [1, 2]) )
        ns.append( Vector( (1, 2)) )
        for n in ns:
            self.assertEqual(v, n)

    def test_vec_init_3d(self):
        v = Vector(1, 2, 3)
        ns = []
        ns.append( Vector(*[1, 2, 3]) )
        ns.append( Vector(*(1, 2, 3)) )
        ns.append( Vector( [1, 2, 3]) )
        ns.append( Vector( (1, 2, 3)) )
        for n in ns:
            self.assertEqual(v, n)


    def test_vec_repr_2d(self):
        v = Vector(1, 2)
        self.assertEqual(repr(v), "(1, 2)")

    def test_vec_repr_3d(self):
        v = Vector(1, 2, 3)
        self.assertEqual(repr(v), "(1, 2, 3)")


    def test_vec_equality_2d(self):
        v1 = Vector(1, 2)
        v2 = Vector(1, 2)
        self.assertEqual(v1, v2)

    def test_vec_equality_3d(self):
        v1 = Vector(1, 2, 3)
        v2 = Vector(1, 2, 3)
        self.assertEqual(v1, v2)

    def test_vec_inequality(self):
        v1 = Vector(1, 2)
        v2 = Vector(1, 2, 3)
        self.assertNotEqual(v1, v2)


    def test_vec_length_zero(self):
        v = Vector(0, 0, 0)
        self.assertEqual(v.length, 0)
        self.assertAlmostEqual(v.length, abs(v))

    def test_vec_length_2d(self):
        v = Vector(3, 4)
        self.assertEqual(v.length, 5)
        self.assertAlmostEqual(v.length, abs(v))

    def test_vec_length_3d(self):
        v = Vector(1, 2, 3)
        self.assertAlmostEqual(v.length, 3.74165739)
        self.assertAlmostEqual(v.length, abs(v))


    def test_vec_dimension(self):
        v2 = Vector(1, 2)
        v3 = Vector(1, 2, 3)
        self.assertEqual(v2.dimension, 2)
        self.assertEqual(v3.dimension, 3)


    def test_vec_coords_2d(self):
        v = Vector(1, 2)
        self.assertEqual(v.x, 1)
        self.assertEqual(v.y, 2)
        self.assertEqual(v.z, None)

        v.x, v.y = 3, 4
        self.assertEqual(v.x, 3)
        self.assertEqual(v.y, 4)


    def test_vec_coords_3d(self):
        v = Vector(1, 2, 3)
        self.assertEqual(v.x, 1)
        self.assertEqual(v.y, 2)
        self.assertEqual(v.z, 3)

        v.x, v.y, v.z = 4, 5, 6
        self.assertEqual(v.x, 4)
        self.assertEqual(v.y, 5)
        self.assertEqual(v.z, 6)

        v = Vector(7, 8)
        v.z = 9
        self.assertEqual(v.x, 7)
        self.assertEqual(v.y, 8)
        self.assertEqual(v.z, 9)


    def test_vec_add_zero(self):
        v = Vector(0, 0, 0)
        self.assertEqual(v + v, v)

    def test_vec_add_2d(self):
        v1 = Vector(1, 2)
        v2 = Vector(3, 4)
        n  = Vector(4, 6)
        self.assertEqual(v1 + v2, n)

    def test_vec_add_3d(self):
        v1 = Vector(1, 2, 3)
        v2 = Vector(4, 5, 6)
        n  = Vector(5, 7, 9)
        self.assertEqual(v1 + v2, n)

    def test_vec_sub_zero(self):
        v = Vector(0, 0, 0)
        self.assertEqual(v - v, v)

    def test_vec_sub_2d(self):
        v1 = Vector(1, 2)
        v2 = Vector(3, 4)
        n  = Vector(-2, -2)
        self.assertEqual(v1 - v2, n)

    def test_vec_sub_3d(self):
        v1 = Vector(1, 2, 3)
        v2 = Vector(4, 5, 6)
        n  = Vector(-3, -3, -3)
        self.assertEqual(v1 - v2, n)


    def test_vec_scale_zero(self):
        f = 2
        v = Vector(0, 0, 0)
        self.assertEqual(f * v, v)
        self.assertEqual(v * f, v)
        self.assertEqual(scale(v, f), v)

    def test_vec_scale_2d(self):
        f = 2.5
        x, y = 4, 5
        v = Vector(x, y)
        d = Vector(f * x, f * y)

        n = v * f
        self.assertEqual(d, n)

        n = n * (1/f)
        self.assertEqual(v, n)

        n = f * v
        self.assertEqual(d, n)

        n = (1/f) * n
        self.assertEqual(v, n)

        n = scale(v, f)
        self.assertEqual(d, n)

        n = scale(n, (1/f))
        self.assertEqual(v, n)

    def test_vec_scale_3d(self):
        f = 2
        x, y, z = 1., 2., 3.

        v = Vector(x, y, z)
        d = Vector(f * x, f * y, f * z)

        n = v * f
        self.assertEqual(d, n)

        n = n * (1./f)
        self.assertEqual(v, n)

        n = f * v
        self.assertEqual(d, n)

        n = (1./f) * n
        self.assertEqual(v, n)

        n = scale(v, f)
        self.assertEqual(d, n)

        n = scale(n, (1./f))
        self.assertEqual(v, n)


    def test_vec_dot_zero(self):
        v = Vector(0, 0, 0)
        self.assertEqual(v * v, 0)
        self.assertEqual(dot(v, v), 0)

    def test_vec_dot_2d(self):
        v = Vector(4., 5.)
        self.assertEqual(v * v, 41)
        self.assertEqual(dot(v, v), 41)

    def test_vec_dot_3d(self):
        v = Vector(1, 2, 3)
        self.assertEqual(v * v, 14)
        self.assertEqual(dot(v, v), 14)


    def test_vec_cross_zero(self):
        n = Vector(0, 0, 0)
        self.assertEqual(n % n, n)
        self.assertEqual(cross(n, n), n)

    def test_vec_cross_normal(self):
        n1 = Vector(1., 0,  0)
        n2 = Vector(0,  1., 0)
        n3 = Vector(0,  0,  1.)
        self.assertEqual(n1 % n2, n3)
        self.assertEqual(cross(n1, n2), n3)

    def test_vec_cross(self):
        v1 = Vector( 1, 2,  3)
        v2 = Vector( 4, 5,  6)
        v3 = Vector(-3, 6, -3)
        self.assertEqual(v1 % v2, v3)
        self.assertEqual(cross(v1, v2), v3)


    def test_vec_mod(self):
        v = Vector(3, 4, 5)
        n = Vector(0, 1, 2)
        self.assertEqual(v % 3, n)


    def test_vec_div(self):
        v = Vector(2, 4, 6)
        n = Vector(1, 2, 3)
        self.assertEqual(v / 2, n)

    def test_vec_pow(self):
        x, y, z = 2, 4, 6
        v = Vector(x, y, z)

        for i in (2, 6):
            n = (x**2 + y**2 + z**2)**(i/2.)
            self.assertAlmostEqual(v**i, n)

        for i in (3, 7):
            n = Vector(x, y, z) * (x**2 + y**2 + z**2)**((i-1)/2.)
            self.assertAlmostEqual(v**i, n)



class TestCaseHelper(unittest.TestCase):

    def test_iseven(self):
        self.assertTrue( iseven(0) )
        for i in (2, 6, 42):
            self.assertTrue(  iseven(i) )
            self.assertFalse( iseven(i+1) )

    def test_isodd(self):
        self.assertFalse( isodd(0) )
        for i in (1, 5, 23):
            self.assertTrue(  isodd(i) )
            self.assertFalse( isodd(i+1) )





if __name__ == '__main__':
    unittest.main()


