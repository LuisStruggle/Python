#!/usr/bin/env python3

"""
列表
"""
import keyword

#定义了一个空列表，并把他赋值给变量a。
a = []
print(type(a))
print(bool(a))

# 列表中数据可以任意类型
b=[1,2,"汉武大帝"]
print(bool(b))

# 索引操作
print(b[0])
print(b[:2])
print(b[1:])

# 可以对列表元素做2次切片
print(b[2][1:2])

# 查找元素的位置
print(b.index(2))

# 按负号从右边编号
print(b[-1])

print(b[-2:])

# 反转列表(这是一种非常简单的方法，虽然我在写程序的时候常常使用，但是，我不是十分推荐，因为有时候让人感觉迷茫。)
print(b[::-1])

# 反转推荐这种方式
print(list(reversed(b)))

# 列表的长度
print(len(b))

# +，连接两个序列
c=[4,5]
print(b+c)

# *，重复元素
print(b*3)

# 判断某个元素是否包含在列表中
print("汉武大帝" in b)

# 按照元素的字典顺序进行比较的。
print(max(c))
print(min(c))

# 向列表中追加元素
c.append("nihao")
print(c)

# 另外一种追加方式
c[len(c):]=["hi"] 
print(c)

# 查看list相关方法
print(dir(list))

# 将一个列表追加到另一个列表
# 这就是列表的一个重要特征：列表是可以修改的。这种修改，不是复制一个新的，而是在原地进行修改。其实，append()对列表的操作也是如此，不妨用同样的方式看看。
d=[1,2]
e=[3,4]
d.extend(e)
print(d)

e[len(e):]=d
print(e)

# 用内建函数hasattr()判断一个字符串是否是可迭代的
print(hasattr(e,'__iter__'))
print(hasattr("abc",'__iter__'))

# 它把一个字符串"itdiffer"转化为['i', 't', 'd', 'i', 'f', 'f', 'e', 'r']，然后将这个列表作为参数，提供给extend()，并将列表中的元素塞入原来的列表中。
f=['python','java']
f.extend("itdiffer")
print(f)

# append是整建制地追加，extend是个体化扩编。
f.append(['1','2'])
print(f)

g=[1,2,3]
g.extend(['1','2'])
print(g)

# count()是一个帮着我们弄清楚列表中元素重复出现次数的方法。
print(f.count('f'))

# 在列表中插入一个元素
f.insert(0,"liu")
print(f)

# 在列表中删除一个元素(列表中没有的删除会报错)
# 如果正确删除，则删除第一个符合条件的对象。不会有任何反馈。没有消息就是好消息。它是对列表进行原地修改。
f.remove("liu")
print(f)

# if语句的首次使用
if "java" in f:
    f.remove("java")
    print(f)
else:
    print("'java' is not in f")

# list.pop的使用
i=f.pop() #pop参数为空，则默认删除最后一个元素，并有返回值
print(i)

j=f.pop(0) #删除指定元素
print(j)

# reverse转置
k=[1,2,3]
k.reverse()
print(k)

# 排序
l=['c','b','d','a']
l.sort() #正序
print(l)

l.sort(reverse=True) #逆序
print(l)

m=["python","java","c","pascal","basic"]
m.sort(key=len) #按字符长度排序
print(m)

# 查看系统中的保留字
print(keyword.kwlist)
