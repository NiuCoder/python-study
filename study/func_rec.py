# -*- coding:utf-8 -*-
# 递归函数

def fact(n):
	if n==1:
		return 1
	return n * fact(n-1)

print fact(3)

# 递归深度过多会导致栈溢出
# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，
# 使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

# 以下就是尾递归方式
def fact(n):
	return fact_iter(n,1)
def fact_iter(num,product):
	if num==1:
		return product
	return fact_iter(num-1,num*product)
	
# 遗憾的是即使改成尾递归，大多数编程语言都没有对尾递归做优化，Python解释器也没有优化，所以上面的方式依然会造成栈溢出
