#!/usr/bin/env python
import random

class B:
    def __iter__(self):
        return A()

class A:
#def __iter__(self):
#        return self

    def __init__(self):
        self.a = 0
        self.b = 1

    def insmethod(self):
        print 'in self'
        print self
        print self.__class__.__name__

#    @classmethod
    def clsmethod(cls):
        print 'in class'
        print cls

#    @staticmethod
    def stmethod():
        print 'in static'

    def next(self):
        t = self.a + self.b
        if t > 99:
            raise StopIteration
        self.a = self.b
        self.b = t
        return t

def foo():
    print 'in foo'

def func(f):
    f()

def foo2():
    return random.randint(10, 20)

ii = iter(foo2, 10)
while True:
    print ii.next()


