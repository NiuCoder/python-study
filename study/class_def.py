class MyClass:
	"""A simple example class"""
	i = 12345

	def f(self):
		return 'hello world'
x = MyClass()
print x.i
print x.f()

class Complex:
	def __init__(self,realpart,imagpart):
		self.r = realpart
		self.i = imagpart

x = Complex(3.0,-4.5)
print x.r,x.i

class Dog:
	def __init__(self,name):
		self.name = name
		self.tricks = []    # creates a new empty list for each dog
	def add_trick(self,trick):
		self.tricks.append(trick)
d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print d.name
print e.name
print d.tricks
print e.tricks 

