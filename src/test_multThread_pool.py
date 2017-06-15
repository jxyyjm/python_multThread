#!/usr/bin/python
# -*- coding:utf-8 -*-

import multiprocessing
from time import ctime, sleep
from multiprocessing import dummy
'''
## dummy is the same as threading ##
## notice:: useage is as same as multiprocess                                                   ##
##          so, if PROCESS, import multiprocessing as multiprocessing                           ##
##              if THREAD,  import multiprocessing,dummy as multiprocessing                     ##
##          and other code did not change anthing, it will exchange multiProcess or multiThread ##
##          however, share-variable only has Queue, Pipe
## threading没有线程池的概念，而dummy有池，这是更好使的地方 ##
'''

def test_fun(a, lock):
	with lock:
		b = a
		a += a
		a = a/2
		a = a%2
		a = a+1
		a = a**2
		print 'test fun :', b, ctime()

if __name__=='__main__':
	time_begin  = ctime()
	Thread_pool = dummy.Pool(4)
	queue       = dummy.Manager().Queue()
	print 'current thread  : ', dummy.current_process
	print 'current process : ', multiprocessing.current_process
	lock = dummy.Lock()
	for i in xrange(10):
		Thread_pool.apply_async(test_fun, args=(i, lock))
		#Thread_pool.apply(test_fun, args=(i, lock))
	Thread_pool.close()
	Thread_pool.join()
	print 'current thread  : ', dummy.current_process
	time_end = ctime()
	print '== last =='
	print 'time begin :', time_begin
	print 'time end   :', time_end

