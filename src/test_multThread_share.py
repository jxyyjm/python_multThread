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
		print 'test_queue_write :', a, ctime()
		queue.put(a)
def test_queue_read(lock):
	with lock:
		while True:
			if queue.empty() == False:
				print queue.get(block=True) 
				##这里的block不管外面的用，只是对queue的get管用##
			else: break
def test_dict_write(a, lock):
	with lock:
		dic[str(a)] = a**2
		print 'test_dict_write :', a, ctime()
def test_dict_read(lock):
	with lock:
		#for k, v in dic.items():
		print 'test_dict_read, ', ctime(), dic
def test_list_write(a, lock):
	with lock:
		list.append(a)
		print 'test_list_write :', a, ctime()
def test_list_read(lock):
	with lock:
		print 'test_list_read, ', ctime(), list
def test_pipe_write(a, lock):
	## pipe is used between two ##
	## queue is used among them ##
	pass
def test_pipe_read(lock):
	pass
if __name__=='__main__':
	time_begin  = ctime()
	Thread_pool = dummy.Pool(10)
	queue       = dummy.Manager().Queue()
	dic         = dummy.Manager().dict()
	list        = dummy.Manager().list()
	print 'current thread  : ', dummy.current_process
	print 'current process : ', multiprocessing.current_process
	lock = dummy.Lock()
	for i in xrange(7):
		Thread_pool.apply_async(test_queue_write, args=(i, lock))
		Thread_pool.apply_async(test_queue_read,  args=(lock, ))
		Thread_pool.apply_async(test_dict_write,  args=(i, lock))
		Thread_pool.apply_async(test_dict_read,   args=(lock,))
		Thread_pool.apply_async(test_list_write,  args=(i, lock))
		Thread_pool.apply_async(test_list_read,   args=(lock,))
	Thread_pool.close()
	Thread_pool.join()
	print 'queue as following:(here queue had been empty, because queue.get above)'
	test_queue_read(lock)
	print 'dict as following:'
	test_dict_read(lock)
	time_end = ctime()
	print 'current thread  : ', dummy.current_process
	print '== last =='
	print 'time begin :', time_begin
	print 'time end   :', time_end
	print 'Manager 的各个变量，可以在进程之间相互共享'

