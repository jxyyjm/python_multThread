#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
	接收从命令行来的以命名指定的参数
	getopt,更优先用argparse模块
'''

import sys, getopt

def main(argv):
	inputfile = ''
	outputfile = ''
	try:
		opts, args = getopt.getopt(argv,"i:o:",["ifile=","ofile="])
		'''
			opts 获取 [(option, opt-value)]
			args 获取 [sys.argv[1], sys.argv[2]]
			"short-opt1:short-opt2:short-opt3:" 短格式支持 -
			["long-opt1=", "long-opt2"]         长格式支持 --
		'''
		print 'opts:', opts
		print 'args:', args
	except getopt.GetoptError:
		print 'test_opt.py -i <inputfile> -o <outputfile>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'test_opt.py -i <inputfile> -o <outputfile>'
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg
			print '输入的文件为：', inputfile
			print '输出的文件为：', outputfile

if __name__ == "__main__":
	main(sys.argv[1:])
'''
	 #test#
	 python test_opt.py -h
	 python test_opt.py -i 'inputfile1' -o 'outfile2'
'''
