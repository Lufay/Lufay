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

if  __name__ == "__main__":
    try:
        test_finally()
    except NameError, e:
        print "in main NameError:", e
    except Exception,e:
        print "Error:", e
    print "end"
