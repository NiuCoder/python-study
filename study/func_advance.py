# -*- encoding:utf-8 -*-

# 变量可以指向函数
x = abs(-10)
print x

f = abs
print f(-10)

# 传入函数：一个函数接收另一个函数做为参数，这种函数就称之为高阶函数
def add(x,y,f):
	return f(x) + f(y)

print add(-5,6,abs)

# Python内建了的传入函数中有两个比较有名，map,reduce
# map(f(x),list)，将f(x)作用在list中的每一个元素，并返回一个新的list
def f(x):
	return x*x
print map(f,range(1,11))

print map(str,range(1,10))

# reduce(f(x),list)，将f(x)作用在list上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算。
# example: reduce(f,[x1,x2,x3,x4]) = f(f(f(x1,x2),x3),x4)

def add(x,y):
	return x+y
print reduce(add,[1,3,5,7,9])


def fn(x,y):
	return x*10+y

def char2num(s):
	return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]

print reduce(fn,map(char2num,'13579'))

# 还可以用lambda函数进一步简化成：
def str2int(s):
	return reduce(lambda x,y:x*10+y,map(char2num,s))
print str2int('4321423')

# 练习一，将字符串首字母大写，其他字母小写
def capital(s):
	return s.capitalize()

print map(capital,['adam','LISA','barT'])

# 练习二，接收一个list并求积
def prod(sequence):
	def fn(x,y):
		return x*y
	return reduce(fn,sequence)

print prod(range(1,6))

# 把一个字符串的空字符串去掉
def not_empty(s):
	return s and s.strip()

print filter(not_empty,['A','','B',None,'C',' '])


# 自定义排序规则，忽略大小写按字母排序
def cmp_ignore_case(s1,s2):
	u1 = s1.upper()
	u2 = s2.upper()
	if u1 < u2:
		return -1
	if u1 > u2:
		return 1
	return 0

print sorted(['bob','about','Zoo','Credit'],cmp_ignore_case)


# 函数作为返回值
# 可变参数求和
def calc_sum(*args):
	ax = 0
	for n in args:
		ax = ax + n
	return ax

print calc_sum(1,2,3)
print calc_sum(1,2,3,4,5)

# 如果不希望立即求和，而是在后面的代码中，根据需要在计算怎么办？可以不返回求和的结果，而是返回求和的函数
def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum
# 以上这种返回函数的方式成为闭包（Closure）

f1 = lazy_sum(1,3,5,7,9)
f2 = lazy_sum(1,3,5,7,9)
print f1()
print f2()
print f1==f2    #return False，f1()和f2()的调用结果互不影响


# 另外一个例子
def count():
	fs = []
	for i in range(1,4):
		def f():
			return i*i
		fs.append(f)
	return fs

f1,f2,f3 = count()
# 上面的例子中，每次循环，都创建了一个新的函数，然后把创建的3个函数都返回了
print f1()
print f2()
print f3()
# 以上输出的结果不是期望中的1,4,9而全都是9.原因在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，
# 它们所引用的变量i已经变成了3，因此最终结果都是9
# 因此返回闭包时牢记一点，返回函数不要引用任何循环变量，或者后续会发生变化的变量。

# 一定要引用循环，需要再创建一个函数，用该函数的参数绑定循环变量当前的值
def count():
	fs = []
	for i in range(1,4):
		def f(i):
			def g():
			    return i*i
			return g    
		fs.append(f(i))
	return fs
f1,f2,f3 = count()
print f1()
print f2()
print f3()

# 匿名函数,可以用lambda 表达式
map(lambda x:x*x,range(1,10))
# lambda x:x*x is equivalent to :
def f(x):
	return x*x
# 匿名函数有个好处，不用担心函数名冲突

# 同样可以把匿名函数做为返回值返回，如：
def build(x,y):
	return lambda: x*x + y*y

f = build(2,3)
print f()

# 装饰器
def now():
	print '2017-03-27'
print now.__name__

# log是一个装饰器，类似于java里边的切片
def log(func):
	def wrapper(*args,**kw):
		print 'call %s():' % func.__name__
		return func(*args,**kw)
	return wrapper

@log
def now():
	print '2017-03-27'

print now()

# 把@log放在now()函数的定义处，相当于执行了语句：
now = log(now)

# 由于log()是一个decorator,返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数
# 于是调用now()将执行新函数，即在log()函数中返回wrapper()函数。在wrapper()函数内，首先打印日志，再紧接着调用原始函数
print now.__name__

# 标准的decorator写法：
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'before call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

# 或者针对带参数的decorator：

import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

# 在OOP设计模式中，decorator被称为装饰模式。OOP的装饰模式需要通过继承和组合来实现，而Python除了能支持OOP的decorator外，
# 直接从语法层次支持decorator。Python的decorator可以用函数实现，也可以用类实现。

# 偏函数
# int() 函数还提供base参数，默认值为10。如果传入base参数，就可以做N进制的转换
print int('100',base=8)

def int2(x,base=2):
	return int(x,base)
print int2('100000')
print int2('100011')

# functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2:
import functools
int2 = functools.partial(int,base=2)
print int2('100010001')


