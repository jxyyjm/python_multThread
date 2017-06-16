#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
	lock 要放到需要保护的共享变量位置，当对其修改时。
	不要将耗时的也放过去
	===============================================
	对多线程的共享锁，可以用dummy.Lock()
	也可以用lock = dummy.Manager().Lock()
'''

import multiprocessing.dummy as multiprocessing
from time import ctime, sleep

def test1(msg):
	print 'msg : ', msg, ctime()
	sleep(3) ## here is help to check time-sync/async
	print 'test1 end'
def test2(msg, dic):
	with lock:
		dic[msg] = msg
		sleep(2)
	return 1
def test3(msg, dic):
	with lock:
		dic[msg] = msg
	sleep(2) ## 将耗时的部分放到lock外面，否则并行无意义 ##
	return 1
def callback_cost_longer(a):
	for i in xrange(1000000):
		a = a**2
		a = a**3
		a = a**4
		a = a%4
if __name__=='__main__':
	time_begin = ctime()
	pool = multiprocessing.Pool(processes = 3)
	dic  = multiprocessing.Manager().dict()
	#lock = multiprocessing.Lock()
	lock = multiprocessing.Manager().Lock()
	Num  = []
	for i in xrange(5):
		msg = 'hello'+ str(i)
		#pool.apply_async(test1, (msg, ))
		#pool.apply_async(test2, (msg, dic))
		#pool.apply_async(test3, (msg, dic))
		#pool.apply_async(test3, (msg, dic), callback=Num.append)
		pool.apply_async(test3, (msg, dic), callback=callback_cost_longer)
	print '== mark =='
	pool.close() ## 调用pool.close()，这样就不会有新的进程加入到pool里面 ##
	pool.join()
	for k, v in dic.items():
		print k,v
	print 'sub-process done', ctime()
	time_end   = ctime()
	print 'all num of run test2 : ', Num
	print 'time begin : ', time_begin
	print 'time end   : ', time_end

