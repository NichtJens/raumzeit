#!/usr/bin/env python

import unittest

from vector import scale, dot, cross, Vector


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





if __name__ == '__main__':
    unittest.main()


