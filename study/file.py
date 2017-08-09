# f=open('test.txt','r')
f = open('test.txt','r+')
print f.readline()
print f.readline()
print f.readline()

for line in f:
	print line

# f = open('test.txt','w')
f.write('This is a test\n')
print f.tell()

f.close()

import json
print json.dumps([1,'simple','list'])
