#!/usr/bin/env python3

"""
迭代
"""
# 循环
lst = ['q', 'i', 'w', 's', 'i', 'r']
for i in lst:
    print(i,end=" ")

# 迭代
lst_iter = iter(lst)

print("\n"+lst_iter.__next__())

print(lst_iter.__next__())

print(type(lst_iter)) # 查看对象类型

# 读取文件
f=open("read.txt")

print(f.__next__())

print(f.__next__())

# 练习1

raw=[1,2,3,4,5]

n=raw.pop(0)
raw.append(n)

print(raw)
