# *-* encoding:utf-8 *-*

# 直接把类的属性暴露出去，就无法检查参数
class Student(object):
	def get_score(self):
		return self._score

	def sec_score(self,value):
		if not isinstance(value,int):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0~100!')
		self._score = value

# 以上这种方式必须调用Student类的方法来进行读写，如果仍然想利用属性的读写则可以用@property
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 60
print s.score

# s.score=9999

# birth是可读写属性，age是只读属性
class Student(object):
	@property
	def birth(self):
		return self._score

	@birth.setter
	def birth(self,value):
		self._birth = value

	@property
	def age(self):
		return 2017-self._birth