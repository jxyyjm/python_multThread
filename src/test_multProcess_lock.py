#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
	多进程，对共享资源，比如print, 贡献变量，也需要加锁。
	lock = multiprocessing.Manager().Lock
'''

import os
import sys
import gzip
import time
import json
reload(sys)
sys.setdefaultencoding('utf-8')
from time import ctime, sleep
#from multiprocessing import dummy as multiprocessing
import multiprocessing as multiprocessing
# 有个疑问是 多进程加锁，程序不能正常执行 #
def test_async(lock):
	with lock:
		print ctime(), 'test_async'
		sleep(2);

def check_file(filepath, dic, lock):
	#print ctime(), 'has been in check_file', filepath
	handle = gzip.GzipFile(filepath, 'r')
	print ctime(), filepath
	cur_dic  = {}
	for line in handle:
		line = str(line).strip()
		if len(line) <= 0: continue
		if line.find('山东省')>=0:
			if cur_dic.has_key('山东省'):pass
			else:cur_dic['山东省'] = 0
			cur_dic['山东省'] +=1
		if line.find('北京市')>=0:
			if cur_dic.has_key('北京市'):pass
			else:cur_dic['北京市'] = 0
			cur_dic['北京市'] +=1
	handle.close()
	with lock:
		if dic.has_key('山东省'):
			dic['山东省'] += cur_dic['山东省']
		else: dic['山东省'] = cur_dic['山东省']
		if dic.has_key('北京市'):
			dic['北京市'] += cur_dic['北京市']
		else: dic['北京市'] = cur_dic['北京市']
		
def save_file(lock, dic):
	with lock:
		print ctime(), 'has been in save_file'
		filepath = './result.callback'
		handle = open(filepath, 'a')
		print ctime(), 'save path is :', filepath
		for k, v in dic.items():
			handle.write(json.dumps(k, ensure_ascii=False) +'\t'+ str(v) +'\t'+ctime()+'\n')
		handle.close()

if __name__=='__main__':
	time_begin = ctime()
	pool = multiprocessing.Pool(10)
	dic  = multiprocessing.Manager().dict()
	lock = multiprocessing.Manager().Lock()
	## 多进程的共享锁，需要用Manager来定义 ##
	rootDir = './20170614'
	for root,dirs,files in os.walk(rootDir):
		for filespath in files:
			filename = os.path.join(root,filespath)
			print 'input filename :', filename
			pool.apply_async(check_file, args=(filename, dic, lock))
			pool.apply_async(save_file, args=(lock, dic))
	print '=== acitve process === '
	p_list = multiprocessing.active_children()
	for p in p_list:
		print p, p.name, p.daemon
	pool.close()
	pool.join()
	time_end = ctime()
	print 'result dict here is :'
	for k, v in dic.items():
		print k, v
	#save_file(lock, dic)
	print 'time begin is : ', time_begin
	print 'time end   is : ', time_end


