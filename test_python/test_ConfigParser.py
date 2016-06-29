#!/usr/bin/env python

from ConfigParser import ConfigParser

if __name__ == '__main__':
    f = ConfigParser({'d1':'dididi', 'd2':'74241'})
    f.read('test4.ini')
    print f.sections()
    print f.options('aaa')
    print f.options('AAA')
    print f.items('aaa')
    print f.items('AAA')
    print repr(f.get('aaa', 'a2'))
    print repr(f.getint('aaa', 'a2'))
    f.write(open('test4-2.ini', 'w'))
