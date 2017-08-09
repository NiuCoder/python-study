# -*- encoding:utf-8 *-*
# windows下可以用python的multiprocessing模块来编写多进程的程序
from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
	print 'Run child process %s (%s)...' % (name,os.getpid())

if __name__ == '__main__':
	print 'Parent process %s.' % os.getpid()
	p = Process(target=run_proc,args=('test',))
	print 'Process will start.'
	p.start()
	p.join()
	print 'Process end.'

# 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，这样创建进程比fork()还简单
# join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步



