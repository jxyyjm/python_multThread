#!/usr/bin/python
# -*- coding:utf-8 -*-

import multiprocessing
from time import ctime, sleep
from multiprocessing import dummy
'''
	share variable is import in threading;
	dummy.Queue-class
	dummy.Pipe
	dummy.Manager()::list, dict, Array, Value, Queue 
	# notice : dummy's usage is the same as multiprocess #
'''

def test_queue_write(a, lock):
	with lock:
		print 'test fun :', a, ctime()
		queue.put(a)
def test_queue_read(queue, lock):
	with lock:
		while True:
			if queue.empty() == False:
				print queue.get(block=True) 
				##这里的block不管外面的用，只是对queue的get管用##
			else: break

if __name__=='__main__':
	time_begin  = ctime()
	Thread_pool = dummy.Pool(4)
	queue       = dummy.Manager().Queue()
	print 'current thread  : ', dummy.current_process
	print 'current process : ', multiprocessing.current_process
	lock = dummy.Lock()
	for i in xrange(10):
		Thread_pool.apply_async(test_queue_write, args=(i, lock))
		Thread_pool.apply_async(test_queue_read,  args=(queue, lock))
	Thread_pool.close()
	Thread_pool.join()
	print 'queue as following:(here queue had been empty, because queue.get above)'
	test_queue_read(queue, lock)
	print 'current thread  : ', dummy.current_process
	time_end = ctime()
	print '== last =='
	print 'time begin :', time_begin
	print 'time end   :', time_end

