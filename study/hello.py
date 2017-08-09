# !/usr/bin/env python
# -*- encoding:utf-8 -*-

' a test module'
__author__ = 'Michael Liao'

import sys
def test():
	args = sys.argv
	if len(args) == 1:
		print 'Hello,world!'
	elif len(args)==2:
		print 'Hello,%s' % args[1]
	else:
		print 'Too many arguments!'

if __name__ == '__main__':
	test()

# sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称，例如：
# 运行python hello.py获得是sys.argv就是['hello.py']
# 运行python hello.py Michael获得的sys.argv就是['hello.py','Michael']

# 作用域，在一个模块中，有的函数和变量我们希望给别人使用，有的函数和变量我们希望仅仅在模块内部使用。
# 在Python中，通过_前缀来实现。
# 类似于__xxx__这样的变量是特殊变量，可以被直接引用。如__author__,__name__就是特殊变量，我们自己的变量一般不要用这种变量名
# 类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用
# private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，因为Python没有一种方法可以完全限制访问private函数或变量，但是，
# 从编程习惯上不应该引用private函数或变量。
# private函数或变量的作用是什么呢?

def _private_1(name):
	return 'Hello,%s' % name

def _private_2(name):
	return 'Hi,%s' % name

def greeting(name):
	if len(name) > 3:
		return _private_1(name)
	else:
		return _private_2(name)
# greeting作为外部函数，可以被引用。
