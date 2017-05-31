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
L1 =[s.lower() for s in L if isinstance(s, str)]
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
print(fib1(6))
# generator和函数的执行流程不一样，函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()或用for循环的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
for n in fib1(6):
	print(n)
# 但是用for循环调用generator时，发现获取不到generator的return语句的返回值，如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
g = fib1(7)
while True:
	try:
		x = next(g)
		print('g:', x)
	except StopIteration as e:
		print('Generator return value:', e.value)
		break
		