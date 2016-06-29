#!/usr/bin/env python
import time, os

#f = open('temp', 'w+')
#f.write('the first line\n')
#f.write('the second line\n')
#f.write('the third line\n')
#f.write('the fourth line\n')
#f.write('the fifth line\n')
##f.flush()
##f.seek(0)
##print "in file temp:"
##for line in f:
##    print "# %s" % line ,
##print "END file temp."
##time.sleep(15)
#f.write('the sixth line\n')
#f.write('the seventh line\n')
##print "in file temp:"
##for line in f:
##    print "# %s" % line ,
##print "END file temp."
#

print os.path.getsize('temp')
f = open('temp')
f.seek(-110, 2)
line = f.readlines()
print line
f.close()
