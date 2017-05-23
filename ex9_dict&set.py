# -*- coding: utf-8 -*-
#习题：dict(字典)和set
######################
names = ["Michael", "Bob", "Tracy"] # 假设根据同学名字查找对应的成绩，用list实现，需要两个list，遍历list直到找到我们想要的名字为止，list越长,查询的耗时越长
scores = [95, 77, 84]
name = input("please enter name: ")
for x in names:
	if x == "Michael" and x == name:
		print("your score is %d." % scores[0])
	elif x == "Bob" and x == name:
		print("your score is %d." % scores[1])
	elif x == "Tracy" and x == name:
		print("your score is %d." % scores[2])
	
# 用dict实现，dict全称dictionary字典，在其他语言中也称为map映射，使用键->值（key->value）存储，具有极快的查找速度
d = {"Michael": 95, "Bob": 77, "Tracy": 84} #　例如"Bob" 对应的是成绩95的内存地址，key不能重复
d["Adam"] = 98 # 把数据放入dict的方法，除了初始化时指定外，还可以通过key放入。一个key只能对应一个value,多次对一个key放入value,后面的值会把前面的值覆盖
# 判断key 是否存在的方法1：通过in判断
'Adam' in d # 返回布尔值
# 通过get方法判断
d.get("Thomas") # 如果key不存在，返回None（不显示结果），
d.get("Thomas", -1) # 或者自己指定的value
# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除
d.pop("Bob")
d["Scc"] = 100
print(d)
# 使用dict重写查询成绩
name = input("please enter your name: ")
# if name in d:
if d.get(name, 0):
	print("your score is %d。" % d[name])
else:
	print("your score isn't exist.")
# dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，需要牢记一点的是dict的key必须是不可变对象
# 这是因为dict是根据key来计算value的存储位置,这个通过key计算位置的算法称为哈希算法（Hash）
# 要保证hash的正确性，作为key的对象就不能变，在Python中，字符串、整数都是不可变的，因此，可以放心地作为key，而list是可变的，就不能作为key

# set，和dict类似，也是一组key的集合，但不存储value。由于key不能重复，在set中没有重复的key，重复也会被忽略
# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
# 要创建一个set，需要提供一个list作为输入集合
s1 = set([1,2,3,4])
s1.add(5) # 通过add(key)方法可以添加元素到set中
print(s1)
s1.remove(2) # 通过remove(key)方法可以删除元素
print(s1)
s2 = set([3, 4, 5, 6])
print(s1 & s2) # 交集
print(s1 | s2) # 并集
# 理解不可变对象和它对应的变量,要始终牢记的是，a是变量，而”abc“才是字符串对象，对象a的内容是”abc“，但其实是指a本身是一个变量，它指向的对象的内容才是”abc“
a = "abc"
b = a.replace('a', 'A') 
print(a)
print(b)

# 练习 解释为什么会出错
d = {"t1": (1, 2, 3), "t2": (1, [2, 3]), "t3": 44} # 值可以为可变元素
# d = {"t1": (1, 2, 3), (1, [2, 3]): 54, "t3": 44} # 报错 TypeError: unhashable type: 'list'，要保证hash的正确性，作为key的对象就不能变，key必须为不可变的，
print(d["t2"])
# s = set([(1, 2, 3), (1, [2, 3]), 1, 2]) # 报错 TypeError: unhashable type: 'list'，因为key必须为不可变的

# list、tuple、dict和set总结
L = [1, 2, 3] # list数组的值可以改变，如 L[0] = 9
T = (4, 5, [1, 2, 3]) # tuple元组的每个元素，指向永远不变,如 不支持T[0] = 3修改值,，要创建一个内容不变的tuple，就要保证每个元素本身不变
D = {"d1": 33, "d2": [1, 2], "d3": 55} # dict字典key本身必须是不可变元素，通过hash计算value地址，value可以为可变元素
S = set([1, (2, 3, 4), 5]) # set集合为key的无序和无重复的集合，集合的元素key本身必须是不可变的