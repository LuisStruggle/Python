#!/usr/bin/env python3

"""
运算符
"""

# 加法运算
print(10+20)

# 减法运算
print(10-20)

# 乘法运算
print(10*20)

# 除法运算
print(10/20)

# 取余运算
print(10%20)

# 幂 - 返回x的y次幂
print(10**2)

# 取整除 - 返回商的整数部分
print(10//20)

# 比较运算符
a=10
b=20
print(a==b)
print(a>b)
print(a<b)

# 布尔运算
# 逻辑“与”

"""
首先运算A，如果A的值是True，就计算B，并将B的结果返回做为最终结果，如果B是False，那么A and B的最终结果就是False，如果B的结果是True，那么A and B的结果就是True；
如果A的值是False ，就不计算B了，直接返回A and B的结果为False.
"""
print(a and b)

print(10<12 and 10>12)

# 逻辑“或”
print(10<12 or 10>12)

# 逻辑“非”
print(not(4>3))

# 循环语句
for i in [1,2,3,4,5]:
    print(i)

# 从帮助文档中可以看出，默认的end='\n'，如果不打算换行，可以在使用print()函数的时候，修改end这个参数的值。
for i in [1,2,3,4,5]:
    print(i, end=',')

# 从math里导入pow，e，pi
from math import pow, e, pi
print(pow(e,pi)) # 引入了math模块里面的pow,e,pi，pow()是一个乘方函数，e是那个欧拉数；pi就是π.

# from math import *         这种方式是导入math中所有的函数

# 赋值语句
x, y, z = 1, "python", ["hello", "world"]
print(x)
print(y)
print(z)

w = "baidu.com", "python"
print(w) # 原来是将右边的两个值装入了一个元组，然后将元组赋给了变量a。

# 两个数对调
a, b = b, a
print(a)
print(b)

# 另一种赋值方式
m = n = "I use python"
print(m,n)

# 检查m和n分别指向的对象是否是同一个，True说明是同一个。
print(m is n)

# 条件语句

"""
if m==n:
    print("true")

print("请输入任意一个整数数字：")
number = int(input())

if number == 10:
    print("您输入的数字是：{}".format(number))
    print("You are SMART.")
elif number > 10:
    print("您输入的数字是：{}".format(number))
    print("This number is more than 10.")
elif number < 10:
    print("您输入的数字是：{}".format(number))
    print("This number is less than 10.")
else:
    print("Are you a human?")
"""

# A = Y if X else Z

"""
如果X为真，那么就执行A=Y
如果X为假，就执行A=Z
"""
l=m if 2<3 else "liu"
print(l)

# 循环语句
hello = "python"
for i in hello:
    print(i)

# 通过索引遍历
for i in range(len(hello)): # range(len(hello)，就是range(5),也就是[0, 1, 2, 3, 4]，对应这"world"每个字母索引。这里应用了一个新的函数range()，关于它的用法，继续阅读，就能看到了。
    print(hello[i])

# for循环用于元组、字典
d = dict([("website", "www.baidu.com"), ("lang", "python"), ("author", "study")])
print(d)

for k in d:
    print(k)

for k,v in d.items():
    print(k+"---"+v)

# 判断一个对象是否可以迭代
import collections
print(isinstance(321, collections.Iterable))
print(isinstance([1,2,3], collections.Iterable))

# range(start,stop[, step])
print(list(range(9)))
print(list(range(0,9,1)))
print(list(range(0,9,2)))
print(list(range(0,-9,-2)))
print(list(range(0,-9,-1)))

# 找出被3整除的一百以内的整数
aliquot = []

for n in range(1,100):
    if n % 3 == 0:
        aliquot.append(n)
        
print(aliquot)

print(list(range(3, 100, 3)))

# 字符配对
e = "study"
f = "github"
print(list(zip(e,f)))

g = [1,2]
h = [3,4]
print(list(zip(g,h)))
for x,y in zip(g,h):
    print(x+y)

# 问题：有一个字典，myinfor = {"name":"study", "site":"baidu.com", "lang":"python"}，将这个字典变换成：infor = {"study":"name", "baidu.com":"site", "python":"lang"}
myinfor = {"name":"qiwsir", "site":"qiwsir.github.io", "lang":"python"}
infor = {}
for k,v in myinfor.items():
    infor[v]=k
print(infor)

print(dict(zip(myinfor.values(), myinfor.keys())))

# enumerate()也是内建函数。
week = ['monday', 'sunday', 'friday']
for (i, day) in enumerate(week):
    print(day+' is '+str(i))

# 到1到9的每个整数的平方，并且将结果放在列表中，打印出来。
power2 = []
for i in range(1, 10):
    power2.append(i*i)

print(power2)

# Python有一个非常强大的功能，就是列表解析，它这样使用：
squares = [x**2 for x in range(1, 10)]
print(squares)

# while的使用
cs = 1
while cs<4:
    print(cs)
    cs+=1

# while...else else即循环体结束后要做的事情
count = 0
while count < 5:
    print(count, " is  less than 5")
    count = count + 1
else:
    print(count, " is not less than 5")

# for...else

for n in range(99, 1, -1):
    print(n)

for n in range(99, 81, -1):
    print(n)

    
