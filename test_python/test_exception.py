#!/usr/bin/env python

def foo():
    try:
        a = 1/0
        print a
        print "in try"
#    except NameError,e:
#        print "NameError:", e.message
#    except Exception,e:
#        print "Error:", e
#    else:
#        print "No error"
    finally:
        print "in final"

def test_finally():
    try:
        foo()
    finally:
        print "in test_finally finally"

def foo2(a=10):
    print a

if  __name__ == "__main__":
    foo2(20 if 1==2 else None)
