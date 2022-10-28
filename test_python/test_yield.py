#!/usr/bin/env python

import inspect
import sys


def foo(a=0, b=1):
    while True:
        try:
            t = yield b
        except:
            # print(e)
            print(sys.exc_info())
            t = None
            raise
        if t is not None:
            b = t
        a, b = b, a + b

def foo1():
    try:
        yield 1
        yield 2
    except:
        print(sys.exc_info())
    try:
        yield 3
        yield 4
    except:
        print(sys.exc_info())
        if sys.exc_info()[0] == GeneratorExit:
            return 999
    yield 5

def foo2():
    while True:
        data = yield
        print(f'foo2: {data}')
        f3.send(data * 2)

def foo3():
    while True:
        data = yield
        print(f'foo3: {data}')
        f2.send(data * 3)

f = foo()
print(f.send(None))
print(next(f))
print(next(f))
print(f.send(10))

# print(next(f))
# try:
#     print(f.throw(Exception, 'foo'))
# except Exception as e:
#     print(e)

print(next(f))

print(f.close())
print(inspect.getgeneratorstate(f))
# print(next(f))

f = foo1()
print(next(f))
print(f.throw(Exception, 'foo'))
print(f.close())
# print(next(f))

f2 = foo2()
next(f2)
f3 = foo3()
next(f3)
f2.send(1)




