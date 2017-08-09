names = ['Michael','Bob','Tracy']
for name in names:
	print name

sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
	sum = sum + x
print sum	

# range(num) ,generate list from 0 to num-1
sum2 = 0
for x in range(11):
	sum2 = sum2 + x
print sum2


sum3 = 0
n = 10
while n>0:
	sum3 = sum3 + n
	n = n-1
print sum3

# break statement
for n in range(2,10):
	for x in range(2,n):
		if n%x == 0:
			print n,'equals',x,'*',n/x
			break
	else:
		# loop fell through without finding a factor
		print n,'is a prime number'

# continue statement
for num in range(2,10):
	if num%2==0:
		print 'Found an even number',num
		continue
	print 'Found a number',num


# Fibonacci series, fib return a value of None
# def fib(n):
# 	a,b=0,1
# 	while a<n:
# 		print a,
# 		a,b=b,a+b
# fib(2000)
# f = fib
# f(1000)
# print fib(1)

def fib2(n):
	result = []
	a,b=0,1
	while a<n:
		result.append(a)
		a,b=b,a+b
	return result
print fib2(100)
