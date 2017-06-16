#!/usr/bin/python
# -*- coding:utf-8 -*-

import multiprocessing
from time import ctime, sleep
from multiprocessing import dummy
'''
	notice:
	1) callback only exit when async ;
	2) callback only input one arg, but this arg can be anyType , what a happy life;
'''

def test_fun(a, lock):
	with lock:
		b = a
		a = a**2
		print 'test fun :', b, ctime(), 'res :', a
		return a
		## here, must get a return ##
def print_test_res(a):
	## callback function must get an arg input ##
	## callback 函数默认接收前面func的返回值   ##
	with lock:
		print 'callback get input is : ', a
def test_fun2(a, lock):
	with lock:
		print 'test fun :', a, ctime()
		return {str(a): str(a**2)}

if __name__=='__main__':
	time_begin  = ctime()
	Thread_pool = dummy.Pool(4)
	lock        = dummy.Lock()
	result      = []
	for i in xrange(10):
		#Thread_pool.apply_async(test_fun, args=(i, lock), callback=print_test_res)
		#Thread_pool.apply_async(test_fun, args=(i, lock), callback=result.append)
		Thread_pool.apply_async(test_fun2, args=(i, lock), callback=print_test_res)
	Thread_pool.close()
	Thread_pool.join()
	time_end = ctime()
	print 'result :', result
	print '== last =='
	print 'time begin :', time_begin
	print 'time end   :', time_end

