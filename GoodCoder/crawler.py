#!/usr/bin/env python
# coding=utf-8

"""
具体执行爬取行为。
"""

import logging
import requests
import re
import os
import urlparse
import time
from Queue import Queue
from bs4 import BeautifulSoup
from threading import Thread


class MyCrawler(object):
    """
    爬虫类，实现单线程和多线程爬虫
    """
    def __init__(self, seeds, crawl_deepth, output_dir, target_url, crawl_interval, timeout, thread_count=1):
        """
        Attrs: 
            seeds: 种子链接
            crawl_deepth: 爬取最大深度
            output_dir: 结果存储目录
            target_url: 要保存文件的正则表达式
            crawl_interval:爬取间隔
            timeout: 爬取超时时间
        """
        self.unvisited = Queue()
        self.visited = []
        seeds = seeds.split()
        for i in seeds:
            self.unvisited.put((i, 0))
            logging.info(u"入队种子链接 %s" % i)
        self.crawl_deepth = crawl_deepth
        self.target_url = target_url
        self.output_dir = output_dir
        if os.path.isdir(self.output_dir) is False:
            os.mkdir(self.output_dir)
        self.crawl_interval = crawl_interval
        self.crawl_timeout = timeout
        self.thread_count = thread_count
        
    def save_file(self, file_name, content):
        """
        保存爬取的文件
        Attrs:
            file_name: 文件名称
            content: 文件内容
        """
        logging.info(u"[Store]存储文件 %s" % file_name)
        file_name = os.path.basename(file_name)
        file_path = os.path.join(self.output_dir, file_name)
        with open(file_path, "wb") as f:
            f.write(content)

    def crawling_single(self):
        """
        单线程爬虫
        """
        while self.unvisited.empty() is False:
            cur_obj = self.unvisited.get()
            cur_url = cur_obj[0]
            cur_deepth = cur_obj[1]
            logging.info(u"当前队头的 url 是 %s" % cur_url)

            if cur_deepth > self.crawl_deepth:
                logging.info(u"超过指定的爬取深度，停止爬取.")
                break

            try:
                logging.info(u"获取url 内容 %s, 高度为 %s" % (cur_url, cur_deepth))
                res = requests.get(cur_url, timeout = self.crawl_timeout)

                # 存储符合正则的内容
                if not re.match(self.target_url, cur_url) is None:
                    self.save_file(cur_url, res.content)

                soup = BeautifulSoup(res.text, "html.parser")
                ans = soup.findAll("a", {"href": re.compile("^http|^/|^\.")})
                for i in ans:
                    if i["href"].startswith("http:") is True or i["href"].startswith("https:") is True:
                        new_url = i["href"]        
                    else:
                        new_url = urlparse.urljoin(cur_url, i["href"])
                    if new_url in self.visited:
                        logging.info(u"爬取的链接访问过 %s" % new_url)
                    else:
                        self.unvisited.put((new_url, cur_deepth + 1))
                        logging.info(u"入队链接 %s, 深度为 %d" % (new_url, cur_deepth + 1))
                        
                self.visited.append(cur_url)
            except requests.exceptions.Timeout:
                logging.error(u"[Timeout]爬取 url 超时 %s" % cur_url)
            except Exception as e:
                logging.error(u"爬取 url 失败 %s" % cur_url)
                logging.error(e)
            
            time.sleep(self.crawl_interval)

    def crawling_multithread(self):
        """
        多线程爬虫
        """
        ths = []
        for i in range(self.thread_count):
            th = Thread(target=self.crawling_single)
            logging.info(u"启动第 %d 个线程." % i)
            th.start()
            ths.append(th)
        for th in ths:
            th.join()


if __name__ == "__main__":
    seeds = "http://www.baidu.com"
    crawl_deepth = 1
    output_dir = "./output"
    target_url = ".*\.(gif|png|jpg|bmp)$"
    crawl_interval = 1
    crawl_timeout = 1
    thread_count = 2

    logging.basicConfig(level=logging.INFO)
    obj = MyCrawler(seeds, crawl_deepth, output_dir, target_url, crawl_interval, crawl_timeout, thread_count)
    # obj.crawling_single()
    obj.crawling_multithread()


