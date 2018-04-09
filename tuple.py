#!/usr/bin/env python3

"""
元组
"""

# 打印结果，带有圆括号的对象，就是一种新的对象（或数据）类型：tuple（元组）。
a = 123, 'abc', ["come","here"]
print(a)

print(type(a)) #<class 'tuple'>

"""
元组是用圆括号括起来的，其中的元素之间用逗号隔开。（都是英文半角）
元组中的元素类型是任意的Python对象（数据）。
仅从前面那个例子，显而易见得出，元组是序列，这点上跟列表和字符串类似。
但元组中的元素不能更改，这点上跟列表不同，倒是跟str类似；它的元素又可以是任何类型的数据，这点上跟列表相同，但不同于字符串。
"""
print(a[1])
print(a[1:])
print(a[2][1])

# 但是这里要特别提醒，如果一个元组中只有一个元素的时候，应该在该元素后面加一个半角的英文逗号。
b=(3)
print(type(b)) #<class 'int'>
b=(3,)
print(type(b)) #<class 'tuple'>

# 分别用list()和tuple()能够实现两者的转化
c=list(a)
print(c)

d=tuple(c)
print(d)
