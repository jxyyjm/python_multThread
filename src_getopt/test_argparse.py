#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
	good-profile
	1) handle both optional and positional arguments (getopt can also do this)
	2) produce highly informative usage messages (it looks meanless)
	3) support parser that dispatch to sub-parsers ( 参数传递到下一级 )
	reference: https://docs.python.org/3/library/argparse.html
'''
import sys
import argparse

## 1) creat an ArgumentParser-object, 
##    which will hold all the info to parse from command-line ##
parser = argparse.ArgumentParser(
		description = 'sum the integers at the command line.'
		)
## 2) tell parser how to take the str-from command-line and turn them into pointed-object ##
##    the info is stored and used when parse_args() is called.
'''
	ArgumentParser.add_argument(
			name or flags --> either a name or a list of option strings, e.g. 'foo' or '-f', '--foo'
			[, action]    --> the basic type of action to-be taken **import**
						  --> 1) action='store'      : 将参数存储起来, default action
						  --> 2) aciton='store_const': 由参数'const'给出指定值
						  e.g. parser.add_argument('--foo', aciton='store_const', const=42)
						       parser.parse_args(['--foo']); Namespace(foo=42)
						  --> 3) action='store_false': e.g. Namespace(foo=False)
						  --> 4) action='store_true' : e.g. Namespace(foo=True)
						  --> 5) action='append'     : 将重复参数输入，存储到list里面
						  --> 6) action='append_const':
						  --> 7) action='count'      : 
						  --> 8) action='help'       :
						  --> 9) action='version'    :
						  e.g. parser.add_argument('--version', action='version', version='%(prog)s 2.0');
							   parser.parse_args(['--version'])

			[, nargs]     --> the num of command-line arguments that should be consumed **imporot**
						  --> 1) nargs='N': 参数后面的多少个数将被收集，into a list.
						  --> 2) nargs='?': 
						  --> 3) nargs='*': all 
						  --> 4) nargs='+': all, generate 'error' when no-command-line argument.
						  --> 5) nargs=argparse.REMAINDER:
			[, const]     --> a constant value required by some action and nargs selections
						  --> 1) when 'action=store_const'/'action=append_const'
						  --> 2) when 'nargs=?'
			[, default]   --> the value produced if argument is absent from then command-line
						  --> give the default-value is command-line argument is not present.
						  e.g. parser.add_argument('--foo', default=42)
							   parser.parse_args([]); Namespace(foo=42)
			[, type]      --> the type will be converted into, for the argmument **import**
						  --> allow any necessary type-checking and type conversion
			[, choices]   --> a container of the allowable values for the argument **import**
						  e.g. parser.add_argument('move', choices=['rock', 'paper', 'scissors']
							   parser.parser_args(['fire']); error,不符合该参数的指定范围
			[, required]  --> whether or not the command-line option maybe omitted(optionals only)
						  --> 必须提供的参数, required=True/False
						  e.g. parser.add_argument('--foo', required=True)
			[, help]      --> a brief description of what the argument does
			[, metavar]   --> a name for the argument in usage messages **import**
			[, dest])     --> the name returned when parse_args() is called **import**
						  --> 参数的名称，对内有效.
'''
parser.add_argument(
		'-i',
		dest    = 'input_file',
		action  = 'store', 
		type    = str,
		help    = 'get the input file'
		)
parser.add_argument(
		'-o',
		dest    = 'output_file', # 对内的名称 #
		action  = 'store',
		type    = str,
		help    = 'get the output file'
		)
parser.add_argument(
		'-integers',
		dest    = 'integers',
		action  = 'store',
		nargs   = '+', # 取所有的，如果没有则提示错误 #
		type    = int,
		choices = xrange(10),
		help    = 'get the intergers'
		)
parser.add_argument(
		'-left_value',
		action  = 'store',
		default = '0', ## 给出默认值 #
		type    = int,
		help    = 'get the lefe-margin-value'
		)
args = parser.parse_args()
print args
print args.input_file
print args.output_file
print args.integers
print args.left_value

