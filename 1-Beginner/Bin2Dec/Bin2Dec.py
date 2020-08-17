#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    Bin2Dec.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.08.12   17:39
-------------------------------------------------------------------------------
   @Change:   2020.08.12
-------------------------------------------------------------------------------
"""

import math


def bin2dec(binary: str) -> int:
    length = len(binary)
    res = 0
    for index, bit in enumerate(binary):
        p = length - 1 - index
        res += int(int(bit) * math.pow(2, p))
    return res


def check(binary: str) -> bool:
    for i in binary:
        if int(i) > 1:
            return False
    return True


if __name__ == '__main__':
    while True:
        s = input("请输入二进制字符串:")
        if check(s):
            print(bin2dec(s))
        else:
            print("Input is invalid")
