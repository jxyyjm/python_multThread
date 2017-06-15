#!/usr/bin/python
# -*- coding:utf-8 -*-

import multiprocessing
from time import ctime, sleep

def test1(msg):
	print 'msg : ', msg, ctime()
	sleep(3) ## here is help to check time-sync/async
	print 'test1 end'
def test_async():
	pool = multiprocessing.Pool(processes = 3)
	for i in xrange(5):
		msg = 'hello', str(i)
		pool.apply_async(test1, (msg,))
		## 异步的 ## asynchronous ## 这四次循环是并行的 ##
		## 在异步的情况下，发现进程池满载是3个进程，最开始的三个函数开始时间是同一时刻 ##
		## 然后，一旦进程池子里有资源空闲出来，则自动启动剩余的进程 ##
	print '== mark =='
	pool.close() ## 调用pool.close()，这样就不会有新的进程加入到pool里面 ##
	pool.join()
	print 'sub-process done', ctime()
def test_sync():
	pool = multiprocessing.Pool(processes = 3)
	for i in xrange(5):
		msg = 'hello', str(i)
		pool.apply(test1, (msg,))      
		## 同步的 ## synchronous  ## 这四次循环是串行的 ##
		## 在同步的情况下，会在当前进程执行完毕后，才会执行下一个进程 ##
	print '== mark =='
	## notice : 这里的 == mark == 标记，会等待上面的进程池执行之后才执行 ##
	pool.close() ## 调用pool.close()，这样就不会有新的进程加入到pool里面 ##
	pool.join() #pool.terminate() ## or pool.join() ##
	print 'sub-process done', ctime()
def test_join():
	pool = multiprocessing.Pool(processes = 3)
	for i in xrange(5):
		msg = 'hello', str(i)
		pool.apply_async(test1, (msg,))
	print '== mark =='
	## 发现 == mark == 标记，会在进程池的所有进程之前 执行               ##
	## 为什么呢？主进程，难道在pool.apply_async时，会更先执行            ##
	pool.close() ## 调用pool.close()，这样就不会有新的进程加入到pool里面 ##
	pool.join()
	## 阻塞主进程，等待子进程的退出                                ##
	## 所以就有了== mark == 标记执行完毕后，仍然在执行进程池的进程 ##
	print 'sub-process done', ctime()
def test_terminate():
	pool = multiprocessing.Pool(processes = 3)
	for i in xrange(5):
		msg = 'hello', str(i)
		pool.apply_async(test1, (msg,))
		#pool.apply(test1, (msg,))
	print '== mark =='
	pool.close() ## 调用pool.close()，这样就不会有新的进程加入到pool里面 ##
	pool.terminate()
	## 结束工作进程，不再处理未完成的任务 ## 
	## 如果这样，就有了两个test1的前半部分 print msg，后面的sleep(3)未执行完毕，就被退出了。##
	print 'sub-process done', ctime()


if __name__=='__main__':
	print '============================'
	print '=== test 异步 pool.apply_async === ', ctime()
	test_async()
	print '============================'
	print '=== test 同步 pool.apply       === ', ctime()
	test_sync()
	print '============================'
	print '=== test 阻塞 pool.join        === ', ctime()
	test_join()
	print '============================'
	print '=== test 非阻 pool.terminate   === ', ctime()
	test_terminate()
	print '============================================'
	print 'pool.apply_async在于控制所有进程的异步, 包括主进程'
	print 'pool.apply在于控制所有进程的同步，包括主进程(很奇怪)'
	print 'pool.join 当主进程结束时，需要等待子进程(pool)的结束'
	print 'pool.terminate 当主进程结束时，不等待子进程'
