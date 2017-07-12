# -*- coding: utf-8 -*-
# 面向对象 oop
#######################
# 类、属性、方法、实例
# 类相当于飞机的设计蓝图（抽象的模板），实例（具体的对象）相当于拥有不同属性的具体飞机，飞机又可以使用这个类提供的功能（方法）
class Student(object): # 类名通常是大写开头的单词，(object)表示该类是从这个object类继承的，通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类
	def __int__(self, name, score): # 通过定义一个特殊的__int__方法，在创建实例的时候，把name，score等属性绑上去；__int__方法第一个参数永远是self，表示创建的实例本身
		self.name = name
		self.score = score
	def print_score(self):
		print('%s, %s' % (self.name, self.score))

scc = Student('sun cc', 99) # 创建Student类的实例scc，Student类有了__int__方法，在创建实例的时候，就不能传入空的参数，必须传入与__int__方法相匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去
scc.print_score()
