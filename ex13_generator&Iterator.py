# -*- coding: utf-8 -*-
#习题：高级特性
#######################
# 列表生成式
L = []
for x in range(1, 10):
	L.append(x * x)

# 使用列表生成式，改写如下
print([x * x for x in range(1,10)])

# 使用两层循环
print([m + n for m in 'ABC' for n in 'XYZ'])

# 运用列表生成式，可以写出非常简洁的代码。如 列出当前目录下的所有文件和目录名
import os
d_1 = [d_1 for d_1 in os.listdir('.')]
print(d_1)

# 列表生成式也可以使用两个变量来生产list
d_2 = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in d_2.items()])

L = ['Hello', 'World', 18, 'Apple', None]
L1 =[s.lower() for s in L if isinstance(s, str)] # isinstance() 判断对象是否是已知类型
print (L1)

# 生成器。不必创建完整的list，通过在循环过程中不断推算出后续的元素，节省大量的空间，这种一边循环一边计算的机制，称为生成器：generator(保存的是算法)
#　创建generator的第一种方法，把一个列表生产式的[]改成(),就创建了一个generator
L = [ x * x for x in range(10)]
print(L)
g = (x * x for x in range(10))
print(g)
# print(next(g))
n = 0
# 用while循环和next()函数计算下一个元素的值
# while n < 10:
	# print(next(g)) # 每次调用next(g),就计算出g的下一个元素的值，直到计算出最后一个元素时，抛出StopIteration的错误
	# n = n + 1
# 因为generator对象也是可迭代的，可以用for循环计算下一个元素值
for i in g:
	print(i)

# 费波拉契数列
def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		print(b)
		a, b = b, a + b # t = (b, a + b),t是一个tuple，值是不变的即(1, 0 + 1)，a = t[0], b = t[1]一条语句=号右边先计算再赋值给左边变量
		n = n + 1
	return 'done'
fib(6)
# fib函数实际上是定义了费波拉契数列的推算规则，可以从第一个元素开始，推算出后续任意的元素，这种逻辑非常类似generator
# 变成generator，只需要把print(b)改为yield b
def fib1(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b # 如果一个函数定义中包含yield关键字，它就是一个generator
		a, b = b, a + b
		n = n + 1
	return 'done'
# generator和函数的执行流程不一样，函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()或用for循环的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
for n in fib1(6):
	print(n)
#　python的for循环本质上就是通过不断调用next()函数实现的
# 完全等价于
f = fib1(6)
while True:
	try:
		# 获得下一个值
		x = next(f)
		print('hhh', x)
	except StopIteration:  
		# except语句遇到StopIteration就退出循环
		break
def odd():
	print("step 1")
	yield 1
	print("step 2")
	yield 2

o = odd() # 创建生成器
next(o)
next(o)

# 下面的调用方式得出的结果和上面调用的结果不一样？应该是因为创建了两次生成器
# next(odd()) # 创建生成器
# next(odd()) #　再次创建生成器，导致结果为初始值


# 但是用for循环调用generator时，发现获取不到generator的return语句的返回值，如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
g = fib1(7)
while True:
	try:
		x = next(g)
		print('g:', x)
	except StopIteration as e:
		print('Generator return value:', e.value)
		break

# 练习 杨辉三角（不会做）
def triangles():
	L = [1]
	while True:
		yield L
		L.append(0) # 补一个0，对初始列表[1]补全为[1, 0]，根据杨辉三角规律，0隐式存在，计算出新列表第一个元素；每次循环列表都增加一个元素
		L = [L[i-1]+L[i] for i in range(len(L))] # 通过列表生成式创建列表，根据len(L)长度i确定元素个数，并定位操作元素计算
		# L[i-1] + L[i],新列表的第一个元素由旧列表的最后一个元素与第一个元素之和得出，以此类推
n = 0
for i in triangles():
	print(i)
	n = n + 1
	if n == 10:
		break
		

# 迭代器 Iterator
# 可以直接作用于for循环的数据类型有：
# 1、一类是集合数据类型，如：list、tuple、dict、set(无序，非重复元素集合)、str等
# 2、一类是generator（生成器），包括生成器和带yield的generator function（生成器函数）
# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器Iterator
# 生成器都是Iterator对象，但list、dict、str、set、tuple虽然是Iterable，却不是Iterator
# 可以使用isinstance()判断一个对象是否是Iterator对象
from collections import Iterable
from collections import Iterator
print(isinstance((x for x in range(10)), Iterable)) # 可迭代对象
print(isinstance((x for x in range(10)), Iterator)) # 是迭代器
print(isinstance([1, 2], Iterator)) # 不是迭代器
print(isinstance([1, 2], Iterable)) # 可迭代对象
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数
print(isinstance((iter([1, 2])), Iterator))
# Iterator对象表示的是一个数据流，可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据
#　所以Iterator的计算是惰性的，只有在需要返回下一个数据时他才会计算，Iterator甚至可以表示一个无限大的数据流，例如全体自然数，而使用list是永远不可能存储全体自然数的