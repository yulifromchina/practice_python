#!/usr/bin/env python
# coding=utf-8
"""
对 ConfigSpiderConf 类进行单元测试。
"""

import unittest
import sys
sys.path.append("../")
from config_parse import ConfigSpiderConf


class TestConfigSpiderConf(unittest.TestCase):
    """
    对 ConfigSpiderConf 类进行单元测试
    """
    def setUp(self):
        self.conf_path = "../spider.conf"
        self.test_obj = ConfigSpiderConf(self.conf_path)
        self.test_obj.readConf()

    def tearDown(self):
        pass

    def test_readConf(self):
        conf_path = "./spider.conf"
        test_obj_1 = ConfigSpiderConf(conf_path)
        self.assertFalse(test_obj_1.readConf())

        conf_path = "../spider.conf"
        test_obj_2 = ConfigSpiderConf(conf_path)
        self.assertTrue(test_obj_2.readConf())

    def test_get_url_list_file(self):
        url = self.test_obj.get_url_list_file().split()
        self.assertEqual(url[0], "http://www.baidu.com")
        self.assertEqual(url[1], "http://www.sina.com.cn")

    def test_get_output_directory(self):
        self.assertEqual(self.test_obj.get_output_directory(), "./output")

    def test_get_max_depth(self):
        self.assertEqual(self.test_obj.get_max_depth(), 3)

    def test_get_crawl_interval(self):
        self.assertEqual(self.test_obj.get_crawl_interval(), 0.001)

    def test_get_crawl_timeout(self):
        self.assertEqual(self.test_obj.get_crawl_timeout(), 1)

    def test_get_target_url(self):
        self.assertEqual(self.test_obj.get_target_url(), ".*\.(gif|png|jpg|bmp)$")

    def test_get_thread_count(self):
        self.assertEqual(self.test_obj.get_thread_count(), 20)


if __name__ == "__main__":
    unittest.main()