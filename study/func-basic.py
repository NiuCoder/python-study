# -*- coding:utf-8 -*-
# show how python function works

# function about number
print abs(-100)

print cmp(1,2)

print cmp(3,3)

print cmp(2,1)

# function about transfer type, command line will show better result
print str(1.23)  #'1.23'

print unicode(100) # u'100'

print bool(1) # True

print bool('')  # Flase


a = abs  # 变量名指向函数名，相当于起了个别名
print a(-1)

