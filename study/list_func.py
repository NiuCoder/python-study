# function of list

# list.append(x), add an item to the end of the list,equivalent to a[len(a):]=[x]
a=[1,2,3]
a.append(4)
a[len(a):]=[5]
print a

# list.extend(L),extend the list by appending another list,equivalent to a[len(a):]=L
b=['a','b','c']
c=['e','f','g']
b.extend(c)
print b

# list.insert(i,x) Insert an item at a given position.i means index, a.insert(0,x) inserts at the front of the list
a=['i','m','n']
a.insert(1,'k')
print a

# list.remove(x), Remove the first item from the list whose value is x.
a = [1,2,3,4,3,5,2,1]
a.remove(2)
print a

# list.pop([i]), Remove the item at the given position in the list, and return it. If no index is specified,a.pop() removes
# and returns the last item in the list.'[]' denote that the parameter is optional.
b = [1,2,3,4,3,5,2,1]
print b.pop(2)
print b

# list.index(x), Return the index in the list of the first item whose valud is x.
b = [1,2,3,4,3,5,2,1]
print b.index(2)
# print b.index(6)

# list.count(x), Return the number of times x appears in the list.
b = [1,2,3,4,3,5,2,1]
print b.count(2)

# list.sort(cmp=None,key=None,reverse=False), Sort the items of the list in place. params can be used to sort customization.
# default sort order asc
b = [1,2,3,4,3,5,2,1]
c = ['a','c','v','b','e']
b.sort()
c.sort()
print b
print c

# list.reverse(),Reverse the elements of the list.
b = [1,2,3,4,3,5,2,1]
c = ['a','c','v','b','e']
b.reverse()
c.reverse()
print b
print c

# Using Lists as Stacks,last-in,first-out. 
# use append() to add an item to the top of the stack, user pop() to retrieve an item.
stack = [3,4,5]
stack.append(6)
stack.append(7)
print stack
stack.pop()
stack.pop()
print stack

# Using Lists as Queues,first-in,first-out. 
# However, lists are not efficient for this purpose. While appends and pops from the end of list are fast.
# doing inserts or pops from the beginning of a list is slow (because all of the other elements have to be shifted by one)
# To implement a queue, use collections.deque which was designed to have fast appends and pops from both ends.
from collections import deque
queue = deque(['Eric','John','Michael'])
queue.append('Terry')    
queue.append('Graham')
queue.popleft()    # The first to arrive now leaves,first in,first out
queue.popleft()    # The second to arrive now leaves
print queue


# build-in functions for functional programming: filter(),map(),and reduce()
# filter(function,sequence) returns a sequence consisting of those items from the sequence for which function(item) is true.
def f(x):
	return x%3==0 or x%5==0
print filter(f,range(2,25))
print filter(f,(2,3,4,5,6,7,8,9)) # if sequence is tuple, return tuple

def s(x):
	return x=='a' or x=='b'
print filter(s,'abcdefghikba')    # if sequence is string, return string

# map(function,sequence) calls function(item) for each of the sequence's items and returns a list of the return values.
def cube(x): return x ** 3
print map(cube,range(1,11))

# More than one sequence may be passed; the function must then have as many arguments as there are sequences.
seq = range(8)
def add(x,y): return x+y
print map(add,seq,seq) # add has two arguments, so two sequences needed

# reduce(function,sequence) returns a single value constructed by calling function on the first two items of the 
# sequence, then on the result and the next item, and so on. 
def add(x,y) : return x+y
print reduce(add,range(1,11))

def muti(x,y): return x*y
print reduce(muti,range(1,6))
print reduce(muti,[2])    #if there is only one item in the sequence, its value is returned.

# a third argument can be passed to function reduce, the argument indicates the starting value.
# add function is first addlied to the starting value and the first sequence item, than to the result and the next item
def my_sum(seq):
	def add(x,y): return x+y
	return reduce(add,seq,1)
print my_sum(range(1,11))    
print my_sum([1])
print my_sum([])

# system build-in function: sum
print sum((1,2,3))
print sum([1,2,3])

# List Comprehensions
squares = []
for x in range(10):
	squares.append(x**2)
print squares

# We can obtain the same result with:
squares = [x**2 for x in range(10)]    # more concise and readable
print squares

# This is also equivalent to :
def f(x):
	return x**2
squares = map(f,range(10))
print squares

# This is also equivalent to :
squares = map(lambda x: x**2, range(10))
print squares

# Another sample about list comprehension
result = [(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]
print result

# it is equivalent to :
combs = []
for x in [1,2,3]:
	for y in [3,1,4]:
		if x != y:
			combs.append((x,y))
print combs

# Nested List Comprehensions
matrix = [
	[1,2,3,4],
	[5,6,7,8],
	[9,10,11,12]
]

# The following list comprehension will transpose rows and columns:
matrix_transpose = [[row[i] for row in matrix] for i in range(4)]
print matrix_transpose

# This is equivalent to:
transposed = []
for i in range(4):
	transposed.append([row[i] for row in matrix])
print transposed

# Which,in turn, is the same as:
transposed = []
for i in range(4):
	transposed_row = []
	for row in matrix:
		transposed_row.append(row[i])
	transposed.append(transposed_row)
print transposed

# built-in functions to transpose rows and columns: zip
print zip(*matrix)

# del statement
a = [-1,1,66.25,333,333,1234.5]
del a[0]
print a
del a[2:4]
print a
del a[:]
print a
del a    # delete the entire list

