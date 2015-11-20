#!/usr/bin/env python
import time

f = open('temp', 'w+')
f.write('the first line\n')
f.write('the second line\n')
f.write('the third line\n')
f.write('the fourth line\n')
f.write('the fifth line\n')
#f.flush()
#f.seek(0)
#print "in file temp:"
#for line in f:
#    print "# %s" % line ,
#print "END file temp."
#time.sleep(15)
f.write('the sixth line\n')
f.write('the seventh line\n')
#print "in file temp:"
#for line in f:
#    print "# %s" % line ,
#print "END file temp."


f.seek(-20, 1)
line = f.readlines()[-1]
print line
f.close()
