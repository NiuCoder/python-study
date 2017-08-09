# the structure of dict is same as json

d = {'Michael':95,'Bob':75,'Tracy':85}
print d['Michael']

d['Jack'] = 80
d['Adam'] = 67

print d

print d.get('Bob')

print d.keys()
print d.values()

print 'Bob' in d

del d['Tracy']
print d

# dict() constructor builds dictionaries from sequences of key-value pairs
dist = dict([('sape',4138),('guido',4127),('jack',4098)])
print dist

# dict comprehension
print {x:x**2 for x in (2,4,6)}

# when the keys are simple strings, sometimes is easier
print dict(sape=4139,guido=4127,jack=4098)

# Looping Techniques
# retrieve the position index and corresponding value at the same time using the enumerate()
for i,v in enumerate(['tic','tac','toe']):
	print i,v

# loop over two or more sequences at the same time, using zip()
questions = ['name','quest','favorite color']
answers = ['lancelot','the holy grail','blue']
for q,a in zip(questions,answers):
	print 'What is your {0}? It is {1}.'.format(q,a)

# reverse a sequence
for i in reversed(xrange(1,10,2)):
	print i,

# loop in sorted order
basket = ['apple','orange','apple','pear','orange','banana']
for f in sorted(set(basket)):
	print f


# loop through dictionaries, using iteritems()
knights = {'gallahad':'the pure','robin':'the brave'}
for k,v in knights.iteritems():
	print k,':',v

# The Boolean operators and and or are so-called short-circuit operators: their arguments are evaluated from left to right
# and evaluation stops as soon as the outcome is determined.
string1,string2,string3 = '','Trondheim','Hammer Dance'
non_null = string1 or string2 or string3
print non_null

print (1,2,3) < (1,2,4)
print 'ABC' < 'BCD'
print 'ABC' < 'ABD'
print 'ABC' < 'ABC'
print (1,2) < (1,2,-1)
print (1,2,3) == (1.0,2.0,3.0)

