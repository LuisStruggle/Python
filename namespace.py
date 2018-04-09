#!/usr/bin/env python3

"""
类
"""
x = 2
def funcx():
    global x #注意声明的是x为全局变量，否则x是局部变量
    x = 9
    print("this x is in the funcx:-->",x)
funcx()
print("--------------------------")
print("this x is out of funcx:-->",x)


import this

# 查询本地命名空间

def foo(num,str):
    name = "qiwsir"
    print(locals())

foo(221,"qiwsir.github.io")

# 类

class liu:
    def __init__(self, str):
        self.str = str
    
    def test(self):
        print(self.str)

aa=liu("hello") # 创建类对象，并初始化
aa.test()

print(liu.__name__) # 类名
print(liu.__doc__) # 类文档
print(liu.__base__) # 类的所有父类
print(liu.__dict__) # 以字典形式显示类的所有属性
print(liu.__module__) # 类所在的模块

# 继承(如果子类中的方法或属性覆盖了父类（即与父类同名），那么就不在继承父类的该方法或者属性。)
class Person:
    def __init__(self, name):
        self.name = name
        
    def height(self, m):        
        h = dict((["height", m],))
        return h
    
    def age(self, n):
        b = dict((["age", n],))
        return b
    
class Girl(Person):
    def get_name(self):
        return self.name

if __name__ == "__main__":
    be = Girl("zhangsan")
    print(be.get_name())
    print(be.height(160))
    print(be.age(25))

# 多继承
class K1(object): #Python 3: class K1:
    def foo(self):
        print("K1-foo")
    
class K2(object):
    def foo(self):
        print("K2-foo")

    def bar(self):
        print("K2-bar")

class J1(K1, K2):
    pass

class J2(K1, K2):
    def bar(self):
        print("J2-bar")

class C(J1, J2):
    pass
if __name__ == "__main__":
    print(C.__mro__)
    m = C()
    m.foo()
    m.bar()

"""
代码中的 print C.__mro__  是要打印出类的继承顺序。从上面清晰看出来了。如果要执
行 foo()  方法，首先看 J1  ，没有，看 J2  ，还没有，看 J1  里面的 K1  ，有了，即
C==>J1==>J2==>K1； bar()  也是按照这个顺序，在 J2  中就找到了一个。
这种对继承属性和方法搜索的顺序称之为“广度优先”。
"""

# 多态
tj=[1,2,4,3,5,3].count(3) # 统计对象中，某个元素出现的次数
# tj="woshishui".count(s)
print(tj)

f = lambda x,y:x+y
print(f(2,3))
print(f("zhang","san"))

print(repr([1,2,3])) # repr针对不同的对象，返回对应的字符串
print(repr(1))
print(repr({"lang":"python"}))

"""
以上，就体现了“多态”——同一种行为具有不同表现形式和形态的能力，换一种说法，就是对
象多种表现形式的体现。
"""

# 私有化
"""
Python中私有化的方法也比较简单，就是在准备私有化的属性（包括方法、数据）名字前面
加双下划线
"""
class ProtectMe:
    def __init__(self):
        self.me = "zhang"
        self.__name = "san"
    def __python(self):
        print("I love Python.")
    def code(self):
        print("Which language do you like?")
        self.__python()
if __name__ == "__main__":
    p = ProtectMe()
    print(p.me)
    p.code()
    # print(p.__name)

# 判断一个对象，是否是另一个对象的实例
class C1: pass
class C2: pass
a = C1()
b = C2()

print(isinstance(a, C1))
print(isinstance(a, C2))


# 定制类（输出分数）
from fractions import Fraction
m, n = Fraction(1, 3), Fraction(1, 2)
print(m + n)

# 属性拦截，当访问的属性不存在时
class A:
    def __getattr__(self, name):
        print("You use getattr")
    def __setattr__(self, name, value):
        print("You use setattr")
        self.__dict__[name] = value

a=A()
a.x # 访问不存在属性，__getattr__起作用

a.x = 7

"""
给对象的属性赋值时候，调用了 __setattr__(self, name, value)  方法，这个方法中有一
句 self.__dict__[name] = value  ，通过这个语句，就将属性和数据保存到了对象
的 __dict__  中
"""

# 迭代器
"""
the interator as range()
"""
class MyRange:
    def __init__(self, n):
        self.i = 1
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        if self.i <= self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()
if __name__ == "__main__":
    x = MyRange(7)
    print([i for i in x])

# 生成器(generator)
my_tup = (x**x for x in range(4))
print(my_tup)

# 定义一个生成器
def g():
    yield 0
    yield 1
    yield 2

print(type(g()))
print(dir(g()))
for x in g():
    print(x)
