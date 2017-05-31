# -*- coding: utf-8 -*-
#习题：条件判断
######################
age = 20
if age >= 6:
	print('teenager')
elif age >= 18:
	print('adult')
else:
	print('kid')
# if语句是从上往下判断，如果在某个判断上是True，执行该判断对应的语句，就会忽略掉剩下的elif和else
x = "" # 只要x是非零数值、非空字符串、非空list，就判断为True，否则为False
if x:
	print("True")
else:
	print("False")
	
birth = input("your birth is: ")
birth = int(birth) # input()返回的数据类型是字符串str，不能直接和整数比较，必须先把str转换成整数，使用int()函数实现转换
if birth < 2000:
	print("00前")
else:
	print("00后")
	
# 练习
height = 1.75
weight = 80.5
bmi = 80.5 / (1.75 * 1.75)
print(bmi)
if bmi < 18.5:
	print("过轻")
elif bmi >= 18.5 and bmi <= 25:
	print("正常")
elif bmi >25 and bmi <= 28:
	print("过重")
elif bmi >28 and bmi <= 32:
	print("肥胖")
else:
	print("严重肥胖")