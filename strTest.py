#!/usr/bin/env python3

"""
字符串练习
"""
print("good good study, day day up")

print("py"+"thon")

# 将整数类型转换为字符类型str
print('aa'+str(12))

# '/'转义符
print("hello.I am qiwsir.\
My website is 'http://qiwsir.github.io'.")

# 字符串的输入
name=input("input your name:")

print(name)

# 原始字符串

print("c:\\news")

print(r"c:\news")

# 字符数组

lang="study python"

print(lang[1])

# 找到字符在在字符串中的下标
print(lang.index("p"))

# 截取字符串
print(lang[2:9])

# 得到从1号到最末尾的字符，这时最后那个需要不用写
print(lang[1:])

# 得到所有字符
print(lang[:])

# 得到从第一个到10号之前的字符
print(lang[:10])

# 字符串长度
print(len(lang))

# 查看字符串地址
print(id(lang))

# 查看某个字符串是否在另一个字符串内
print("dy1" in lang)

# 字符串，最大，最小值(ASCII编码)
print(max(lang))
print(min(lang))

# 查看字符ASCII码
print(ord('a'))

# 查看ASCII对应的字符
print(chr(97))

# 比较字符串
print("aa">"bb")
print("aa"<"bb")
print("aa"=="bb")

# 字符串中的“乘法”
print("_"*20)

# 占位符，格式化
str="I like {1} and {0}".format("python", "java")
print(str)

# 有10个字符那么长，并且左对齐
print("I like {0:10}".format("python","java"))
print("I like {1:10}".format("python","java"))
# 有10个字符那么长，并且右对齐
print("I like {0:>10}".format("python","java"))
print("I like {1:>10}".format("python","java"))
# 有10个字符那么长，并且居中对齐
print("I like {0:^10}".format("python","java"))
print("I like {1:^10}".format("python","java"))

# .2表示对于传入的字符串，截取前两个，并放到第一个位置，注意的是，在:后面和.号前面，没有任何数字，意思是该位置的长度自动适应即将放到该位置的字符串
print("I like {0:^10.2}".format("python","java"))
print("I like {1:^10.2}".format("python","java"))

# 向format()中，除了能够传入字符串，还可以传入数字（包括整数和浮点数），而且也能有各种花样。+
# {0:d}表示在第一个位置放一个整数；{1:f}表示在第二个位置放一个浮点数，那么浮点数的小数位数，是默认的。
print("She is {0:d} years old and the breast is {1:f}cm".format(28, 90.1415926))

# {0:4d}表示第一个位置的长度是4个字符，并且默认状态下，填充到该位置的整数是右对齐。
# {1:6.2f}表示第二个位置的长度使6个字符，并且填充到该位置的浮点数要保留两位小数，默认也是右对齐。
print("She is {0:4d} years old and the breast is {1:6.2f}cm".format(28, 90.1415926))

# {0:04d}和{1:06.2f}与前述例子不同的在于在声明位置长度的数字前面多了0，其含义是在数字前面，如果位数不足，则补0。
print("She is {0:04d} years old and the breast is {1:06.2f}cm".format(28, 90.1415926))

# 以上的输出方式中，我们只讨论了format(*args, **kwargs)中的*args部分。还有另外一种方式，则是与**kwargs有关的（关于这两种参数的含义，本教程后面有专门介绍）。
print("I like {lang} and {name}".format(lang="python", name="java"))

# 一种被称为“字典格式化”，这里仅仅列一个例子
data = {"name":"liu", "age":28}
print("{name} is {age}".format(**data))

# 字符串全是字母，应该返回True
# 字符串含非字母，返回False
print("python".isalpha())
print("2python".isalpha())

# 分割字符串
print("I LOVE PYTHON".split(" "))

# S.strip()：去掉字符串的左右空格；S.lstrip()：去掉字符串的左边空格；S.rstrip()：去掉字符串的右边空格
print(" liuyang ")
print(" liuyang ".strip())

# S.upper()：S中的字母大写；S.lower()：S中的字母小写；S.capitalize()：首字母大写；S.isupper()：S中的字母是否全是大写；S.islower()：S中的字母是否全是小写；S.istitle()：S中字符串中所有的单词拼写首字母是否为大写，且其他字母为小写（标题都这么写）
a = "This is a Book"
print(a.istitle())
b = a.title()     #这样就把所有单词的第一个字母转化为大写
print(b)
print(b.istitle())       #判断每个单词的第一个字母是否为大写

# 用字符串的.join()方法拼接字符串
c="I LOVE PYTHON"
d=c.split(" ")
print(".".join(d))
