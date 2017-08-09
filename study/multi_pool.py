# -*- encoding:utf-8 -*-
# Pool，如果要启动大量的子进程，可以用进程池的方式批量创建子进程
from multiprocessing import Pool
import os,time,random

def long_time_task(name):
	print 'Run task %s (%s)...' % (name,os.getpid())
	start = time.time()
	time.sleep(random.random() * 3)
	end = time.time()
	print 'Task %s runs %0.2f seconds. From %0.2f to %0.2f' % (name,(end-start),start,end)

if __name__ == '__main__':
	print 'Parent process %s.' % os.getpid()
	p = Pool()
	for i in range(5):
		p.apply_async(long_time_task,args=(i,))
	print 'Waiting for all subprocesses done...'
	p.close()
	p.join()
	print 'All subprocesses done.'
# 对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须调用close(),调用close()之后就不能继续添加新的Process了

# 进程间通信
# Process之间肯定是要通信的，操作系统提供了很多机制来实现进程间的通信。
