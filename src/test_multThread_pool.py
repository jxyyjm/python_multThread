#!/usr/bin/python
# -*- coding:utf-8 -*-

from time import ctime, sleep
from multiprocessing import dummy
## dummy is the same as threading ##
## useage is like multiprocess    ##
## threading没有线程池的概念，而dummy有池，这是更好使的地方 ##

def test_fun(a, lock):
	with lock:
		a += a
		a = a/2
		a = a%2
		a = a+1
		a = a**2

if __name__=='__main__':
	time_begin = ctime()
	Thread_pool = dummy.Pool(4)
	print 'current thread : ', dummy.current_process
	lock = dummy.Lock()
	for i in xrange(100000):
		#Thread_pool.apply_async(test_fun, args=(i, lock))
		Thread_pool.apply(test_fun, args=(i, lock))
	Thread_pool.close()
	Thread_pool.join()
	print 'current thread : ', dummy.current_process
	time_end = ctime()
	print '== last =='
	print 'time begin :', time_begin
	print 'time end   :', time_end

