# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# hello.py
# 符合WCGI标准的HTTP处理函数
def application(environ,start_response):
	start_response('200 ok',[('Content-Type','text/html')])
	return '<h1>Hello,web!<br/>Hello,%s!</h1>' % (environ['PATH_INFO'][1:] or 'web')

# 这个函数可以看作是Web应用程序的入口函数，无论多复杂的Web应用，都有一个WSGI处理函数。
# 复杂的Web应用还需要在WSGI上抽象出Web框架，进一步简化Web开发。
