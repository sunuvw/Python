# -*- coding: utf-8 -*-
# 模块
#######################
'a test module' # 任何模块代码的第一个字符串都被视为模块的文档注释
__author__ = 'Scc' # 模块作者
print(__doc__) # 上面的文档注释
import sys # 导入python内置的sys模块，就有变量sys指向该模块，利用sys这个变量，就可以访问sys模块的所有功能
# sys模块有一个argv变量，用列表list存储了命令行的所有参数，argv至少有一个元素，因为第一个元素永远是该.py文件的名称
print(sys.argv) # 文件名
def test():
	args = sys.argv
	if len(args) == 1: # 列表只有一个元素，那就是文件名
		print('Hello, world')
	elif len(args) == 2:
		print('Hello, %s' % args[1])
	else:
		print('Too many arguments')

print(__name__)	# 单独运行模块时，变量__name__的值为__main__	
if __name__ == '__main__': # 如果在其他地方导入该模块时，__name__的值将不是__main__,if判断可以作为测试该模块使用——
	test()

# 作用域
# public函数变量，如abc 这样不加下划线的，可以被直接引用
# private函数或变量，如_xxx和__xxx这样前下划线，从编程习惯上不应该被直接引用，仅仅在模块内部使用
# 特殊变量或函数，如__name__、__doc__等前后双下划线，python内置，可以被直接引用，但是有特殊用途
def _private_1(name): # 外部不需要引用的函数全部定义成private，隐藏内部逻辑
	return 'Hello, %s' % name

def _private_2(name):
	return 'Hello, %s' % name

def greeting(name): # 只有外部需要引用的函数才定义为public
	if len(name) > 3:
		return _private_1(name)
	else:
		return _private_2(name)
