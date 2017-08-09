# -*- encoding:utf-8 -*-

import gevent
from gevent import monkey; monkey.patch_all()
import urllib2

def f(url):
    print('GET:%s' % url)
    resp = urllib2.urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data),url))

gevent.joinall([
        gevent.spawn(f,'https://www.python.org/'),
        gevent.spawn(f,'https://www.yahoo.com/'),
        gevent.spawn(f,'https://github.com/'),
])
# 三个网络操作是并发执行的，而且顺序不同，但只有一个线程

