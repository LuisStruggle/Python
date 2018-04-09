#!/usr/bin/env python3

"""
错误和异常
"""
"""
NameError 尝试访问一个没有申明的变量
ZeroDivisionError 除数为0
SyntaxError 语法错误
IndexError 索引超出序列范围
KeyError 请求一个不存在的字典关键字
IOError 输入输出错误（比如你要读的文件不存在）
AttributeError 尝试访问未知的对象属性
"""
# NameError
"""
print(bar)

Traceback (most recent call last):
  File "D:\github\Python\error.py", line 16, in <module>
    print(bar)
NameError: name 'bar' is not defined
"""

# ZeroDivisionError
"""
print(1/0)

Traceback (most recent call last):
  File "D:\github\Python\error.py", line 26, in <module>
    print(1/0)
ZeroDivisionError: division by zero
"""

# SyntaxError
"""
for i in range(10)


SyntaxError: invalid syntax
"""

while 1:
    print("this is a division program.")
    c = input("input 'c' continue, otherwise logout:")
    if c == 'c':
        a = input("first number:")
        b = input("second number:")
        try:
            print(float(a)/float(b))
            print("*************************")
        except ZeroDivisionError:
            print("The second number can't be zero!")
            print("*************************")
        except ValueError:
            print("please input number.")
            print("************************")
    else:
        break

# 也可以这么写except (ZeroDivisionError, ValueError) as e: print(e)

# raise,是将异常的信息抛出

"""
在上面程序中，只处理了两个异常，还可能有更多的异常，如果要处理，怎么办？可以这
样： execpt:  或者 except Exception as e  ，后面什么参数也不写就好了。
"""

while 1:
    try:
        x = input("the first number:")
        y = input("the second number:")
        r = float(x)/float(y)
        print(r)
    except Exception as e:
        print(e)
        print("try again.")
    else:
        break

# else的作用，当try正确执行时，else才会执行。当try出错时，except执行，但是else不执行。

"""
finally  子句，一听这个名字，就感觉它是做善后工作的。的确如此，如果有了 finally  ，
不管前面执行的是 try  ，还是 except  ，最终都要执行它。因此一种说法是将 finally  用在可
能的异常后进行清理。
"""

# 异常结构体
"""
try:
    do something
except:
    do something
else:
    do something
finally
    do something
"""
# assert
"""
assert，翻译过来是“断言”之意。 assert  是一句等价于布尔真的判定，发生异常就意味着表
达式为假。
assert  的应用情景就有点像汉语的意思一样，当程序运行到某个节点的时候，就断定某个变
量的值必然是什么，或者对象必然拥有某个属性等，简单说就是断定什么东西必然是什么，
如果不是，就抛出异常。
"""
assert 1==1
assert 1==0


