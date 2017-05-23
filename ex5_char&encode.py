#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 上面第一行为了告诉linux，这是个python可执行程序，windows系统会忽略
# 上面第二行是为了让python解释器用utf-8的编码读取python代码，否则源代码中写的中文输出可能会有乱码
# 习题4：字符串和编码
########################
# 对于单个字符的编码，用ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
a = ord('A')
print(a)
z = ord('中')
print(z)
print(chr(a))
print(chr(z))


# 字符串类型为str，在内存中以Unicode编码,以字符为单位，一个字符对应若干个字节，如果要在网络上传输或保存到硬盘
# 就需要把str变为以字节为单位的bytes类型(一个字符对应一个字节)，用带b前缀的单引号或双引号表示
print('ABC'.encode('ascii')) # 将str类型的ABC用ascii编码为bytes
print('中文'.encode('utf-8')) # 将str类型的中文用utf-8编码为bytes
# '中文'.encode('ascii') # 中文编码的范围超过了ASCII编码的范围
print(b'ABC'.decode('ascii')) # 把bytes变为str，decode()方法
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

print(len('ABC')) # 计算字符数
print(len(b'ABC')) # len()计算字节数
print(len('ABC'.encode('ascii'))) # len()计算字节数
print(len('中文')) # 计算字符数
print(len('中文'.encode('utf-8')))# 将str类型的中文用utf-8编码为bytes,再计算字节数

# 在操作字符串时，我们经常遇到str 和 bytes的互相转换。为避免乱码问题，应当始终坚持使用UTF-8编码对str和bytes进行转换
# 在内存中字符串都是str类型

# 格式化字符串,%d 整数，%f 浮点数，%s 字符串，%x 十六进制整数
print('hello, %s' % 'world')
print('hi, %s, you have $%d' % ('scc', 199999))
print('%.3f' % 189) # 指定小数点位数
print('growth rate: %d %%' % 7) # 需要输出%，用%%转义

# 练习
s1 = 72
s2 = 85
r = (s2-s1)/s1 * 100
print('小明去年成绩是%d,今年成绩是%d,小明成绩提高了%.1f%%' %(s1,s2,r))