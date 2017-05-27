# -*- coding: utf-8 -*-
#习题：递归函数
#######################
# 在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数
# 阶乘公式n! = n * (n-1)! 转换成递归函数：fact(n) = n * fact(n - 1)
def fact(n):
	if n == 1:
		return 1
	return n * fact(n - 1)
print(fact(5))
# print(fact(1000)) # 由于栈的大小是有限的，所以，递归调用的次数过多，会导致栈溢出
# 解决递归调用栈溢出的方法是通过尾递归优化,是指 在函数返回的时候，调用自身本身，并且，return语句不能包含表达式，这样编译器或者解释器就可以把尾递归做优化，
# 使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况
def fact(n):
	return fact_iter(n, 1)

def fact_iter(num, product):
	if num == 1:
		return product
	return fact_iter(num - 1, num * product) # 可以看到，仅返回递归函数本身，num - 1和num * product在函数调用钱就会被计算，不影响函数调用
# fact(1000) #遗憾的是，python解释器也没有针对尾递归做优化，也会导致栈溢出

# 练习 汉诺塔游戏：先把上面的n-1个盘子移动到B柱，再把最底层的盘子移动到C柱，最后将B柱上的n-1个盘子移动到C柱上，并保证大盘子始终在下面，小盘子在上面

def move(n, a, b, c):
	if n == 1:	
		print('move', a, '-->', c) # 
	else:
		move(n - 1, a, c, b) # 借助C柱将A上面的n-1个盘子从A移动到B,
		move(1, a, b, c) # 再将A剩下的1个盘子从A移到C
		move(n - 1, b, a, c) # 借助A柱最后将B上的n-1个盘子移到C

# 递归过程执行如下
# move(3, 'A', 'B', 'C')
	# move(2, 'A', 'C', 'B')  （此时传入参数改变了：a = 'A', b = 'C', c = 'B'）
		# move(1,'A', 'B', 'C') : A --> C # A借助C
		# move(1, 'A', 'C', 'B') : A --> B
		# move(1, 'C', 'A', 'B') : C --> B 
		# 借助C柱将A上面的n-1个盘子从A移动到B,
	# move(1, 'A', 'B', 'C') : A --> C 再将A剩下的1个盘子从A移到C
	# move(2, 'B', 'A', 'C')
		# move(1, 'B', 'C', 'A') : B --> A # B借助A
		# move(1, 'B', 'A', 'C') : B --> C
		# move(1, 'A', 'B', 'C') : A --> C
		# 最后借助A柱将B上的n-1个盘子移到C
move(3, 'A', 'B', 'C')
# 理解递归函数的运行原理，先递进，再回归，一层一层递进，直到递进到不可递进为止，然后再一层一层回归执行未执行的语句