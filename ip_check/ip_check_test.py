#!/usr/bin/env python3
"""
针对 ip_check 函数的单元测试
"""


import unittest
from ip_check import ip_check


class TestIpCheck(unittest.TestCase):
    """
    对 ip_check 函数进行单元测试的类
    """
    def test_legal_ip(self):
        ip_addr = "1.0.0.0"
        self.assertTrue(ip_check(ip_addr))
        ip_addr = "255.255.255.255"
        self.assertTrue(ip_check(ip_addr))
        ip_addr = "  123.123.123.123"
        self.assertTrue(ip_check(ip_addr))

    def test_illegal_ip(self):
        ip_addr = "1.0.0"
        self.assertFalse(ip_check(ip_addr))
        ip_addr = "1.2.3.4.5"
        self.assertFalse(ip_check(ip_addr))
        ip_addr = "1.abc.2.4"
        self.assertFalse(ip_check(ip_addr))
        ip_addr = "abc"
        self.assertFalse(ip_check(ip_addr))
        ip_addr = "123"
        self.assertFalse(ip_check(ip_addr))
        

if __name__ == "__main__":
    unittest.main()