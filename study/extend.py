# *-* encoding:utf-8 *-*
class Animal(object):
	pass

class Runnable(object):
	def run(self):
		print('Running...')

class Flyable(object):
	def fly(self):
		print('Flying...')

class CarnivorousMixin(object):
	print 'I am carnivorous'

class HerbivoresMixin:
	print 'I am herbivores'

class Mammal(Animal):
	pass

class Bird(Animal):
    pass

# kinds of animal
class Dog(Mammal,Runnable,CarnivorousMixin):
	pass

class Bat(Mammal,Flyable):
	pass

# Mixin的目的就是一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个Mixin的功能，
# 而不是设计多层次的继承
# Python自带了TCPServer和UPDServer两类网络服务，而要同时服务多个用户就必须使用多进程或者多线程模型，这两种模型由
# ForkingMixin和ThreadingMixin提供
# 例子：
class MyTCPServer(TCPServer,ForkingMixin):
	pass

class MyUDPServer(UDPServer,ThreadingMixin):
	pass


