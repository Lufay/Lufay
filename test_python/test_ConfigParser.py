#!/usr/bin/env python

from configparser import ConfigParser

if __name__ == '__main__':
    f = ConfigParser({'d1':'dididi', 'd2':'74241'})
    f.read('conf.ini')
    print ('sections:', f.sections())
    print ('options[aaa]:', f.options('aaa'))
    print ('options[AAA]:', f.options('AAA'))
    print ('items[aaa]:', f.items('aaa'))
    print ('items[AAA]:', f.items('AAA'))
    print ('get `aaa.a2`:', repr(f.get('aaa', 'a2')))
    print ('getint `aaa.a2`:', repr(f.getint('aaa', 'a2')))
    print ('write to test4-2.ini')
    f.write(open('test4-2.ini', 'w'))
