#! /usr/bin/env python

import pprint

stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
tup = (stuff, 'spam', ('eggs', ('lumberjack', ('knights', ('ni', ('dead',('parrot', ('fresh fruit',))))))))
stuff.insert(0, tup)
a = ['aaa', 'bbb']
tt = []
tt.append(a)
tt.append(a)
print tt
pprint.pprint(tt)
print pprint.isrecursive(tt)
print pprint.pformat(tt)
print pprint.saferepr(tt)
