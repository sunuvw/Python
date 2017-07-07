# -*- coding: utf-8 -*-
# 函数式编程
#######################
# 返回函数
# 函数作为返回值
def lazy_sum(*args): # *args可变参数，参数数目不确定
	def sum():
		ax = 0
		for n in args: # 内部函数sum()可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包”
			ax = ax + n
		return ax
	return sum # 不立刻求和，而是在后面的代码中根据需要计算，这里不返回求和的结果，而是返回求和的函数sum
	
f1 = lazy_sum(1, 3, 5, 7, 9) # 返回求和的函数,但不执行
print(f1) # <function lazy_sum.<locals>.sum at 0x01E742B8>
print(f1()) # 调用函数f1()时，相当于sum()，才真正执行
f2 = lazy_sum(1, 3, 5, 7, 9) # 每次调用都会返回一个新的函数,f1 != f2
print(f2) # <function lazy_sum.<locals>.sum at 0x02174270> 

# 闭包 当一个函数返回另一个函数后，其内部的局部变量还被返回的那个函数引用
def counts():
	fs = []
	for i in range(1, 4): # 迭代[1,2,3]
		def f():
			return i * i # 引用参数i			
		fs.append(f) # 添加一个函数f到fs列表中，f没有加()，不运行，所以目前它只是一个内置i参数的函数，并没有执行,fs = [f, f, f]，for循环完毕i变为3
	return fs # 返回fs，即返回fs = [f, f, f]，f只是函数名称，并不运行
f1, f2, f3 = counts() # counts()返回f1, f2, f3 = [f, f, f]

print(f1) # <function counts.<locals>.f at 0x01E44270>
# 类似f1--> f , f1() --> f() i为3
print(f1()) # 结果函数f()为9的原因在于：返回的函数引用了变量i，但并没有立刻执行，等到3个迭代完毕，即3个函数都返回时，i的值已经变为3了，因此最终的结果为9
# 返回闭包时牢记的一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量
print(f2) # <function counts.<locals>.f at 0x01E94420>
print(f2()) # 9
print(f3) # <function counts.<locals>.f at 0x01E944B0>
print(f3()) # 9

# 匿名函数lambda
# 学习一下lambda表达式用在def函数中：
# 例如 
def lam(y):
	return lambda x: x + y # x为positional argument位置参数，不通过形参传输
a = lam(2)
print(a(20)) # 结果22
print((lam(2))(20)) # 等同上面，结果也是22，y = 2, x = 20



def counts_v1():
	#def f(j):
		# def g():
			# return j * j
	###########################
	# 用 lambda改写def1
	# def f(j):
		# return lambda: j * j # 无位置参数即分号：前面没有参数,返回lambda表达式
	###########################
	# 用 lambda改写def2
	f = lambda j: lambda : j * j # lambda函数赋值给变量f，这里的f没有加括号(j)这个形参，所以需要添加j这个位置参数，以接收传来的参数f(i)，例如f(1) --> lambda 1: lambda: 1 * 1 
	
	fs = []
	for i in range(1, 4):
		fs.append(f(i)) # 函数f加了括号(i)立刻被执行：[f(1),f(2),f(3)]，该函数的参数绑定循环变量i当前的值，无论该循环变量后学如何更改，已绑定到函数参数的值不变,再传递给g
	return fs 
f4, f5, f6 = counts_v1() # counts_v1()返回f4, f5, f6 = [f(1),f(2),f(3)]
print(f4) # <function counts_v1.<locals>.f.<locals>.g at 0x01EB4270>
# 类似f4 --> f(1) ,f4() --> f(1)() --> g() j = 1
print(f4())
print(f5())
print(f6())

# 装饰器 decorator 不修改原函数的定义，在代码运行期间动态增加功能的方式，本质上就是一个返回函数的高阶函数
def now(i):
	print("2017-7-7", i)
f = now # 函数也是一个对象，可以赋值给变量
f(1) # 等同于now(1)
# 函数对象有一个__name__属性，可以拿到函数的名字
print(now.__name__) # 双下划线__
print(f.__name__)

# 定义一个能打印日志的decorator
import functools
def log(func): # decorator可以接收一个函数作为参数
	@functools.wraps(func)
	def wrapper(*args, **kw): # 接收任意参数：*args可变参数tuple,**kw字典dict
		print('call %s():' % func.__name__)
		return func(*args, **kw) # 返回原函数,执行原函数
	return wrapper # 返回的是wrapper,now_v1的__name__属性也变成wrapper，在def wrapper前面用这个@functools.wraps(func)修正
	
@log # @log放到now_v1()前面，相当于执行了语句 now_v1 = log(now_v1) --> wrapper
def now_v1(i):
	print('2017-7-8', i)
now_v1(2222) # 相当于执行log(now_v1)(2222) --> wrapper(2222) 
print(now_v1.__name__) # 经过修饰器后now_v1的__name__属性变了

# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数
def log_v1(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print('%s %s():' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper # 返回的是wrapper,now_v2的__name__属性也变成wrapper，在def wrapper前面用这个@functools.wraps(func)修正
	return decorator
	

@log_v1('execute')# 相当于执行now_v2 = log_v1('execute')(now_v2)
def now_v2(): 
	print('2017-7-9')
now_v2() # log_v1('execute')(now_v2)() ---> 首先执行log_v1('execute') 返回decorator函数，再调用执行decorator(now_v2),最终返回wrapper函数，再调用执行wrapper()
print(now_v2.__name__) # 经过修饰器后now_v2的__name__属性变了


# 练习1，编写一个decorator，能在函数调用的前后打印出'begin call' 和 'end call'的日志
def log_v3(text1, text2):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print('%s %s():' % (text1, func.__name__))
			func(*args, **kw)
			print('%s %s()' % (text2, func.__name__))
		return wrapper 
	return decorator
@log_v3('begin call', 'end call')
def now_v3():
	print('2017-7-10')
now_v3()
# 练习2，编写一个既可以支持参数也可以不支持参数的decorator
def log_v4(text1 = None, text2 = None): # 可以先赋空值
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			if isinstance(text1, str) or isinstance(text2, str):
				print('%s %s():' % (text1, func.__name__))
				func(*args, **kw)
				print('%s %s():' % (text2, func.__name__))
			else:
				print('%s():' % (func.__name__))
				func(*args, **kw)
				print('%s():' % (func.__name__))
		return wrapper 
	return decorator
@log_v4('start call','end call')
def now_v4():
	print('2017-7-10')
now_v4()