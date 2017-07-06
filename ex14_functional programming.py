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

def fn(x, y): # 把序列变成整数
	return x * 10 + y
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
		nonlocal point # 使用外层变量point，和global（全局变量）有区别
		if n == -1:
			point = 1 # 确定接下来的数全在小数点（.）后面
			return f
		if point == 0:
			return f * 10 + n
		else:
			point = point * 10
			return f + n / point
	return reduce(to_float, nums)
print('%.3f' % (str2float('123.451')))	 # 不指定小数点后的位数，则返回值是123.45100000000001
print(123.45 + 0.001) # 结果也是123.45100000000001

# filter() 把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
# 在list中，删掉偶数，只保留奇数
def is_odd(n):
	return n % 2 == 1 # 与2求余数，余数和1相等时表达式为真，为奇数
print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))) # 返回真则保留，假则丢弃
from collections import Iterable
from collections import Iterator
print(isinstance(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]), Iterable)) # 为真，可迭代
print(isinstance(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]), Iterator)) # filter()函数返回的是一个Iterator，是一个惰性序列，要filter()完成计算结果，需要用list()函数获得所有结果并返回list

# 把一个序列中的空字符串删掉
def not_empty(s):
	return s and s.strip() # strip()删除字符串中的空格，如果为strip('str'),删除指定的字符str
print(list(filter(not_empty, ['A', '', 'B', None, 'C', ' ']))) # 列表中存在空字符串，None，空格

# 用filter求素数，计算素数的一个方法是埃氏筛法，
# 先构造一个从3开始的奇数序列
def _odd_iter():
	n = 1
	while True:
		n = n + 2
		yield n
# 这是一个生成器，并且是一个无限序列
# 再定义一个筛选函数
def _not_divisible(n):
	return lambda x: x % n > 0 # 余数大于0，为奇数, 参数x 接收序列？？（为什么x接收序列），返回表达式的布尔值
# 最后定义一个生成器，不断返回下一个素数
def primes():
	yield 2
	it = _odd_iter() # 初始化序列，由于是生成器，还需迭代
	while True:
		n = next(it) # 使用next()迭代it，返回序列第一个数（下一次返回经过递归筛选的）		
		yield n
		it = filter(_not_divisible(n), it) # 构造经过筛选后的序列,此处开始递归，一层层递归筛选计算,
		# filter(_not_divisible(9),filter(_not_divisible(7),filter(_not_divisible(5),filter(_not_divisible(3),_odd_iter))))
		print('ddd')
for n in primes():
	if n < 13:
		print(n)
	else:
		break

# 练习 筛选出回数，从左到右读和从右到左读都是一样的数，例如12321，909
def is_palindrome(n): # 傻版本
	nums = str(n) # 将整数转化为字符串，以方便取位比较
	i = 0
	while i < len(nums)/2: # 折中比较
		if nums[i] == nums[len(nums)-1-i]: # 首尾逐个比较，如果是回数，折中比较完毕，退出循环
			i = i + 1
		else: # 如果不是回数，返回False
			return False 
	return True # 比较完毕，是回数，返回True
output = filter(is_palindrome, range(1, 10000))
print(list(output))		
def is_palindrome_v1(n): # 高级版本
	return n == int(str(n)[::-1]) # 切片[::-1]，切片——L[起始:结束:方向]，从右到左，每隔一个取，即将字符串化的str(n)倒序，再转换为整数与原数比较
output = filter(is_palindrome_v1, range(1, 10000))
print(list(output))

# sorted()排序函数
print(sorted([36, 5, -12, 9, -21])) # 按从小到大进行排列
# sorted()作为高阶函数，还可以接收一个key函数来实现自定义排序
print(sorted([36, 5, -12, 9, -21], key = abs)) # 如绝对值函数
# key指定的函数作用于list的每一个元素，并根据key函数返回的结果进行排序，再根据对应关系（映射关系）返回list最终结果
# 对比原始的list和经过key = abs处理过的list
# list = [36, 5, -12, 9, -21] --> keys = [36, 5, 12, 9, 21] --> sorted()函数按照keys排序结果[5, 9, 12, 21, 36] -->再按照对应关系返回list最终结果[5, 9, -12, -21, 36]
# 按字母ASCII排序，由于'Z'<'a',大写字母Z会排在小写字母a的前面
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower, reverse = True)) # 用key函数str.lower把字符串映射为忽略大小写再进行排序，最后反转reverse排序

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
	return t[0]
print(sorted(L, key = by_name))
def by_score(t):
	return t[1]
print(sorted(L, key = by_score))