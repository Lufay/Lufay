#!/usr/bin/env python


def foo(a=[]):
    a.append('aa')
    return a

def foo1():
    x = y = z = 2
    def foo2():
        y = z = 3
        def foo3():
            z = 4
        print foo3.func_closure
        foo3()
    print foo2.func_closure
    print 'In foo1 of before:'
    print '"%s" %x %d' % ('w', id(w), w)
    print '"%s" %x %d' % ('x', id(x), x)
    print '"%s" %x %d' % ('y', id(y), y)
    print '"%s" %x %d' % ('z', id(z), z)
    print
    foo2()
    print 'In foo1 of after:'
    print '"%s" %x %d' % ('w', id(w), w)
    print '"%s" %x %d' % ('x', id(x), x)
    print '"%s" %x %d' % ('y', id(y), y)
    print '"%s" %x %d' % ('z', id(z), z)
    print

if __name__ == '__main__':
    w = x = y = z = 1
    print foo1.func_closure
    print 'In outer of before:'
    print '"%s" %x %d' % ('w', id(w), w)
    print '"%s" %x %d' % ('x', id(x), x)
    print '"%s" %x %d' % ('y', id(y), y)
    print '"%s" %x %d' % ('z', id(z), z)
    print
    foo1()
    print 'In outer of after:'
    print '"%s" %x %d' % ('w', id(w), w)
    print '"%s" %x %d' % ('x', id(x), x)
    print '"%s" %x %d' % ('y', id(y), y)
    print '"%s" %x %d' % ('z', id(z), z)
    print
