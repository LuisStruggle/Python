#!/usr/bin/env python3

"""
函数
"""
# 通常使小写字母来命名Python中的变量，也可以是用下划线连接的多个单词。比如：alpha，x，j，p_beta，这些都可以做为Python的变量。

# 函数的定义
def add_function(a,b):
    c=a+b
    print("a=",a)
    print("b=",b)
    return c

print(add_function(2,3))

print(add_function(b=10,a=5))

def test_function(x,y=2):
    print("x=",x)
    print("y=",y)
    return x+y

print(test_function(2))

print(test_function(x=2,y=5))

# 函数什么也不做，统统pass
def bar(): pass

# 斐波那契数列

def fibs(n):
    result=[0,1]
    for i in range(n-2):
        result.append(result[-2]+result[-1])
    return result

print(fibs(6))

# 上面的函数只返回了一个返回值（是一个列表），有时候需要返回多个，是以元组形式返回。
def my_fun():
    """
    多返回值演示,这块是函数文档说明
    """
    return 1,2,3
print(my_fun())

x,y,z=my_fun()

print(y)

print(my_fun.__doc__) # 打印出函数的文档

# 参数个数的不确定性
# 如果输入的参数个数不确定，其它参数全部通过 *hs  ，以元组的形式由hs收集起来
def hs(*canshu):
    print(canshu)

hs(1,2,3)
hs("a","b","c","d")

# **canshu 输出的是一个字典
def foo(**canshu):
    print(canshu)
# 如果用 **kargs  的形式收集值，会得到dict类型的数据，但是，需要在传值的时候说明“键”和“值”，因为在字典中是以键值对形式出现的。
foo(a=1,b=2,c=3)

# 先把要传的值放到元组中，赋值给一个变量 bars  ，然后用 add(*bars)  的方式，把值传到函数内。这有点像前面收集参数的逆过程。注意的是，元组中元素的个数，要跟函数所要求的变量个数一致。
bars=(2,3)
print(add_function(*bars))

# 赋默认值
def foo1(p1, p2=22, p3=33): #设置了两个参数p2, p3的默认值
    print("p1==>",p1)
    print("p2==>",p2)
    print("p3==>",p3)
foo1(11)
foo1(11, 222)
foo1(11, p2=122)
foo1(11, 222, 333)

# 递归
def fib(n):
    """
    This is Fibonacci by Recursion.
    """
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
if __name__ == "__main__":
    f = fib(10)
    print(f)

# 传递函数
def bar1():
    print("I am in bar()")

def foo2(func):
    func()

foo2(bar1)

# 嵌套函数
def foo3():
    def bar2():
        print("bar() is running")
    bar2() #显示调用内嵌函数
    print("foo() is running")
foo3()

# 装饰器的使用
def foo4(fun):
    def wrap():
        print("start")
        fun()
        print("end")
        print(fun.__name__)
    return wrap

@foo4 #装饰器本身是一个函数，将被装饰的类（后面会介绍这种东西）或者函数当作参数传递给装饰器函数
def bar3():
    print("I am in bar()")

bar3()

def bar4():
    print("I am in bar()")

f = foo4(bar4)
f()

# lambda泛型语言(lambda arg1, arg2, ...argN : expression using arguments)
g = lambda x, y: x + y
print(g(3, 4))

print((lambda x : x ** 2)(4)) #返回4的平方

# map()是python的一个内置函数，它的基本样式是 map(func,seq)
"""
func是一个函数，seq是一个序列对象。在执行的时候，序列对象中的每个元素，按照从左到
右的顺序，依次被取出来，塞入到func那个函数里面，并将func的返回值依次存到一个列表
中。
"""
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(map(lambda x: x+3, numbers)))

def sqr(x): return x**2

print(list(map(sqr,numbers)))

# reduce是横着逐个元素进行运算
from functools import reduce
print(reduce(lambda x,y: x+y,[1, 2, 3, 4, 5]))

# 练习
a = [3, 9, 8, 5, 2]
b = [1, 4, 9, 2, 6]

"""
zip(a,b) #复习一下zip，下面的方法中要用到
[(3, 1), (9, 4), (8, 9), (5, 2), (2, 6)]
"""

print(sum(x*y for x,y in zip(a,b))) #解析后直接求和

# 练习
scores={"zhangsan":90, "lisi":78,"wangermazi":39}

def sorted_score(scores):
    """
    对成绩从高到低排队.
    """
    score_lst = [(scores[k],k) for k in scores] # 键和值对调
    print(score_lst)
    sort_lst = sorted(score_lst, reverse=True) # 按键排序
    print(sort_lst)
    return [(i[1], i[0]) for i in sort_lst] # 最后再将键和值对调

print(sorted_score(scores))

def max_score(scores):
    """
    成绩最高的姓名和分数.
    """
    lst = sorted_score(scores) #引用分数排序的函数sorted_score
    max_score = lst[0][1]
    print(max_score)
    return [(i[0],i[1]) for i in lst if i[1]==max_score]

max_score(scores)
        
