# !/usr/bin/env python
# -*- encoding:utf-8 -*-
import re
email1 = 'someone@gmail.com'
email2 = 'bill.gates@microsoft.com'
email3 = '<Tom Paris> tom@voyager.org'

if(re.match(r'^\w+@\w+.com$',email1)):
	print 'OK'
else:
	print 'NOT MATCH'


if(re.match(r'^[\w.]+@\w+.com$',email2)):
	print 'OK'
else:
	print 'NOT MATCH'

if(re.match(r'^[\w.]+@\w+.com$',email1)):
	print 'OK'
else:
	print 'NOT MATCH'


if(re.match(r'^[\w\s<>.]+@\w+.(com|org)$',email3)):
	print 'OK'
else:
	print 'NOT MATCH'

if(re.match(r'^[\w\s<>.]+@\w+.(com|org)$',email2)):
	print 'OK'
else:
	print 'NOT MATCH'

if(re.match(r'^[\w\s<>.]+@\w+.(com|org)$',email1)):
	print 'OK'
else:
	print 'NOT MATCH'