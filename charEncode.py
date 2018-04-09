#!/usr/bin/env python3

"""
字符编码
"""

import sys

# 打印出系统采用的编码方式
print(sys.getdefaultencoding())

# 在Python中，有两个内建函数，能够实现字符和对应数字之间的转换。
print(ord("Q"))
print(chr(81))
print(ord("刘"))
print(chr(21016))

# 查看方法描述
print(dir(str))
help(str.encode)
