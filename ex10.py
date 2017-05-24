# -*- coding: utf-8 -*-
#习题：函数
######################
# 调用函数，需要知道函数名称和参数，函数名其实就是指向一个函数对象的引用，可以把函数名赋给一个变量，相当于给这个函数起了个“别名”
n1 = 255
n2 = 1000
print("n1 hex is %s; n2 hex is %s." % (hex(n1), hex(n2))) # 利用hex()将n1、n2转换成十六进制
print(str(hex(n1)),str(hex(n2)))
# 可以查看内置函数的在线帮助文档https://docs.python.org/3/library/functions.html 
# 常用函数 abs(), max(), int(), float(), str(), bool()

# 定义函数，使用def语句，一次写出函数名、括号、括号中的参数和冒号：，在缩进块中编写函数体，函数的返回值用return语句返回
from abs_test import out_abs
print(out_abs(-111))

# 空函数 ，如果想定义一个什么事也不做的空函数，可以用pass语句,pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass
def nop():
	pass
#参数检查
def my_abs1(x):
	if not isinstance(x,(int, float)): # 参数类型检查，用isinstance()函数检查
		raise TypeError("bad operand type")
	if x >= 0:
		return x  # 函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕
	else:
		return -x # 如果没有return语句，函数执行完毕后也会返回结果，只是结果为None，return None 可以简写为return		
# my_abs1('A')

# 返回多个值
import math # 导入math包，并允许后续代码引用math包里的sin、cos等函数
def move(x, y, step, angle = 0): # angle 为默认参数
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny 
# 返回多个值，其实就是返回一个tuple，可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值	
x, y = move(100, 200, 11, math.pi / 6)
r = move(100, 200, 11, math.pi / 6)
print(x, y)
print(r)

# 练习	
# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：ax^2 + bx + c = 0的两个解。
def	quadratic(a, b, c):
	x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
	x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
	return x1, x2
x = quadratic(2, 3, 1)
print("x1 is %.2f; x2 is %.2f" % x)
	
# 函数的参数，位置参数、默认参数、可变参数
# 位置参数
def power(x, n): # 两个位置参数
	s = 1
	while n > 0:
		s = s * x
		n = n - 1
	return s
print(power(3, 3)) # 3的3次方
# 默认参数
def power1(x, n = 2): # 第二个参数设定为默认参数，值为2
	s = 1
	while n > 0:
		s = s * x
		n = n - 1
	return s
print(power(3)) # 如果第二参数不指定，将使用默认参数的值2
# 设置默认参数时，需要注意
# 一是必选参数在前，默认参数在后，否则Python的解释器会报错（因为解释器将分不清必选参数和默认参数）
# 二是如何设置默认参数：当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面，变化小的参数就可以作为默认参数
# 只有与默认参数不符的才需要额外提供参数，可见，默认参数降低了函数调用的难度，而一旦需要更复杂调用时，又可以传递更多的参数来实现，无论是简单调用还是复杂调用，函数只需要定义一个
def enroll(name, gender, age = 6, city = 'Beijing'):
	print('name', name)
	print('gender', gender)



