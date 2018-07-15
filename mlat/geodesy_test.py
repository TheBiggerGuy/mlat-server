#!/usr/bin/env python

import unittest


from .geodesy import llh2ecef
from .geodesy import ecef2llh
from .geodesy import greatcircle


class CoordinateConversionTest(unittest.TestCase):
    def test_llh2ecef(self):
        self.assertEqual(llh2ecef((0, 0, 0)), (6378137.0, 0.0, 0.0))

    def test_ecef2llh(self):
        self.assertEqual(ecef2llh((6378137.0, 0.0, 0.0)), (0, 0, 0))

    def test_round_trip(self):
        self.assertEqual(ecef2llh(llh2ecef((0, 0, 0))), (0, 0, 0))


class GreatCircleTest(unittest.TestCase):
    def test_greatcircle(self):
        self.assertEqual(greatcircle((0, 0), (0, 0)), 0)
        self.assertEqual(greatcircle((0, 0), (1, 0)), 111194.92664454764)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
