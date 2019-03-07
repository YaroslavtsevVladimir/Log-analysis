
# -*- coding: utf-8 -*-
""" Web server log analysis."""

import re
from collections import Counter


def read_log():
    """
    Read file "access_log.log"
    :return: reading the whole file
    """

    with open('access_log.log', 'r') as reader:
        return reader.read()


def parse_log(log):
    """
    Parse log file
    :param log: result of read_log()
    :return: re.iterator with 2 groups: user and platform
    """
    reg_log = re.finditer(r'(\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - - '
                          r'\[\d\d/\w{3,10}/\d{4}:\d{2}:\d{2}:\d{2} \+\d{4}\])'
                          r'.+(\"\w{1,35}/\d+\.\d+ \(.+\))', log)
    return reg_log


def get_user(reg):
    """
    Get 10 user with the most requests
    :return: list with nested tuple (user, quantity)
    """

    ip_list = [user.group(1) for user in reg]
    counter_user = Counter(ip_list).most_common(10)
    return counter_user


def get_platform(reg):
    """
    Get 5 the most popular platform
    :return: list with nested tuple (platform, quantity)
    """

    platform_list = [plat.group(2) for plat in reg]
    counter_platform = Counter(platform_list).most_common(5)
    return counter_platform


def main():
    log = read_log()
    parse = list(parse_log(log))
    print get_user(parse), '\n'
    print get_platform(parse)


if __name__ == '__main__':
    main()
