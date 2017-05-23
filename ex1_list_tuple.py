#coding:utf-8
#习题：使用list和tuple
######################
# list列表（数组）数据类型
classmates = ['Scc', 'Lili', 'Tracy']
print(classmates)
print(classmates[0]) # 索引是从0开始,获取一个元素，以次类推
print(classmates[1])
print(classmates[2])
print(classmates[-1]) # -1做索引，获取最后一个元素
print(classmates[-2])
classmates.append("Adam") # 用append()方法在list结尾追加元素
print(classmates)
classmates.pop() # 删除list末尾的元素,用pop()方法
print(classmates)
classmates.pop(1) # 删除指定位置的元素，用pop(i),其中i是索引位置
print(classmates)
classmates.insert(1,"Scc1") # 在指定位置插入元素，用insert(index,obj)
print(classmates)
s = ['python', 'java',['asp', 'php'], 'scheme'] # list元素也可以是另一个list
print(s[2][1]) # s可以看成是一个二维数组，类似的还有三维、四维。。。数组
L = [] # 空数组

# tuple 元组，一旦初始化就不能修改
classmates = ("Scc", "Bob", "Lili") # 这个tuple不可改变
t = ("scc",) # 定义只有一个元素的tuple,元素后面要加逗号，否则就变成元素值为1，被误解成数学计算意义上的括号
print(t[0])
t = () # 空元组
t = ('a', 'b', ['A', 'B']) # ”可变“的元组，tuple所谓的不变是说：tuple 的每个元素指向永远不变，即指向list就不能指向其他对象，但list本事是可变的
print(t)
t[2].insert(2, "C")
print(t)

# 练习
L = [['Apple', 'Google', 'Microsoft'], ['Java', 'Python', 'Ruby', 'PHP'], ['Adam', 'Bart', 'Lisa']]
# 打印Apple,Python,Lisa
print(L[0][0])
print(L[1][1])
print(L[2][2])

