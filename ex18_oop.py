# -*- coding: utf-8 -*-
# 面向对象 oop
#######################
# 类、属性、方法、实例
# 类相当于飞机的设计蓝图（抽象的模板），实例（具体的对象）相当于拥有不同属性的具体飞机，飞机又可以使用这个类提供的功能（方法）
class Student(object): # 类名通常是大写开头的单词，(object)表示该类是从这个object类继承的，通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类
	def __init__(self, name, score): # 通过定义一个特殊的__int__方法，在创建实例的时候，把name，score等属性绑上去；__int__方法第一个参数永远是self，代表创建的实例本身
		self.name1 = name  # 这些属性是类的属性，即内部属性，可以把一些常见的经常用的属性绑定到一个类中，创建的实例能够共享这些属性
		self.score1 = score
	def print_score(self): # 通过在类的内部定义访问数据的函数，把“数据”给封装起来，这些封装数据的函数是和Student类本身是关联起来的，称之为类的方法
		print('%s: %s' % (self.name1, self.score1))
	def get_grade(self): #　定义方法访问实例的数据self.score
		if self.score1 >= 90:
			return 'A'
		elif self.score1 <= 60:
			return 'B'
		else:
			return 'C'
		
scc = Student('suncc', 99) # 创建Student类的实例scc，Student类有了__int__方法，在创建实例的时候，就不能传入空的参数，必须传入与__int__方法相匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去
scc.print_score()
print(scc.get_grade())
scc.age = 18 # 将age这个属性绑定到实例scc，这个属性属于这个实例,和继承类的属性互不影响
print(scc.age)

# 类是创建实例的模板，而实例是一个一个具体的对象，各个实例拥有的数据都相互独立，互不影响
# 方法就是与实例绑定的函数，和普通的函数不同，方法可以直接访问实例的数据

# 访问控制
# 如果要让内部属性不被外部访问，可以在属性的名称前加上两个下划线__，就变成一个私有变量(private),只有内部可以访问，外部不能访问
class Student1(object):
	def __init__(self, name, score):
		self.__name1 = name  # 变成私有变量后，实际上这里的__name1和__score1已经变成_Student1__name1和_Student1__score1
		self.__score1 = score
	def print_score(self):
		print('%s: %s' % (self.__name1, self.__score1))
	def return_info(self): # 可通过定义返回函数，从外部获取内部变量值
		return self.__name1, self.__score1
	def set_score(self11, score): # self11 是用来接收实例名的，名字可以随便起，但默认写为self
		if 0 <= score <=100:
			self11.__score1 = score
		else:
			raise ValueError('bad score') # 抛出错误
		
lisa = Student1('sunlisa', 88)
# lisa.__name1 # 会报错，属性不存在，私有属性不可访问
lisa.print_score()
print(lisa.return_info())
lisa.set_score(55) # 当调用一个方法时，会隐含的把实例名（self）传过去，这就要定义方法时至少定义一个self形式参数（其实名字可以随便起，但为了统一标准，默认写为self），set_score(self, score):
lisa.print_score()

# 继承和多态
class Animal(object):
	def run(self):
		print('Animal is running...')

class Dog(Animal): # 子类Dog继承父类Animal
	def run(self): # 当子类和父类都存在相同的run()方法时，子类的run()覆盖了父类的run(),在代码运行的时候，总是会调用子类的run(),就是继承的另一个好处：多态
		print('Dog is running...')
	def eat(self):
		print('Eating meat...')
super()	

dog = Dog()
dog.run() # 可以使用父类Animal的run()，子类的run()覆盖了父类的run()
# 多态，当定义一个class时，就相当于定义了一种数据类型，和str、list、dict数据类型是一样的
a = list() # 变量a是列表类型
b = Animal() # ｂ是Animal类型
c = Dog() # c 是Dog类型
print(isinstance(a, list)) # 判断变量a是否是list类型
print(isinstance(b, Animal))
print(isinstance(c, Dog))
print(isinstance(c, Animal)) # 类Dog是从Animal类继承下来的，所以创建的Dog实例c，既是Dog类，同时也是Animal类

def run_twice(animal):
	animal.run() # 只要是Animal类型就可以调用run()方法，具体调用的run()方法是作用在Animal、Dog还是Tortoise对象上，由运行时该对象的确切类型决定，这就是多态的真正威力
	animal.run()

run_twice(Animal()) # 传入Animal()实例
run_twice(Dog()) # 传入Dog()实例

class Tortoise(Animal):
	def run(self):
		print('Tortoise is running slowly...')
run_twice(Tortoise())
# “开闭”原则
# 对扩展---开放：允许新增Animal子类
# 对修改---封闭：不需要修改依赖Animal类型的run_twice()等函数
					        （根类）object 
		    （父类）  Animal                       Plant
	 （子类） Dog              Cat         Tree            Flower 
（实例） 小白     小黑
 
# 继承可以把父类的所有功能都直接拿过来，这样就不必从零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写

