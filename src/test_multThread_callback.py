#!/usr/bin/python
# -*- coding:utf-8 -*-

import multiprocessing
from time import ctime, sleep
from multiprocessing import dummy
'''
	callback only exit when async 
'''

def test_fun(a, lock):
	with lock:
		b = a
		a += a
		a = a/2
		a = a%2
		a = a+1
		a = a**2
		print 'test fun :', b, ctime(), 'res :', a
		return a
		## here, must get a return ##
def print_test_res(a):
	## callback function must get an arg input ##
	## callback 函数默认接收前面func的返回值   ##
	with lock:
		print 'callback get input is : ', a

if __name__=='__main__':
	time_begin  = ctime()
	Thread_pool = dummy.Pool(4)
	lock        = dummy.Lock()
	result      = []
	for i in xrange(10):
		#Thread_pool.apply_async(test_fun, args=(i, lock), callback=print_test_res)
		Thread_pool.apply_async(test_fun, args=(i, lock), callback=result.append)
	Thread_pool.close()
	Thread_pool.join()
	time_end = ctime()
	print 'result :', result
	print '== last =='
	print 'time begin :', time_begin
	print 'time end   :', time_end

