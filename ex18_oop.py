# -*- coding: utf-8 -*-
# 面向对象 oop
#######################
# 类、属性、方法、实例
# 类相当于飞机的设计蓝图（抽象的模板），实例（具体的对象）相当于拥有不同属性的具体飞机，飞机又可以使用这个类提供的功能（方法）
class Student(object): # 类名通常是大写开头的单词，(object)表示该类是从这个object类继承的，通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类
	def __init__(self, name, score): # 通过定义一个特殊的__int__方法，在创建实例的时候，把name，score等属性绑上去；__int__方法第一个参数永远是self，表示创建的实例本身
		self.name = name  # 这些属性是类的属性，可以把一些常见的经常用的属性绑定到一个类中，创建的实例能够共享这些属性
		self.score = score
	def print_score(self): # 通过在类的内部定义访问数据的函数，把“数据”给封装起来，这些封装数据的函数是和Student类本身是关联起来的，称之为类的方法
		print('%s: %s' % (self.name, self.score))
	def get_grade(self): #　定义方法访问实例的数据self.score
		if self.score >= 90:
			return 'A'
		elif self.score <= 60:
			return 'B'
		else:
			return 'C'
		
scc = Student('suncc', 99) # 创建Student类的实例scc，Student类有了__int__方法，在创建实例的时候，就不能传入空的参数，必须传入与__int__方法相匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去
scc.print_score()
print(scc.get_grade())
scc.age = 18 # 将age这个属性绑定到实例scc，这个属性属于这个实例,和继承类的属性互不影响

class Animal:
	pass
	run = 'fast'
	eat = 'more'

dog = Animal
print(dog.run)
# 类是创建实例的模板，而实例是一个一个具体的对象，各个实例拥有的数据都相互独立，互不影响
# 方法就是与实例绑定的函数，和普通的函数不同，方法可以直接访问实例的数据