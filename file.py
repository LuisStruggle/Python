#!/usr/bin/env python3

"""
文件
"""
import file

# 用dir()这种已经熟练的方法查看相关属性和方法。
print(dir(file))

f=open("study/study.txt") # open是内建的函数

print(dir(f))

for line in f:
    print(line)

# 创建文件
nf=open("write.txt","w")

nf.write("hello")

nf.close()

# 下面这种方式不需要显示的close文件流了
with open("write.txt","a") as f:
    f.write("\npython")

# 查看文件状态
import os

file_stat=os.stat("write.txt")

print(file_stat)

print(file_stat.st_ctime) # 文件创建时间

# 格式化时间
import time

print(time.localtime(file_stat.st_ctime))

# read演示
fr=open("read.txt")
content = fr.read()

print(content)

fr.close()

# readline演示

fr=open("read.txt")
print(fr.readline())

print(fr.readline())
fr.close()

# 循环读取readline
fr=open("read.txt")
while True:
    line=fr.readline()
    if not line:
        break
    print(line)
fr.close()

# readlines演示
fr=open("read.txt")

content=fr.readlines() # 返回的是一个列表

fr.close()
print(content[0])

# fileinput模块的使用
import fileinput

for line in fileinput.input("read.txt"):
    print(line)


# seek，让指针移动
fr=open("read.txt")
fr.readline()
fr.readline()
fr.seek(0) # 让指针回到开始位置
print(fr.readline())
 
print(fr.tell()) # 此时指针所在的位置，还可以用 tell()  来显示，返回的是字节位置
fr.close()

# 上下文管理器
read_file = open("read.txt")
write_file = open("write.txt", "w")
try:
    r = read_file.readlines()
    for line in r:
        write_file.write(line)
finally:
    read_file.close()
    write_file.close()

"""
如果你不知道“上下文管理器”，这样做无可厚非，可偏偏现在已经知道了，所以，从今以后这
样做就不是最优的了，因为它可以用“上下文管理器”写的更好。所以，用 with  语句改写之
后，就是很优雅的了。
"""
with open("read.txt") as read_file, open("write.txt", "w") as write_file:
    for line in read_file.readlines():
        write_file.write(line)

# 观察上下文执行
class ContextManagerOpenDemo:
    def __enter__(self):
        print("Starting the Manager.")
    def __exit__(self, *others):
        print("Exiting the Manager.")

with ContextManagerOpenDemo():
    print("In the Manager.")

class ContextManagerOpenDemo1:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    def __enter__(self):
        print("Starting the Manager.")
        self.open_file = open(self.filename, self.mode)
        return self.open_file
    def __exit__(self, *others):
        self.open_file.close()
        print("Exiting the Manager.")
with ContextManagerOpenDemo1("read.txt", 'r') as reader:
    print("In the Manager.")
    for line in reader:
        print(line)
