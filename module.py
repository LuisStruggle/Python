#!/usr/bin/env python3

"""
模块和标准库
"""
"""
如果要作为程序执行，则 __name__ == "__main__"  ；如果作为模块引入，则 pm.__name__ ==
"pm"  ，即属性 __name__  的值是模块名称。
用这种方式就可以区分是执行程序还是作为模块引入了。
在一般情况下，如果仅仅是用作模块引入，不必写 if __name__ == "__main__"  。
"""
import sys
sys.path.append("hello.py")
import hello
print(hello.my_name)

# 查看系统中模块的位置
import pprint
pprint.pprint(sys.path)

# 让字典对象格式化输出
zfc = {"zhang":"san", "li":"si", "wang":"wu", "zhao":"liu","hello":"nihao","hei":"jiayou"}
pprint.pprint(zfc)

# from pprint import pprint(意思是从 pprint  模块中之将 pprint()  引入，之后就可以直接使用它了。)
# from pprint import *(这就将pprint模块中的一切都引入了，于是可以像上面那样直接使用模块中的所有可用的内容。)
# 如果很明确使用模块中的哪些方法或属性，那么使用类似 from modulename import name1, name2, name3...  也未尝不可。减少内存开销
print([ m for m in dir(pprint) if not m.startswith('_') ])
print(pprint.__all__)

"""
当我们使用 from pprint import *  的时候，就是将 __all__  里面的方法引入，如果没有
这个，就会将其它所有属性、方法等引入，包括那些以双划线或者单划线开头的变量、函
数，事实上这些东西很少在引入模块时被使用。
"""
# 查询模块的位置
print(pprint.__file__)

# 退出程序sys.exit()
"""
for i in range(10):
    if i == 5:
        sys.exit("我退出了")
    else:
        print(i)
"""

"""
在大多数函数中会用到return，其含义是终止当前的函数，并向调用函数的位置返回相应值
（如果没有就是None）。但是 sys.exit()  的含义是退出当前程序——不仅仅是函数，并发
起 SystemExit  异常。这就是两者的区别了。

如果使用 sys.exit(0)  表示正常退出。若需要在退出的时候有一个对人友好的提示，可以
用 sys.exit("I wet out at here.")  ，那么字符串信息就被打印出来。
"""

# sys.stdout.write(str(i) + '\n') 等价于 sys.print(i)

"""
f = open("stdout.txt","w")
sys.stdout = f # 当 sys.stdout = f  之后，就意味着将输出目的地转到了打开（建立）的文件中，如果使用 print  ，即将内容输出到这个文件中，在控制台并无显现。
print("Learn Python: From Beginner to Master")
f.close()
"""

# copy模块
import copy
print(copy.__all__)

# os模块的使用
import os
print(dir(os))

# 修改文件名
# os.rename("write.txt", "newwrite.txt")

# remove,删除一个文件
# os.remove("test.txt")

# 文件和目录属性
print(os.stat("newwrite.txt"))

import time
print(time.ctime(os.stat("newwrite.txt")[8]))
print("-------------------------------------------------")

# 执行command
command="dir "+os.getcwd()
print(command)
print(os.system(command))

# 用该模块打开浏览器
"""
import webbrowser
webbrowser.open("http://www.baidu.com")
"""

# heapq  中的heap是堆，q就是queue（队列）的缩写。堆按二叉树排序
import heapq
print(heapq.__all__)
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 9)
heapq.heappush(heap, 2)
heapq.heappush(heap, 4)
heapq.heappush(heap, 0)
heapq.heappush(heap, 8)
print(heap)

# heappop(heap)：删除最小元素
print(heapq.heappop(heap))
print(heap)

# heapify()：将列表转换为堆
hl = [2, 4, 6, 8, 9, 0, 1, 5, 3]
heapq.heapify(hl)
print(hl)

# heapreplace()是 heappop()  和 heappush()  的联合，也就是删除一个，同时加入一个。
print("-------------------------------------------------")
# 在列表的前后增加元素
lst = [1, 2, 3]
lst.append(4)
print(lst)
nl = [7]
nl.extend(lst)
print(nl)

# deque的使用
from collections import deque
lst = [1, 2, 3, 4]
qlst = deque(lst)
qlst.append(5) # 从右边增加一个元素
print(qlst)
qlst.appendleft(7) # 从左边增加一个元素
print(qlst)
qlst.pop() # 从右边删除
print(qlst)
qlst.popleft() # 从左边删除
print(qlst)
print("-------------------------------------------------")
# calendar的使用
import calendar
cal = calendar.month(2016,3)
print(cal)
year = calendar.calendar(2017)
print(year)

# isleap(year)判断是否为闰年，是则返回true，否则false.
print(calendar.isleap(2017))
print(calendar.isleap(2016))

# leapdays(y1, y2)返回在y1，y2两年之间的闰年总数，包括y1，但不包括y2，这有点如同序列的切片一样。
print(calendar.leapdays(2000, 2004))

# weekday(year,month,day)输入年月日，知道该日是星期几（注意，返回值依然按照从0到6依次对应星期一到星期六）。
print(calendar.weekday(2018,3,12))
print("-------------------------------------------------")
# time()
print(time.time()) # 获取当前时间
print(time.localtime()) # 获取当前时间，格式化
print(time.asctime())

# strptime()  的作用是将字符串转化为时间元组。请注意的是，其参数要指定两个，一个是时间字符串，另外一个是时间字符串所对应的格式，格式符号用上表中的。
today = time.strftime("%y/%m/%d")
print(today)

# timedelta类主要用来做时间的运算
import datetime
now = datetime.datetime.now()
print(now)
b = now + datetime.timedelta(hours=5) # 加5小时
print(b)
c = now + datetime.timedelta(weeks=2) # 加两周
print(c)

print("-------------------------------------------------")
# urllib  模块用于读取来自网上（服务器上）的数据
import urllib.request
baidu = urllib.request.urlopen("https://my.bjut.edu.cn/")
# print(baidu.read())

print(dir(urllib.request))

# 完整案例
import urllib.parse
url = 'https://my.bjut.edu.cn/'
# values = {}
# data = urllib.parse.urlencode(values) # 编码
# req = urllib.request.Request(url, data) # 发送请求同时传data表单
req = urllib.request.Request(url) # 发送请求同时传data表单
response = urllib.request.urlopen(req) #接受反馈的信息
the_page = response.read() #读取反馈的内容
print(the_page)

print("-------------------------------------------------")
# xml解析
import xml.etree.ElementTree as ET
tree = ET.ElementTree(file="xmljx.xml")
print(tree)
root = tree.getroot() #获得根
print(root)
for child in root:
     print(child.tag, child.attrib)

for ele in tree.iterfind("book/title"):
    print(ele.text)


# 利用 findall()  方法，也可以是实现查找功能：
for ele in tree.findall("book"):
    title = ele.find('title').text
    price = ele.find('price').text
    lang = ele.find('title').attrib
    print(title, price, lang)

"""
# 删除节点
print(root[1].tag)
del root[1]

outpath = os.getcwd()
file = outpath + "\\xmljx.xml"
tree.write(file)

# 修改
for price in root.iter("price"): #每本上涨7元，并且增加属性标记
    new_price = float(price.text) + 7
    price.text = str(new_price)
    price.set("updated","up")

tree.write(file)
"""

print("-------------------------------------------------")
# JSON
import json
print(json.__all__)

data = [{"name":"qiwsir", "lang":("python", "english"), "age":40}]
data_json = json.dumps(data) # 编码
print(data_json)

"""
encoding的操作是比较简单的，请注意观察 data  和 data_json  的不同——lang的值从元组变
成了列表，还有不同：
type(data_json)
<type 'str'>
type(data)
<type 'list'>
"""

data_j = json.dumps(data, sort_keys=True, indent=2) # 解码
print(data_j)
