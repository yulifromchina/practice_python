#!/usr/bin/env python
# coding=utf-8

"""
主程序，运行入口。
"""

import argparse
import logging
import sys
from logger import init_log
from config_parse import ConfigSpiderConf
from crawler import MyCrawler

if __name__ == "__main__":

    init_log("./log/mini_spider")
    logging.info(u"开始解析参数...")
    parser = argparse.ArgumentParser(description="Mini Spider of Multithreading.")
    parser.add_argument("-v", action="store_true", help="Show Version info.")
    parser.add_argument("-c", action="store", help="Input config file.")
    args = parser.parse_args()
    if args.v is True:
        print "Mini Spider V 1.0."
        logging.info(u"解析参数结束.")
        sys.exit(0)
    if args.c is None:
        logging.info(u"解析参数结束.")
        sys.exit(1)     
    logging.info(u"解析参数结束.")

    logging.info(u"开始读取 spider 的 conf文件...")
    config_path = args.c    
    config_spider = ConfigSpiderConf(config_path)
    if config_spider.readConf() is False:
        exit
    url_list_file = config_spider.get_url_list_file()
    output_directory = config_spider.get_output_directory()
    max_depth = config_spider.get_max_depth()
    crawl_interval = config_spider.get_crawl_interval()
    crawl_timeout = config_spider.get_crawl_timeout()
    target_url = config_spider.get_target_url()
    thread_count = config_spider.get_thread_count()
    logging.info(u"读取 conf 文件结束.")

    logging.info(u"启动爬虫...")
    url_list_file = "http://cp01-rdqa-dev-yulii06.epc.baidu.com:8080/index4.html"
    mini_spider = MyCrawler(url_list_file, max_depth, output_directory, 
                            target_url, crawl_interval, crawl_timeout, thread_count)
    mini_spider.crawling_multithread()
    logging.info(u"爬虫爬取结束.")


