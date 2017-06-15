#usr/bin/python
# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import threading
from time import ctime, sleep

'''
	threading is a baseTreading-package.
	if use threading_pool, you will need multiprocessing.dummy.
	it will be better.
'''

def music(name):
	for i in range(2):
		print "I was listening to", name, ctime()
		sleep(1)

def move(name):
	for i in range(2):
		print "I was at the ", name, ctime()
		sleep(5)
def print_tribution(thread):
		print thread
		print 'before setDaemon: ', thread.daemon
		print 'after  setDaemon: ', thread.daemon
		print 'thread name     : ', thread.name
		print 'thread alive    : ', thread.isAlive()
		print 'thread ident    : ', thread.ident
	
def testDaemon(threads):
	## if setDaemon==True, mainThread will kill subThread when exit ##
	for t in threads:
		t.setDaemon(True)
		t.start()
		#print_tribution(t)
	print ' === when setDaemon, subthread will quit while main thread over === '
	print ' === so, move cost 5s/each loop, will only run once ==='
def testJoin(threads):
	for t in threads:
		t.start()
		### 将线程，从"新建状态" 启动为 ==> "等待CPU调度状态" ##
		print print_tribution(t)
	for t in threads:
		t.join()
	print ' === when join, main thread will wait until subthread over or timeout === '
	
if __name__=='__main__':
	threads = []
	t1 = threading.Thread(target=music, name='first thread', args=('分手快乐',))
	threads.append(t1)
	t2 = threading.Thread(target=move,  name='second thread', args=('阿凡达',))
	threads.append(t2)
	mainThread = threading.currentThread().getName()
	print 'current main thread is : ', mainThread
	sleep(1)
	#print ' ======= testDaemon ======== '
	#testDaemon(threads)
	print ' ======= testJoin ======= '
	testJoin(threads)
	sleep(2)
	print 'mainThread all over : ', ctime() 
