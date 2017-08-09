# !usr/bin/env python
# -*- encoding:utf-8 -*-
# python内建模块
# namedtuple,一种有意义的数据组合
# namedtuple('名称',[属性list])
from collections import namedtuple
Point = namedtuple('Point',['x','y'])
p = Point(1,2)
print p.x,p.y

# namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用
print isinstance(p,Point)
print isinstance(p,tuple)


# deque，高效实现插入和删除操作的双向列表，适用于队列和栈
from collections import deque
q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print q

# defaultdict，除了在key不存在时返回默认值，defaultdict的其他行为跟dict完全一样
from collections import defaultdict
dd = defaultdict(lambda:'N/A')
dd['key1'] = 'abc'
print dd['key1']
print dd['key2']


# OrderedDict，dict的key是无序的，想要有序可以用OrderedDict
from collections import OrderedDict
d = dict([('a',1),('b',2),('c',3)])
print d
od1 = OrderedDict([('a',1),('b',2),('c',3)])
od2 = OrderedDict([('a',1),('c',2),('b',3)])
print od1
print od2

# Counter，简单的计数器
from collections import Counter
c = Counter()
for ch in 'programming':
	c[ch] = c[ch] + 1
print c

# base64
import base64
print base64.b64decode('YWJjZA==')

# struct, 解决str和其他二进制数据类型的转换
import struct
print struct.pack('>I',10240099) #将这个四字节无符号整数转为字符串

print struct.unpack('>IH','\xf0\xf0\xf0\xf0\x80\x80') #将字符串转换为4字节无符号整数和2字节无符号整数

# itertools
import itertools
natuals = itertools.count(1)
for n in natuals:
	if n < 100:    #不加这个的话会无限循环下去
		print n
	else:
		break

cs = itertools.cycle('ABC')
# 以下代码同样用于示意，放开执行会无限循环下去
# for c in cs:
	# print c

ns = itertools.repeat('A',10)
for n in ns:
	print n

# 除了自己写逻辑控制循环以外，还可以用takewhile来截取一个有限的序列
nats = itertools.count(1)
ns = itertools.takewhile(lambda x:x<=10,nats)
for n in ns:
	print n

