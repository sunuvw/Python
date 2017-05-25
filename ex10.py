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
print(power1(3)) # 如果第二参数不指定，将使用默认参数的值2
# 设置默认参数时，需要注意
# 一是必选参数在前，默认参数在后，否则Python的解释器会报错（因为解释器将分不清必选参数和默认参数）
# 二是如何设置默认参数：当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面，变化小的参数就可以作为默认参数
# 只有与默认参数不符的才需要额外提供参数，可见，默认参数降低了函数调用的难度，而一旦需要更复杂调用时，又可以传递更多的参数来实现，无论是简单调用还是复杂调用，函数只需要定义一个
def enroll(name, gender, age = 6, city = 'Beijing'):
	print('name: ', name)
	print('gender: ', gender)
	print('age: ', age)
	print('city: ', city)
enroll("scc", "A", 9) # 按顺序使用默认参数值
enroll("scc", "A",city = 'Hefei') # 也可以不按顺序，但需把参数名写上

# 默认参数存在的坑
def add_end(L = []):
	L.append("END")
	return L
print(add_end([1, 2, 3]))
L = [5, 5,]
# Python函数在定义的时候，默认参数L的值就被计算出来了，即L的内存地址，因为默认参数也是一个变量，它指向对象[]
# 每次调用该函数，如果改变了L的内容，则下次调用时，也没有指定参数值，默认参数的内容就变成了调用时改变的内容，而不再是函数定义时的[]
print(add_end()) # 没有指定参数，使用默认参数值，函数执行完毕后，def add_end(L = []):中L的值已经变成L = ["END"]即def add_end(L = ["END"]):
print(add_end()) # 函数返回值已经变成["END", "END"]
# 所以默认参数必须指向不变对象！
# 改造上面的例子，可以用None这个不变对象来实现
def add_end(L = None):
	if L is None:
		L = []
	L.append("END")
	return L
# 为减少修改数据导致的错误，此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题没有，在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象

# 可变参数，在参数前加*号，就是传入的参数个数是可变的，可以是多个或0个，这些可变参数在函数调用时自动组装为一个tuple
def calc(numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum
print(calc([1, 2, 3])) # 非可变参数list
print(calc((4, 5, 6))) # 非可变参数tuple
# 改写成 可变参数,
def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum
print(calc(1, 2, 3)) # list或tuple作为可变参数，都组装成tuple
nums = [1, 2, 3] # 也可以先组装出一个list或tuple，然后把该list或tuple转换为可变参数传进去
print(calc(nums[0], nums[1], nums[2])) # 麻烦，可以简化为下面的方法
print(calc(*nums)) # *nums表示把nums这个list的所有元素作为可变参数传进去，

# 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw): # 关键字参数 **kw
	print('name:', name, 'age:', age, 'other:', kw)
person('scc', 28) # 可以只传入必选参数
person('scc', 28, city = 'Hefei')  # 关键字参数必须传入参数名city，将city = 'Hefei'组装成{'city': 'Hefei'}
extra = {'city': 'Hefei', 'job': 'Engineer'} # 同可变参数，也可以先组装一个dict
person('scc', 28, city = extra['city'], job = extra['job']) # 同样可以简化成下面的形式
person('scc', 28, **extra) # **extra 表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw，kw将获得一个dict
# 注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra

# 命名关键字参数，可以限制关键字参数的名字
def person(name, age, *, city, job): # 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
	print(name, age, city, job)
# def person(name, age, *, city = 'Hefei', job): # 可以给关键字参数设置默认值，调用时可以不传入参数
	# print(name, age, city, job)
# person('scc', 28, weight = '178', job = 'Engineer') # TypeError: person() got an unexpected keyword argument 'weight'
person('scc', 28, city = 'Hefei', job = 'Engineer') # 只接受 关键字参数名city，job
def person(name, age, *args, city, job): # 函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
	print(name, age, args, city, job)
person('scc', 28, city = 'Hefei', job = 'Engineer')

# 总结 参数类型：必选参数（位置参数），默认参数，可变参数、关键字参数和命名关键字参数，这5种参数可以组合使用
# 参数定义的顺序必须是：必选参数、默认参数、可变参数（tuple）、命名关键字参数和关键字参数（dict）
