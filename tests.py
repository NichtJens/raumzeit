#!/usr/bin/env python

import unittest

from vector import scale, dot, cross, Vector


class TestCaseMultiplication(unittest.TestCase):

    def test_scale_zero(self):
        v = [0] * 3
        n = scale(v, 2)
        self.assertEqual(n, v)

    def test_scale_2d(self):
        v = [4, 5]
        n = scale(v, 1.23)
        self.assertEqual(n, [4.92, 6.15])

        n = scale(n, 1/1.23)
        self.assertEqual(n, v)

    def test_scale_3d(self):
        v = [1., 2., 3.]
        n = scale(v, 2)
        self.assertEqual(n, [2, 4, 6])

        n = scale(n, 1/2.)
        self.assertEqual(n, v)


    def test_dot_zero(self):
        v = [0] * 3
        self.assertEqual(dot(v, v), 0)

    def test_dot_2d(self):
        v = [4., 5.]
        self.assertEqual(dot(v, v), 41)

    def test_dot_3d(self):
        v = [1, 2, 3]
        self.assertEqual(dot(v, v), 14)


    def test_cross_zero(self):
        n = [0] * 3
        self.assertEqual(cross(n, n), n)

    def test_cross_normal(self):
        n1 = [1., 0,  0]
        n2 = [0,  1., 0]
        n3 = [0,  0,  1.]
        self.assertEqual(cross(n1, n2), n3)

    def test_cross(self):
        v1 = [ 1, 2,  3]
        v2 = [ 4, 5,  6]
        v3 = [-3, 6, -3]
        self.assertEqual(cross(v1, v2), v3)



class TestCaseVector(unittest.TestCase):

    def test_scale(self):
        pass

    def test_dot(self):
        pass

    def test_cross(self):
        pass




if __name__ == '__main__':
    unittest.main()


