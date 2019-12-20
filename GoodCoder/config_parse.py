#!/usr/bin/env python
# coding=utf-8
"""
通过 ConfigParser 类解析 spider.conf 配置文件。
"""

import ConfigParser
import logging

class ConfigSpiderConf(object):
    """
    读取 spider conf 配置文件
    """
    def __init__(self, conf_path):
        self.conf_path = conf_path
        self.config = ConfigParser.RawConfigParser()

    def readConf(self):
        """
        读取 conf 文件
        Attrs:
            无
        Returns:
            True/False:读取成功/失败
        """
        try:
            logging.info(u"读取 conf 文件 %s" % self.conf_path)
            self.config.read(self.conf_path)
        except Exception as e:
            logging.error(u"读取 conf 文件出错 %s" % e)
            return False
        
        try:
            logging.info(u"开始读取 conf 配置...")
            self.url_list_file = self.config.get("spider", "url_list_file")
            self.output_directory = self.config.get("spider", "output_directory")
            self.max_depth = self.config.getint("spider", "max_depth")
            self.crawl_interval = self.config.getfloat("spider", "crawl_interval")
            self.crawl_timeout = self.config.getfloat("spider", "crawl_timeout")
            self.target_url = self.config.get("spider", "target_url")
            self.thread_count = self.config.getint("spider", "thread_count")
        except Exception as e:
            logging.error(u"读取 conf 配置出错 %s" % e)
            return False
        return True

    def get_url_list_file(self):
        """
        返回 url_list_file
        """
        return self.url_list_file

    def get_output_directory(self):
        """
        返回 output_directory
        """
        return self.output_directory

    def get_max_depth(self):
        """
        返回 get_max_depth
        """
        return self.max_depth

    def get_crawl_interval(self):
        """
        返回 crawl_interval
        """
        return self.crawl_interval

    def get_crawl_timeout(self):
        """
        返回 crawl_timeout
        """
        return self.crawl_timeout

    def get_target_url(self):
        """
        返回 target_url
        """
        return self.target_url

    def get_thread_count(self):
        """
        返回 thread_count
        """
        return self.thread_count


if __name__ == "__main__":
    obj = ConfigSpiderConf("./spider.conf")
    if obj.readConf() is True:
        print obj.get_url_list_file()
        print obj.get_output_directory()
        print obj.get_max_depth()
        print obj.get_crawl_interval()
        print obj.get_crawl_timeout()
        print obj.get_target_url()
        print obj.get_thread_count()
