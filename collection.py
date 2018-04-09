#!/usr/bin/env python3

"""
集合
"""

# 将字符串中的字符拆解成集合
a= set("python"*2) #集合中的元素不能重复
print(a)

# 在创建集合的时候，如果发现了重复的元素，就会过滤掉，剩下不重复的。
b=set([123,"google","face","book","facebook","book"])
print(b)

# 查看集合中的方法
print(dir(set))

# 除了用set()来创建集合。还可以使用{}的方式。
c = {"facebook",123}       #通过{}直接创建
print(c)

# add, update
d = set(["1","2"])
print(type(d))
print(d)
d.add("3") #添加一个元素
print(d)
e=set(["4","5"])
d.update(e) #这个方法的作用是用原有的集合自身和其它的什么东西构成的新集合更新原来的集合。
print(d)

# pop, remove, discard, clear
##print(d.pop())     #从set中任意选一个删除,并返回该值
##print(d)

d.remove("4") #set.remove(obj)中的obj,必须是set中的元素,否则就报错
print(d)

d.discard("5") #discard(obj)中的obj如果是集合中的元素,就删除；如果不是,就什么也不做
print(d)

d.clear()
print(d)

# 还有一种集合，不能在原处修改
f=frozenset("python"*2)
print(f)

# 元素要么属于某个集合，要么不属于
g=set(['h', 'o', 'n', 'p', 't', 'y'])
print("a" in g)
print("h" in g)

# 集合与集合的关系
h=set(['h', 'n'])
print(h==g)
print(h!=g)

print(h<g) #判断集合A是否是集合B的子集，可以使用A<B，返回true则是子集，否则不是

print(h.issubset(g)) #或者用这种方法，判断h是否是g的子集

print(g.issuperset(h)) #判断g是否是h的超集

# 表达式是A | B.也可使用函数A.union(B)，得到的结果就是两个集合并集，注意，这个结果是新生成的一个对象，不是将结合A扩充
i=set(['a','b','n'])
print(i|g)

print(i.union(g))

# 交集
print(i & g)
print(i.intersection(g))

# A相对B的差（补），即A相对B不同的部分元素
print(i-g)

print(i.difference(g))
# A、B的对称差集,即，去掉A,B的公共部分，剩下的A和B的合集
print(i.symmetric_difference(g))
