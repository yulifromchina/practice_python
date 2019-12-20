#!/usr/bin/env python
# coding=utf-8
"""
实现日志格式和级别设置。
"""

import os
import logging
import logging.handlers


def init_log(log_path):
    """
    log_path: 日志路径
    """
    format="%(levelname)s: %(asctime)s: %(filename)s:%(lineno)d * %(thread)d %(message)s"
    datefmt="%m-%d %H:%M:%S"

    level=logging.INFO
    formatter = logging.Formatter(format, datefmt)
    logger = logging.getLogger()
    logger.setLevel(level)

    dir = os.path.dirname(log_path)
    if not os.path.isdir(dir):
        os.makedirs(dir)

    
    handler_0 = logging.handlers.TimedRotatingFileHandler(log_path + ".log", when='H', backupCount=10)
    handler_0.setLevel(logging.INFO)
    handler_0.setFormatter(formatter)
    logger.addHandler(handler_0)
    
    handler_1 = logging.handlers.TimedRotatingFileHandler(log_path + ".log.wf", when='H', backupCount=10)
    handler_1.setLevel(logging.ERROR)
    handler_1.setFormatter(formatter)
    logger.addHandler(handler_1)


if __name__ == "__main__":
    init_log("./log/mimi_spider")
    logging.info("测试 info")
    logging.warn("测试 warn")
    logging.error("测试 error")