# -*- encoding:utf-8 -*-
class Student(object):
	def __init__(self,name):
		self.name = name
print Student('Michael')

# <__main__.Student object at 0x00000000008124E0> ,这样的输出不好看

# 可以重写类的__str__()方法（类似于java中重写toString）
class Student(object):
	def __init__(self,name):
		self.name = name
	def __str__(self):
		return 'Student object (name:%s)' % self.name
print Student('Michael')

class Fib(object):
	def __init__(self):
		self.a,self.b=0,1
	def __iter__(self):
		return self
	def next(self):
		self.a,self.b = self.b,self.a + self.b
		if self.a > 100:
			return StopIteration()
		return self.a
# for n in Fib():
# 	print n
# Fib通过定义__iter__看起来和List有点像
# 如果要表现的像List那样按下标取出元素，需要实现__getitem__()方法
class Fib(object):
	def __getitem__(self,n):
		a,b = 1,1
		for x in range(n):
			a,b = b,a+b
		return a
f = Fib()
print f[10]

# list还有切片的方法，想要Fib也具备切片方法，需要这样做：
class Fib(object):
	def __getitem__(self,n):
		if isinstance(n,int):
			a,b = 1,1
			for x in range(n):
				a,b = b,a+b
			return a
		if isinstance(n,slice):
			start = n.start
			stop = n.stop
			a,b = 1,1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a,b = b,a+b
			return L

f = Fib()
print f[0:5]


class Student(object):
	def __init__(self,name):
		self.name = name
	def __call__(self):
		print('My name is %s' % self.name)

s = Student("Mike")
print s()


