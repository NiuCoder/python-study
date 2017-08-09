# -*- encoding:utf-8 -*-
# 网络通信就是两个进程之间的通信
# 互联网协议包含了上百种，但是最重要的是TCP和IP协议，简称TCP/IP
# 通信的时候，双方必须知道对方的标识，好比发邮件必须知道对方的邮件地址，互联网上每个计算机的唯一标识是IP地址
# 如果一台计算机同时接入到两个或更多的网络，比如路由器，他就会有两个或多个IP地址，所以IP地址实际上是计算机的
# 网络接口，通常是网卡
# IP协议负责把数据从一台计算机通过网络发送到另一台计算机。IP包的特点是按块发送，途径多个路由，但不保证到达，
# 也不保证顺序到达
# TCP协议建立在IP协议之上， 负责在两台计算机之间建立可靠连接，保证数据按顺序到达。TCP协议会通过握手建立
# 连接，然后，对每个IP包编号，确保对方按顺序收到，如果包丢掉了，就自动重发
# IP包除了传输的数据，还包括源和目标的IP地址以及各自的端口。
# 两个进程在两台计算机之间建立网络连接需要各自的IP地址和各自的端口号
# 一个进程也可能同时与多个计算机建立连接，因此它会申请很多端口

# 以下是一个TCP客户端程序的示例
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 建立连接
s.connect(('www.sina.com.cn',80))
# 发送HTTP请求
s.send('GET / HTTP/1.1\r\nHost:www.sina.com.cn\r\nConnection:close\r\n\r\n')

buffer = []
while True:
	# 接受请求返回数据
	d = s.recv(1024)
	if d:
		buffer.append(d)
	else:
		break
data = ''.join(buffer)
s.close()

header,html = data.split('\r\n\r\n',1)
print header
# 将html内容写入文件中
with open('sina.html','wb') as f:
	f.write(html)
