#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
	good-profile
	1) handle both optional and positional arguments (getopt can also do this)
	2) produce highly informative usage messages (it looks meanless)
	3) support parser that dispatch to sub-parsers ( 参数传递到下一级 )
'''
import sys
import argparse

parser = argparse.ArgumentParser(
		description = 'sum the integers at the command line'
		)
parser.add_argument(
		'integers', metavar='int', nargs='+', type=int,
		help='an integer to be summed'
		)
parser.add_argument(
		'--log', default=sys.stdout, type=argparse.FileType('w'),
		help='the file where the sum should be written'
		)
args = parser.parse_args()
args.log.write(str(args.integers))
args.log.close()
