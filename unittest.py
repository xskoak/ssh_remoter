#!/usr/bin/env python3

import unittest

class FirstTestClass(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('rubiks code'.upper(), 'RUBIKS CODE')

if __name__ == '__main__':
    unittest.main()
