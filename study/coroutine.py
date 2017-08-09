# -*- encoding:utf-8 -*-
# 协程，又称微线程，英文名Coroutine
# 子程序，或者成为函数，在所有语言中都是层级调用，比如A调用B，B在执行中又调用了C，C执行完毕返回，B执行完毕返回，
# 最后是A执行完毕
# 所以子程序调用是通过栈实现的,一个线程就是一个子程序,子程序调用就是一个入口,一次返回
# 协程看上去也是子程序,但执行过程中,在子程序内部可中断,然后转而执行别的子程序,在适当的时候再返回来接着执行
# 在一个子程序中中断，去执行其他子程序，有点类似于CPU的中断。比如子程序A、B：
def A():
	print '1'
	print '2'
	print '3'

def B():
	print 'x'
	print 'y'
	print 'z'

# 假设由协程执行，在执行A的过程中，可以随时中断，去执行B，执行结果可能是：
# 1
# 2
# x
# y
# 3
# z

# 协程的特点是一个线程执行，而不是多线程，尽管和多线程很像
# 和多线程比，协程的子程序切换不是线程切换，没有线程切换的开销，因此效率很高
# 协程的第二大优势是多线程的锁机制，因为只有一个线程，也不存在写变量冲突，在协程中控制共享资源不加锁，
# 只要判断状态就好了,所以执行效率比多线程高好多
# Python对协程的支持非常有限，用在generator的yield可以一定程度上实现协程
# 下面例子将生产者-消费者模型改用协程实现，生产者生产消息后，直接通过yield跳转到消费者开始执行，
# 待消费者执行完毕后，切换回生产者继续生产，效率极高

import time
def consumer():
	r = ''
	while True:
		n = yield r
		if not n:
			return
		print('[CONSUMER] Consuming %s...' % n)
		time.sleep(1)
		r = '200 OK'

def produce(c):
	c.next()
	n = 0
	while n < 5:
		n = n+1
		print('[PRODUCER] Producing %s...' % n)
		r = c.send(n)
		print('[PRODUCER] Consumer return:%s' % r)
	c.close()

if __name__ == '__main__':
	c = consumer()
	produce(c)

# 注意到consumer函数是一个generator，把一个consumer传入produce后：
# (1)首先，调用c.next()启动生成器
# (2)然后，一旦生产了东西，通过c.send(n)切换到consumer执行
# (3)consumer通过yield拿到消息，处理，又通过yield把结果传回
# (4)produce拿到consumer处理的结果，继续生产下一条消息
# (5)produce决定不生产了，通过c.close()关闭consumer，整个过程结束
# 整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务
# Python通过yield提供了对协程的支持，但是不完全，而第三方的gevent为Python提供了比较完善的协程支持，详见gevent.py