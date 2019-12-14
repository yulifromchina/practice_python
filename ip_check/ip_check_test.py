#!/usr/bin/env python3
"""
针对 ip_check 函数的单元测试
边界值：最小和最大：0.0.0.0  255.255.255.255
等价类：1）不符合格式，字节数不对
       2）不符合格式，包含字符串
       3）数字不在最大和最小范围内
       4）输入为空
"""


import unittest
from ip_check import ip_check


class TestIpCheck(unittest.TestCase):
    """
    对 ip_check 函数进行单元测试的类
    """
    def test_0(self):
        """
        边界
        """
        # 边界，最小
        ip_addr = "0.0.0.0"
        self.assertTrue(ip_check(ip_addr))
        # 边界，最大
        ip_addr = "255.255.255.255"
        self.assertTrue(ip_check(ip_addr))
        # 在最大和最小之间
        ip_addr = "  123.123.123.123"
        self.assertTrue(ip_check(ip_addr))

    def test_1(self):
        """
        等价类：不符合格式，字节数不对
        """
        ip_addr = "1.0.0"
        self.assertFalse(ip_check(ip_addr))
        ip_addr = "1.2.3.4.5"
        self.assertFalse(ip_check(ip_addr))
        ip_addr = "1.0.0.1"
        self.assertTrue(ip_check(ip_addr))

    def test_2(self):
        """
        等价类：不符合格式，包含字符串
        """
        ip_addr = "1.abc.2.4"
        self.assertFalse(ip_check(ip_addr))
        ip_addr = "abc"
        self.assertFalse(ip_check(ip_addr))
        ip_addr = "123"
        self.assertFalse(ip_check(ip_addr))

    def test_3(self):
        """
        等价类：数字不在最大和最小范围内
        """
        ip_addr = "999.999.999.999"
        self.assertFalse(ip_check(ip_addr))

    def test_4(self):
        """
        等价类：输入为空
        """
        ip_addr = ""
        self.assertFalse(ip_check(ip_addr))
        

if __name__ == "__main__":
    unittest.main()