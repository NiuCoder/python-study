# -*- encoding:utf-8 -*-
import os
print os.name

# rename file
# os.rename('test.txt','test2.txt')

# list all folders
print [x for x in os.listdir('.') if os.path.isdir(x)]

# list all python files
print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']

# Python 的os模块封装了操作系统的目录和文件操作，要注意这些函数有的在os模块中，有的在os.path模块中