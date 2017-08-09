# -*- encoding:utf-8 -*-
# 多线程---Lock
# 多线程和多进程的最大不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，
# 多线程中，所有变量都由所有线程共享
import time,threading

# 银行存款
balance = 0

def change_it(n):
	# 先存后取，结果应该为0
	global balance
	balance = balance + n
	print balance
	balance = balance - n
	print balance

# 不加锁的版本会让存取顺序变乱，导致结果可能不为0，因为高级语言的一条语句在CPU执行时是若干语句
# def run_thread(n):
# 	for i in range(10000):
# 		change_it(n)

# 加锁的版本，保证线程同步
lock = threading.Lock()
def run_thread(n):
    for i in range(100000):
    	# 先获得锁
    	lock.acquire()
    	try:
    		change_it(n)
    	finally:
    		lock.release()


t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print balance

# 当多个线程同时执行lock.acquire()时，只有一个线程能够成功获取锁，然后继续执行代码，其他线程就继续等待直到获得锁为止。
# 获得锁的线程用完后一定要释放锁，否则那些等待锁的线程将会永远等待下去，成为死线程。所以我们用try...finally来确保锁
# 一定会被释放

# Python解释器在执行时有一个GIL锁：Global Interpreter Lock，任何Python线程在执行前，必须先获得GIL锁，然后，每执行100条
# 字节码，解释器就会自动释放GIL锁，让别的线程有机会执行。因此Python永远无法利用多核多线程，只能用到1核
# 不过可以用多进程来实现多核任务。
