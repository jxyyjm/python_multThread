#!/usr/bin/python
# -*- coding:utf-8 -*-

import argparse

'''
	main-function get all the arguments.
	dispatch them into specify sub-function. like svn checkout, svn update, svn commit
	parser.add_subparser() here is needed.

	ArgumentParser.add_subparsers(
		title --> title for the sub-parser.
		description --> 
		prog  --> sub-conmmand help program-name
		parser_class-->
		action--> 
		dest  --> 
		help  -->
		metavar
		)
	notice:::: only one sub-function can get the argumens !!!
			   只能携带一个子函数的参数。
			   先指定子函数，再给出待输入的参数。
	if you want some sub-function can get the argument at the same time, only pass them into main-function			
'''
# 1) create the top-level parser #
parser = argparse.ArgumentParser(prog='main-PROG')
parser.add_argument(
		'--foo',
		action = 'store_true',
		help   = 'foo help',
		)
# 2) create sub-commands with the add_subparsers(),
#    which has only one-methed named 'add_parser',
#    whose function is add sub-parser
subparser = parser.add_subparsers(
		title = 'subcommds',
		help  = 'sub-command help',
		description = 'valid subcommands'
		)

# 3) create the parser for the 'a' command
parser_a = subparser.add_parser('a', help='a help')
parser_a.set_defaults(func='a') ## 强调保证执行 a sub-command-line ##
parser_a.add_argument(
		'-update',
		type = int,
		help = 'update help',
		choices = range(10)
		)
parser_a.add_argument(
		'-update2',
		type = int,
		help = 'update2 help',
		choices = range(5)
		)

# 4) create the parser for the 'b' command
parser_b = subparser.add_parser('b', help='b help')
parser_b.set_defaults(func='b')
parser_b.add_argument(
		'-commit',
		type = int,
		help = 'commit help'
		)

args = parser.parse_args()
print args
#print parser.parse_args(['b', '-commit', '99'])
#print parser.parse_args(['--foo', 'b', '-commit', '99'])
#print parser.parse_args(['--foo', 'a', '-update', '8'])
# notice : here is wrong !!! #
#print parser.parse_args(['--foo', 'a', '-update', '8', 'b', '-commit', '99'])

