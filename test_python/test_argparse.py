#! /usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description='this is a demo program')
parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
parser.add_argument('-p', '--path', default='a/b/c', help='the path to store')
parser.add_argument('page', type=int,choices=xrange(1, 101), metavar='PAGE', nargs='+', help='range of page or which pages')  #

arg = parser.parse_args()
print arg
#print arg.version
print arg.path
if len(arg.page) == 2:
    print arg.page[0], arg.page[1]
else:
    print sorted(set(arg.page), reverse=True)
