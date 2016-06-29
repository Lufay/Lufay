#!/usr/bin/env python

class A:
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

a = A()
a.insmethod()
a.clsmethod()
#a.stmethod()
#A.clsmethod()
A.stmethod()
