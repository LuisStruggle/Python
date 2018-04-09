#!/usr/bin/env python3

"""
字典
"""

import copy

# 这里的字典，类似javascript中的json
a={"1":"liu","2":"zhang","3":"li"}
print(a)

# 添加(字典可以原地修改，即它是可变的。)
a["4"]="wang"
print(a)

# 利用元组建构字典
b = (["first", "Google"], ["second", "Yahoo"])
c=dict(b)
print(c)

# 或者用这样的方法
d = dict(name = "qiwsir", age = 42)
print(d)

# 跟上面的不同在于使用fromkeys
e = {}.fromkeys(("third", "forth"), "facebook")
print(e)

# 查找键对应的值
print(e["third"])

# 字典长度
print(len(e))

# 删除项
del e["third"]
print(e)

# 查找键是否存在
print("third" in e)

# 字符串格式化输出
print("你好 %(forth)s" % e)

# copy
f=e.copy() # 这种事浅拷贝，即只拷贝了基本类型，里面包含的其它数据类型，并没有重新拷贝一份，而是引用了原来的
print(f)

# 可以用id()这个方法查看内存地址

g = copy.deepcopy(e) # 这个是深拷贝，所有的数据结构都复制了一份
print(g)

# clear清空字典中所有元素的操作。
g.clear()
print(g)

# dict.get()就是要得到字典中某个键的值（获取的键不存在，不会报错，返回None）
print(e.get("forth"))

print(e.get("name",'liu')) #如果不能得到键"name"的值，就返回后面指定的值"liu"

# setdefault()的使用和get()类似，只是当键不存在时，将键存入字典
print(e.setdefault("forth"))
print(e.setdefault("name",'liu'))
print(e)

# items, keys, values
print(list(e.keys())) #得到键列表
print(list(e.values())) #得到值列表
for key in e.keys():
    print(key)

# pop, popitem
print(e.pop("name")) #删除指定键的元素，并返回值
print(e)

print(e.popitem())#随机删除一个元素，并返回键值元组
print(e)

# update
h={"lang":"python"}
i={"song":"I dreamed a dream"}
h.update(i)
print(h)

# update另一种方式
i.update([("name","liu"), ("sex","body")])
print(i)
