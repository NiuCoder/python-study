
# print 'The quick brown fox','jump over','the lazy dog'

# name = raw_input('please enter your name:')

# print 'hello',name


# Many values, such as numbers or structures like lists and dictionaries, have the same representation using either function.
# String and floating point number, in particular, have two distinct representations.
s = 'Hello,world.'
print s
print str(s)
print repr(s)

print 1.0/7.0
print str(1.0/7.0)
print repr(1.0/7.0)

# format output
for x in range(1,11):
	# print x,x*x,x*x*x
	print '{0:2d} {1:3d} {2:4d}'.format(x,x*x,x*x*x)

print '12'.zfill(5)
print '-3.14'.zfill(7)
print '3.14159265359'.zfill(5)
print 'We are the {} who say "{}"!'.format('knights','Ni')

print '{0} and {1}'.format('spam','eggs')
print '{1} and {0}'.format('spam','eggs')

print 'This {food} is {adjective}.'.format(food='spam',adjective='absolutely horrible')

print 'The story of {0},{1}, and {other}.'.format('Bill','Manfred',other='Georg')

table={'Sjoerd':4127,'Jack':4098,'Dcab':7678}
for name,phone in table.items():
	print '{0:10} ==> {1:10d}'.format(name,phone)

import math
print 'The value of PI is approximately %5.3f.' % math.pi

