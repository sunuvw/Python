# -*- coding: utf-8 -*-
# 习题1-2：输出
###################
print("hello, world.")
print('hello, world.')
print("I have some 'apples'.")
print('I have some "apples".')
print('I\'m "OK"!') # 既包含‘ 又包含“时需要转义字符\
print(u"你好，世界。") # 在windows中，python2.7中字符串默认采用ASCII编码(3.0使用unicode编码，支持多语言)，中文为避免乱码，要声明unicode就要加u（linux环境下不需要加）
print("The quick brown fox", "jumps over", "the lazy dog.") # print()函数也可以接受多个字符串，用逗号“,”隔开，就可以连成一串输出
#遇到逗号“,”会输出一个空格
print(200, '100+300 =', 100+300) # 可以打印整数或计算结果
# 这是注释的意思，#号后面加一个空格好看些
# 任何在 # 后面的东西都不会被python执行
print("I could have code like this.")
# print("This won't run.")
print("This will run.")
# 注意倒着读代码有助于找错误