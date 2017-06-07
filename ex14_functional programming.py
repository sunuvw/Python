# -*- coding: utf-8 -*-
# 函数式编程
#######################
# 高阶函数 Higher-order function
abs(-10) # 函数调用
abs # 函数本身也是变量，指向的是该函数
d = abs # 函数本身也可以赋值给变量，
# 传入函数，既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数称之为高阶函数
# 高阶函数
def add(x, y, f):
	return f(x) + f(y)
print(add(-5, 6, abs))

# python内建函数map()和reduce()
# map()接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Lterator返回
def f(x):
	return x * x
r = map(f, [1, 2, 3, 4]) 
print(list(r)) # 返回一个Iterator赋值给r，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list
# map()作为高阶函数，事实上它把运算规则抽象了，因此还可以计算任意复杂的函数，
map(str, [1, 2, 3, 4]) # 把list所有数字转为字符串

# reduce()的用法，reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce
def add(x, y):
	return x + y
print(reduce(add, [1, 3, 5, 7, 9]))

def fn(x, y):
	return x * 10 + y # 把序列变成整数
def char2num(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s] # 返回相应键的值
# print(char2num('2345')) # 会出现键值错误，因为会直接以'2345'这个键值寻找对应的值，肯定是没有的
print(reduce(fn, map(char2num, '13579'))) # 因为字符串'13579'是Iterable，map()函数会将其逐个迭代出，作为dict的键，返回一个Iterator

# 整理成一个函数
def str2int(s):
	def fn(x, y):
		return x * 10 + y
	def char2num(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	return reduce(fn, map(char2num, s))
print(str2int('2323'))

# 还可以用lambda函数进一步简化
def str2int_v1(s):
	return reduce(lambda x, y: x * 10 + y, map(char2num, s)) # lambda 参数: 表达式， 返回表达式的值
print(str2int_v1('3224'))

# 练习
# 把用户输入英文名字，变为首字母大写，其他字母小写 
def normalize(name):		
	return name[0].upper() + name[1:].lower() # 调用upper()大写字母转换函数和lower()小写字母转换函数
L1 = ['adam', 'LISA', 'bar']
print(list(map(normalize, L1))) # 用list()函数计算Iterator

name = 'scc'
print(name[0]) # 字符串可以直接按list下标使用元素

# 求积
def prod(L):
	return reduce(lambda x, y: x * y, L) 
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

# 将字符串转为float型
CHAR_TO_FLOAT = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': -1}
def str2float(s):	
	
	nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
	point = 0
	def to_float(f, n): # 开始接收迭代器nums从左到右开始的两个数值
		nonlocal point
		if n == -1:
			point = 1
			return f
		if point == 0:
			return f * 10 + n
		else:
			point = point * 10
			return f + n / point
	return reduce(to_float, nums)
print('%.3f' % (str2float('123.451')))	 # 不指定小数点后的位数，则返回值是123.45100000000001
print(123.45 + 0.001) # 结果也是123.45100000000001