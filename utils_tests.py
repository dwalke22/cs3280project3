#!/usr/bin/env python3
"""
Unit test for utils.py
"""

import unittest
import utils

__author__ = "David Walker"
__verison__ = "Fall 2020"

class TestUtils(unittest.TestCase):
    def test_nonvalid_ipv4(self):
        self.assertFalse(utils.verify_ipv4("12"))

    def test_valid_ipv4(self):
        self.assertTrue(utils.verify_ipv4("192.168.244.3"))

    def test_single_port(self):
        ports = utils.scan("127.0.0.1", 50000, 50000)
        size = len(ports)
        self.assertEqual(size, 1)

    def test_multiple_ports(self):
        ports = utils.scan("127.0.0.1", 50000, 50003)
        size = len(ports)
        self.assertEqual(size, 4)

if __name__ == "__main__":
    unittest.main()
