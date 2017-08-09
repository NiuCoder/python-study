# -*- encoding:utf-8 -*-
# 在程序运行的过程中，所有的变量都是在内存中，比如，定义一个dict:
d = dict(name='Bob',age=20,score=88)
# 可以随时修改变量，比如把name改成Bill，但是一旦程序结束，内存就会被操作系统回收，下次运行程序，变量又被初始化为Bob
# 我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫picking,在其他语言中叫serialization,marshalling等
# 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上
# 把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling
import pickle
print pickle.dumps(d)

# pickle.dump()直接把对象序列化后写入一个file-like Object
f = open ('dump.txt','wb')
pickle.dump(d,f)
f.close()

# 用pickle.load()方法从一个file-like Object中直接反序列化出对象
f = open('dump.txt','rb')
d = pickle.load(f)
f.close()
print d

# 如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，但更好的是JSON。
# 因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或通过网络传输。
import json
print json.dumps(d)

# 要把JSON反序列化为Python对象，用load()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object
# 中读取字符串并反序列化
json_str = '{"age":20,"score":88,"name":"Bob"}'
print json.loads(json_str)

f = open('dump.txt','wb')
json.dump(d,f)
f.close()

f = open('dump.txt','rb')
d = json.load(f)
f.close()
print d

# JSON进阶,将类序列化
import json 
class Student(object):
	def __init__(self,name,age,score):
		self.name = name
		self.age = age
		self.score = score

s = Student('Bob',20,88)
# print(json.dumps(s))    #这么用会报错，因为dumps方法不知道如何将Student实例变成一个JSON对象

# 因此需要为Student写一个转换函数，首先将Student对象转换为dict,再把函数传进去即可
def student2dict(std):
	return {
		'name':std.name,
		'age':std.age,
		'score':std.score
	}

print (json.dumps(s,default=student2dict))

# 我们也可以偷个懒，将任意class的实例变为dict，通常class的实例都有一个__dict__属性，除了定义了__slots__的class
print (json.dumps(s,default=lambda obj:obj.__dict__))

# 同样的道理，如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换为一个dict对象，然后传入一个object_hook函数
# 负责把dict转换为Student实例
def dict2student(d):
	return Student(d['name'],d['age'],d['score'])

json_str = '{"age":20,"score":88,"name":"Bob"}'
print(json.loads(json_str,object_hook=dict2student))
