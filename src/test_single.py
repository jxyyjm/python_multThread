#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import sys
import gzip
reload(sys)
sys.setdefaultencoding('utf-8')
from time import ctime
from multiprocessing import dummy as multiprocessing
#import multiprocessing

def check_file(filepath):
	handle = gzip.GzipFile(filepath, 'r')
	print ctime(), filepath
	for line in handle:
		line = str(line).strip()
		if len(line) <= 0: continue
		#print line
		if line.find('山东省')>=0:
			if dic.has_key('山东省'):
				dic['山东省'] += 1
			else:dic['山东省'] = 1
		if line.find('北京市')>=0:
			if dic.has_key('北京市'):
				dic['北京市'] +=1
			else:dic['北京市'] = 1
	handle.close()

if __name__=='__main__':
	time_begin = ctime()
	dic		= {}
	rootDir	= './20170614'
	for root,dirs,files in os.walk(rootDir):
		for filespath in files:
			filename = os.path.join(root,filespath)
			#print 'input here :', filename
			check_file(filename)
			#print 'after pool.apply_async', dic
	print 'result:'
	for k, v in dic.items():
		print k, v
	time_end = ctime()
	print 'time begin is : ', time_begin
	print 'time end   is : ', time_end

