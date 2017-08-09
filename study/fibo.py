# Fibonacci numbers module
def fib(n):
	a,b = 0,1
	while b<n:
		print b,
		a,b = b,a+b

def fib2(n):
	result = []
	a,b = 0,1
	while b<n:
		result.append(b)
		a,b = b,a+b
	return result

# act as entry of the module, the executable statements
if __name__ == "__main__":
	import sys
	print fib2(int(sys.argv[1]))    # you can do anything here using fib or fib2, think about main in Java but different.

