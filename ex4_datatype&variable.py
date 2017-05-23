# -*- coding: utf-8 -*-
# 习题3：数据类型和变量
########################
# 整数。包括正、负整数，整数运算永远都是精确的（整数除法的结果是浮点数），十六进制用0x前缀和0-9，a-f表示
print(10 / 3) # 除不尽的结果是浮点数
print(9 / 3) # 整除的结果也是浮点数
print(10 // 3) # //称为地板除，整数的地板除永远是整数
print(10 % 3) # 求余数
print(0xa, 0xb)
# 浮点数。浮点数的运算可能存在四舍五入的误差
print(1.23, 1.23e3) # 等同1.23*10^3
# 字符串。用'' 或""表示，如果字符串内部有很多换行，用\n写在一行里面不好阅读，为了简化，可以用''' '''的格式表示
print('''line1
line2
line3''')
# 转义字符"\"。例如\n表示换行，\t表示制表符，\本身转义\\
print('I\'m learning\nPython.')
print('\\\n\\')
print(r'\\\n\\') # 用r''表示''内部的字符串默认不转义

# 布尔值只有True、False两种值，要么True，要么False，注意大小写
# 布尔值可以用 and、or和not运算，即与或非运算
print(True and True)
print(5 > 3 and 3 > 1)
print(True or False)
print(5 > 3 or 3 < 1)
print(not True)
print(not 5 >3)
age = int(input("please enter your age："))
# if语句体中冒号”:“下面的语句块用四个空格缩进表示，一个Tap制表符
if age >= 18: 
	print('adult')
else:
	print('teenager')
# 空值。一个特殊的值，用none表示
# 变量。变量名必须是大小写英文、数字和_的组合，且不能用数字开头
# python变量本身类型是不固定的，所以python也叫动态语言，与之对应的是静态语言。静态语言在定义变量时必须指定变量类型
# 常量。所谓常量就是不能变的变量，通常用全部大写表示
PI = 3.1415926

# 练习
n = 123
print(n)
f = 456.789
print(f)
s1 = 'hello, world'
print(s1)
s2 = 'hello, \'Adam\''
print(s2)
s3 = 'hello, "Bart"'
print(s3)
s4 = r'''hello,
Lisa!'''
print(s4)