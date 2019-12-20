#!/usr/bin/env python
# coding=utf-8
"""
对 MyCrawler 类进行单元测试。
"""

import sys
import logging
import unittest
sys.path.append("../")
from crawler import MyCrawler

class TestMyCrawler(unittest.TestCase):
    """
    对 MyCrawler 类进行单元测试
    """
    def setUp(self):
        seeds = "http://cp01-rdqa-dev-yulii06.epc.baidu.com:8080/index1.html"
        crawl_deepth = 1
        output_dir = "output"
        target_url = ".*\.(gif|png|jpg|bmp)$"
        crawl_interval = 0.001
        timeout = 1
        thread_count = 1
        logging.basicConfig(level=logging.INFO)
        self.test_obj = MyCrawler(seeds, crawl_deepth, output_dir, target_url,
                            crawl_interval, timeout, thread_count)

    def tearDown(self):
        pass

    def test_crawling_single(self):
        """
        测试 crawling_single
        """
        self.assertEqual(self.test_obj.crawling_single(), None)

    def test_crawling_multithread(self):
        """
        测试 crawling_multithread
        """
        self.assertEqual(self.test_obj.crawling_multithread(),None)


if __name__ == "__main__":
    unittest.main()
