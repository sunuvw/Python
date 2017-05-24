def out_abs(x):
	if not isinstance(x,(int, float)): # 参数类型检查
		raise TypeError("bad operand type")
	if x >= 0:
		return x  # 函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕
	else:
		return -x # 如果没有return语句，函数执行完毕后也会返回结果，只是结果为None，return None 可以简写为return
		