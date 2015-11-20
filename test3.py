#!/usr/bin/env python

import sys

f = open('temp', 'r+')
t = []
for line in f:
    sys.stdout.write(line)
    t.append(line[1:])
else:
    for tt in t:
        f.write(tt)
