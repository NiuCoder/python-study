# -*- coding:utf-8 -*-
# 定义函数以及函数的参数
def my_abs(x):
	if x >= 0:
		return x
	else:
		return -x

print my_abs(-22)

# 空函数
def nop():
	pass   #pass可以当做占位符



import math
def move(x,y,step,angle=0):
	nx = x + step * math.cos(angle)
	ny = x + step * math.sin(angle)
	return nx,ny

r= move(1,1,10,math.pi/6)

#函数的多值返回值r其实是一个tuple
print r

def my_power(x,n=2):
	s = 1
	while n>0:
		n = n-1
		s = s * x
	return s

print my_power(2,3)

print my_power(5)


def enroll(name,gender,age=6,city='Beijing'):
	print 'name:',name
	print 'gender:',gender
	print 'age:',age
	print 'city:',city

enroll('Sarah','F')
enroll('Bob','M',7)

# 下面这种用法在很多语言中都是不可以的，比如php一定要按照顺序传入所有的参数，除非后边的参数都有默认值
enroll('Adam','M',city='Tianjin')


# 可变参数，如果定义为如下所示需要在参数中传入list或tuple
def calc(numbers):
	sum = 0
	for n in numbers:
		sum = sum + n*n
	return sum

# 传入list或者tuple都可以
print calc([1,2,3])
print calc((1,2,3,4))

# 如果不想要这么麻烦，可以将函数定义如下
def calc2(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n*n
	return sum

# 然后就可以摆脱list或tuple传可变参数了
print calc2(1,2,3)
print calc2(1,2,3,4)

# 这是这种print calc2([1,2,3]) 调用的方式就不好使了，正确的调用如下
nums = [1,2,3]
print calc2(nums[0],nums[1],nums[2])

# 或者采用更为方便的方法，加*，这种方法较为常用
print calc2(*nums)


# 关键字参数，这些可变参数在函数调用时自动组装为一个tuple，允许你传入0个或任意个参数名的参数，在函数内部自动组装成一个dict
def person(name,age,**kw):
	print 'name:',name,' age:',age,' other:',kw

person('Michael',30)
person('Bob',35,city='Beijing')
person('Adam',45,gender='M',job='Engineer')

kw = {'city':'Beijing','job':'athlete'}
person('boke',36,**kw)

# 参数组合，这个太灵活了，但是参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数
def func(a,b,c=0,*args,**kw):
	print 'a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw

func(1,2)
func(1,2,c=3)
func(1,2,3,'a','b')
func(1,2,3,'a','b',x=99)


# Lambda Expressions
def make_incrementor(n):
	return lambda x: x+n
f = make_incrementor(42)
print f(3)

# example of documentation
def my_function():
	"""Do nothing, buf document it.

	No,really,it doesn't do anything.
	"""
	pass
print my_function.__doc__

def ask_ok(prompt, retries=4, complaint='Yes or no,please!'):
	while True:
		ok = raw_input(prompt)
		if ok in ('y','ye','yes'):
			return True
		if ok in ('n','no','nop','nope'):
			return False
		retries = retries - 1
		if retries < 0:
			raise IOError('refusenik user')
		print complaint

ask_ok('Do you really want to quit?')