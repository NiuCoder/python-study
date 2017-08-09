# -*- encoding:utf-8 -*-
# 多任务可以由多进程完成，也可以由一个进程内的多线程完成。
# 线程是操作系统直接支持的执行单元，因此，高级语言都内置多线程的人支持。Python的线程是真正的Posix Thared
# 而不是模拟出来的线程
# Python的标准库提供了两个多线程模块，thread和threading，thread是低级模块，threading是高级模块，对thread进行了封装
# 绝大多数情况，使用threading，启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行

import time,threading
# 新线程执行的代码：
def loop():
	print 'thread %s is running...' % threading.current_thread().name
	n = 0
	while n < 5:
		n = n + 1
		print 'thread %s >>> %s' % (threading.current_thread().name,n)
		time.sleep(1)
	print 'thread %s ended.' % threading.current_thread().name

print 'thread %s is running...' % threading.current_thread().name
t = threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print 'thread %s ended.' % threading.current_thread().name

# 新进程执行代码中看来只执行while中的部分
