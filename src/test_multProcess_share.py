#!/usr/bin/python
# -*- coding:utf-8 -*-

from time import ctime, sleep
from multiprocessing import Process, Queue, Array, Manager, Pool, Lock

'''
	Queue: 子进程间通信,
	缺点：不支持Pool
'''
def test_queue_write(queue):
	for i in ['hello', 'word', 'what', 'you', 'want']:
		queue.put(i)
		print 'put time : ', ctime(), i
		#sleep(2)
def test_queue_read(queue):
	while True:
		if not queue.empty():
			v = queue.get(True)
			print 'read time: ', ctime(), v
		else: break
def test_queue():
	q = Queue() ## 创建列表 ##
	p1 = Process(target = test_queue_write, args=(q,))
	p1.start()
	p1.join() ## 等待write 执行完 ##
	p2 = Process(target = test_queue_read,  args=(q,))
	p2.start()
	p1.join()
'''
	Manager: 子进程间通信
	优点：适用于Pool
'''
def test_Manager_write(share_par, v):
	with lock:
		#lock.acquire() ## 为什么加上锁就不行了, 因为要加全局的锁 ##
		share_par.append(v)
		print ctime(), 'writ', len(share_par), share_par
		#lock.release()
def test_Manager_read(share_par):
	with lock:
		print ctime(), 'read', len(share_par), share_par
		#share_par.pop() ## 好像没有起作用 ##
		#print ctime(), 'read', len(share_par), share_par
def test_Manager():
	lists = Manager().list() ## 创建子进程 共享变量 ## list里面可以放任意东西 ##
	print len(lists), 'begin'
	pool  = Pool()
	for i in xrange(10):
		print len(lists), ctime()
		if len(lists)<=0: ## 为什么这个是<=0??? ##
			pool.apply_async(test_Manager_write, args=(lists,i))
		else:
			pool.apply_async(test_Manager_read, args=(lists))
			break
	pool.close()
	pool.join()
	print lists ## 子进程间的共享变量，没法被主进程读取到 ## 所以为空 ##

if __name__=='__main__':
	lock  = Lock() ## notice: lock 必须是全局的 ##
	#print ' === test Queue   === '
	#test_queue()
	#sleep(5)
	print ' === test Manager === '
	test_Manager()


