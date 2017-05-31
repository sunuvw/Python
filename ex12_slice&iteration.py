# -*- coding: utf-8 -*-
#习题：高级特性
#######################
# 切片（slice）
L = ['Scc', 'Michael', 'Sarah', 'Tracy', 'Bob']
r = []
for i in list(range(1,3)):
	r.append(L[i])
print(r)
# 对于这种经常取指定索引范围的操作，用循环十分繁琐，因此，Python提供了切片（slice），能大大简化这种操作
L[0:3] # 对应上面的问题，取前3个元素（0,1,2）不包括3，用这一行代码就可以完成切片
L[:3] # 简写,缺省从索引0开始
print(L[1:3]) # 从索引1开始取1,2两个元素
print(L[-2:-1]) # 倒数第一个元素的索引是-1，这样写不包含-1,仅输出-2
print(L[-2:]) # 这样写输出包含-1,-2
L = list(range(100))
print(L[:10:2]) # 前10个数，每2个取一个
print(L[::5]) # 所有数，每5个取一个
print(L[:]) # 原样复制一个list
# tuple也是一种list，唯一区别是tuple不可变，因此，tuple也可以用切片操作，只是操作的结果仍是tuple
t = (0, 1, 2, 3, 4)
print(t[:3])
# 字符串'xxxxx'也可以看成是一种list，每个元素就是一个字符，因此，字符也可以用切片操作
print('ABCDEFG'[:3])
print('ABCDEFG'[::2])

# 迭代（iteration） 通过迭（叠）加带入的方式遍历，比如说，可以通过for循环来遍历list或tuple，以上一次结果作为下一次的初始值
# 对于很多没有下标的数据类型，python都可以迭代
# 如 dict
d = {'a':1, 'b': 2, 'c': 3}
for key in d:
	print(key) # 因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样
# 默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values(),如果要同时迭代key和value，可以用for k, v in d.items()
for value in d.values():
	print(value)
for k, v in d.items():
	print(k, v)
for ch in 'ABCD': # 字符串也是可以迭代的
	print(ch)
# 判断一个对象是否为可迭代对象
# 通过collections模块的iterable类型判断
from collections import Iterable
isinstance('abc', Iterable) # 判断'abc'的类型是否为Iterable（可迭代）类型
# python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i, value in enumerate(['A', 'B', 'C']): # 0-'A'
	print(i, value)
# for循环里，还可以同时引用两个变量
for x, y in [(1, 2), (3, 4), (5, 6)]:
	print(x, y)




