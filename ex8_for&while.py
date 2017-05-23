# -*- coding: utf-8 -*-
#习题：循环
######################
# for x in ...循环，依次把list或tuple中的每个元素迭代出来
names = ['Michael', 'Bob', 'Scc']
for name in names:
	print(name)

sum = 0 # 累加
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
	sum = sum + x 
print(sum)

range(101) # 使用range()函数生成整数序列，默认不设置步进或范围，从0开始到100，等同range(0, 101, 1)，不包含101，
print(list(range(0, 101, 1))) # 通过list()函数转换成list
sum = 0
for x in range(101):
	sum = sum + x
print(sum)

n = 99
sum = 0
while n > 0:
	sum = sum + n
	n = n - 2
print(sum)
# 练习
L = ['Bart', 'Lisa', 'Adam']
for name in L:
	print('Hello, %s' % name)
while n < len(L):
	print('Hello,', L[n])
	n = n + 1
# 在循环中，break 语句可以提前退出循环
n = 1
while n <= 100:
	if n >10:
		break
	print(n)
	n = n + 1
print('end')

n = 0
while n < 10:
	n = n + 1
	if n % 2 == 0: # 如果n为偶数，执行continue语句
		continue # continue语句会直接继续执行下一轮，后续的print()语句不会执行
	print(n)

