# -*- encoding:utf-8 -*-
# 要理解generator的工作原理，它是在for循环的过程中不断计算出下一个元素，并在适当的条件结束for循环。
# 对于函数改成的generator来说，遇到return语句或者执行到函数体最后一行语句，就是结束generator的指令，for循环随之结束。


# def fib(max):
# 	n,a,b = 0,0,1
# 	while n< max:
# 		print b
# 		a,b = b,a+b
# 		n = n+1
# fib(6)

def fib(max):
	n,a,b = 0,0,1
	while n< max:
		yield b			# 跟上面的注释代码相比，生成器只需要将print改成yield
		a,b = b,a+b
		n = n+1

f = fib(6)
print f.next()
print f.next()
print f.next()
print f.next()
print f.next()
print f.next()
print f.next()        # 有一种打断点的意思
