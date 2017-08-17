#!/usr/bin/env python

def foo(a=0, b=1):
    while True:
        t = yield b
        if t is not None:
            b = t
        a, b = b, a + b

f = foo()
print f.next()
print f.next()
print f.send(10)
print f.next()
print f.next()
print f.next()
print f.next()
print f.next()
print f.close()
print f.next()


