# !/usr/bin/env python
# -*- encoding:utf-8 -*-
# server.py
# wsgiref是Python内置的一个WSGI服务器参考实现
from wsgiref.simple_server import make_server
from hello import application

# 创建一个服务器，IP地址为空，端口是8888，处理函数是application httpd =
make_server('',8888,application) print "Serving HTTP on port 8888..."
httpd.serve_forever()

# 在浏览器访问localhost:8888即可访问服务
