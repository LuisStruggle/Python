#!/usr/bin/env python3

"""
第三方库
"""

# 第三方库
import requests
print(dir(requests))

r = requests.get("http://www.baidu.com") # get请求，得到一个请求的实例
print(r.cookies)

print(r.headers)

print(r.encoding)

print(r.status_code)

# print(r.text) # 网页的内容
