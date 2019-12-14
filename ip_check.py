#!/usr/bin/env python3
"""
检查IP地址是否合法
"""


def ip_check(ip_addr):
    """
    检查 IP 地址是否合法的函数
    Attrs:
        ip_addr: ip 地址
    Returns:
        True/False:  ip 地址合法/不合法
    """
    ip_addr = ip_addr.strip().split('.')
    if len(ip_addr) != 4:
        return False
    try:
        ip_addr[0] = int(ip_addr[0])
        ip_addr[1] = int(ip_addr[1]) 
        ip_addr[2] = int(ip_addr[2]) 
        ip_addr[3] = int(ip_addr[3]) 
    except Exception as e:
        return False

    if ((ip_addr[0] >= 1 and ip_addr[0] <= 255) and 
        (ip_addr[1] >= 0 and ip_addr[1] <= 255) and
        (ip_addr[2] >= 0 and ip_addr[2] <= 255) and
        (ip_addr[3] >= 0 and ip_addr[3] <= 255)):
        return True
    return False


if __name__ == "__main__":
    ip_addr = " 1.1.1.1 "
    if ip_check(ip_addr) is True:
        print("IP 地址合法")