#! C:\Users\vyaroslavtsev\PycharmProjects\log_analysis
# -*- coding: utf-8 -*-
'''
    Web server log analysis
'''

import re
from collections import Counter

print 'Hello!' + '\n'


def read_log():
    '''
    Read file "access_log.log"
    :return: reading the whole file
    '''

    with open('access_log.log', 'r') as reader:
        return reader.read()


def parse_log(log):
    '''
    Parse log file
    :param log: result of read_log()
    :return: re.iterator with 2 groups: user and platform
    '''
    reg_log = re.finditer(r'(\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
                          r' - - \[\d\d/\w{3,10}/\d{4}\:\d{2}\:\d{2}\:\d{2}'
                          r' \+\d{4}\]).+(\"Mozilla/[45]\.0 \(.+\))', log)
    return reg_log


def get_user():
    '''
    Get 10 user with the most requests
    :return: list with nested tuple (user, quantity)
    '''

    ip_list = [user.group(1) for user in parse_log(LOG)]
    counter_user = Counter(ip_list).most_common(10)
    # for key in sorted(counter_ip, key=counter_ip.get, reverse=True):
    #     result.append((key, counter_ip[key]))
    # result = [(x, ip_list.count(x)) for x in ip_list]

    return counter_user


def get_platform():
    '''
    Get 5 the most popular platform
    :return: list with nested tuple (platform, quantity)
    '''

    platform_list = [plat.group(2) for plat in parse_log(LOG)]
    counter_platform = Counter(platform_list).most_common(5)

    return counter_platform


def main():
    print get_user(), '\n'
    print get_platform()


if __name__ == '__main__':
    LOG = read_log()
    main()


