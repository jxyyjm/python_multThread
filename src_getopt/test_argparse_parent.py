#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
	argparse.ArgumentParser
	parser会共享一些arguments,为避免重复定义。
	可以类似继承的方式,将共享的设置继承下。
'''
import argparse

'''
	notice:: add_help=False is must ***import***
'''
parent_parser = argparse.ArgumentParser(add_help=False)
parent_parser.add_argument(
		'-parent::input',
		type    = int,
		action  = 'store',
		default = 'parent-file'
		)
child_parser = argparse.ArgumentParser(parents=[parent_parser])
child_parser.add_argument(
		'-i',
		type   = str,
		action = 'store',
		default= 'child-input-file'
		)
args = child_parser.parse_args(['-parent::input', '2', '-i', 'xxx'])
print args

