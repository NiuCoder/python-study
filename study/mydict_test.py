# -*- encoding:utf-8 -*-
# from mydict import *
# d = Dict(a=1,b=2)
# print d['a']
# print d.a

# 单元测试
import unittest
from mydict import Dict
class TestDict(unittest.TestCase):
	def test_init(self):
		d = Dict(a=1,b='test')
		self.assertEquals(d.a,1)
		self.assertEquals(d.b,'test')
		self.assertTrue(isinstance(d,dict))

	def test_key(self):
		d = Dict()
		d['key'] = 'value'
		self.assertEquals(d.key,'value')

	def test_attr(self):
		d = Dict()
		d.key = 'value'
		self.assertTrue('key' in d)
		self.assertEquals(d['key'],'value')

	def test_keyerror(self):
		d = Dict()
		with self.assertRaises(KeyError):
			value = d['empty']
	def test_attrerror(self):
		d = Dict()
		with self.assertRaises(AttributeError):
			value = d.empty

	# setUp和tearDown可以在所有的测试方法之前和之后分别执行，可以干很多事，比如连接数据库以及关闭数据库
	def setUp(self):
		print 'setUp....'

	def tearDown(self):
		print 'tearDown....'
# 单元测试类一定要从unittest.TestCase继承
# 以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行


if __name__ == '__main__':
	unittest.main()
	# import doctest
	# doctest.testmod()    #测试模块的文档