#!/usr/bin/env python

import unittest


from .geodesy import greatcircle


class GreatCircleTest(unittest.TestCase):
    def test_greatcircle(self):
        self.assertEqual(greatcircle((0, 0), (0, 0)), 0)
        self.assertEqual(greatcircle((0, 0), (1, 0)), 111194.92664454764)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
